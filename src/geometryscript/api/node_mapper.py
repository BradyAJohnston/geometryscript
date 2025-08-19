import bpy
import enum
import os
import re
from typing import Any, Dict, List, Optional, Set, Type as TypingType, Union

from .state import State
from .types import *
from .static.input_group import InputGroup
from .static.curve import Curve
from pathlib import Path


def absolute_path(component: Path | str) -> Path:
    """
    Returns the absolute path to a file in the addon directory.

    Alternative to `os.abspath` that works the same on macOS and Windows.
    """
    return Path(__file__).parent / component


# Constants
SOCKET_COLORS = {
    "INT": "#598C5C",
    "FLOAT": "#A1A1A1",
    "BOOLEAN": "#CCA6D6",
    "GEOMETRY": "#00D6A3",
    "VALUE": "#A1A1A1",
    "VECTOR": "#6363C7",
    "MATERIAL": "#EB7582",
    "TEXTURE": "#9E4FA3",
    "COLLECTION": "#F5F5F5",
    "OBJECT": "#ED9E5C",
    "STRING": "#70B2FF",
    "RGBA": "#C7C729",
}
DEFAULT_SOCKET_COLOR = "#A1A1A1"
DENYLIST_NODES = {"filter"}
DENYLIST_CLASSES = {"CompositorNodeMath", "TextureNodeMath"}
TEMP_NODE_GROUP_NAME = "temp_node_group"
NODE_TREE_TYPE = "GeometryNodeTree"


class OutputsList(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def set_or_create_link(x: Any, node_input: Any) -> None:
    if issubclass(type(x), Type):
        State.current_node_tree.links.new(x._socket, node_input)
    else:

        def link_constant():
            constant = Type(value=x)
            State.current_node_tree.links.new(constant._socket, node_input)

        if node_input.hide_value:
            link_constant()
        else:
            try:
                node_input.default_value = x
            except (TypeError, AttributeError):
                link_constant()


def _process_kwargs(kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """Process keyword arguments, expanding InputGroups and removing None values."""
    processed_kwargs = kwargs.copy()
    for k, v in kwargs.items():
        if isinstance(v, InputGroup):
            processed_kwargs = {**processed_kwargs, **v.__dict__}
            del processed_kwargs[k]
        if v is None and k in processed_kwargs:
            del processed_kwargs[k]
    return processed_kwargs


def _set_node_properties(node: Any, kwargs: Dict[str, Any]) -> None:
    """Set node properties from keyword arguments."""
    for prop in node.bl_rna.properties:
        argname = prop.identifier.lower().replace(" ", "_")
        if argname in kwargs:
            value = kwargs[argname]
            if (
                isinstance(value, list)
                and len(value) > 0
                and isinstance(value[0], Curve)
            ):
                for i, curve in enumerate(value):
                    curve.apply(getattr(node, prop.identifier).curves[i])
                continue
            if isinstance(value, Curve):
                value.apply(getattr(node, prop.identifier).curves[0])
                continue
            if isinstance(value, enum.Enum):
                value = value.value
            setattr(node, prop.identifier, value)


def _get_inputs_with_matching_name(
    node: Any, argname: str, primary_arg: Any
) -> List[Any]:
    """Get all node inputs with matching argument name and type."""
    all_with_name = []
    input_range = node.inputs[1:] if primary_arg is not None else node.inputs

    # Find the first input with this name to get the type
    reference_input = None
    for node_input in input_range:
        if node_input.name.lower().replace(" ", "_") == argname:
            reference_input = node_input
            break

    if reference_input is None:
        return all_with_name

    # Find all inputs with same name and type
    for node_input in input_range:
        if (
            node_input.name.lower().replace(" ", "_") == argname
            and node_input.type == reference_input.type
        ):
            all_with_name.append(node_input)

    return all_with_name


def _is_multi_input_iterable(node_input: Any, value: Any) -> bool:
    """Check if value is a valid multi-input iterable."""
    return (
        node_input.is_multi_input
        and hasattr(value, "__iter__")
        and len(value) > 0
        and issubclass(type(next(iter(value))), Type)
    )


def _is_tuple_for_multiple_inputs(all_with_name: List[Any], value: Any) -> bool:
    """Check if value is a tuple for multiple inputs."""
    return len(all_with_name) > 1 and issubclass(type(value), tuple) and len(value) > 0


def _set_node_inputs(node: Any, kwargs: Dict[str, Any], primary_arg: Any) -> None:
    """Set node inputs from keyword arguments."""
    input_range = node.inputs[1:] if primary_arg is not None else node.inputs

    for node_input in input_range:
        if not node_input.enabled:
            continue

        argname = node_input.name.lower().replace(" ", "_")
        if argname not in kwargs:
            continue

        all_with_name = _get_inputs_with_matching_name(node, argname, primary_arg)
        if not all_with_name:
            continue

        value = kwargs[argname]
        if isinstance(value, enum.Enum):
            value = value.value

        if _is_multi_input_iterable(node_input, value):
            for x in value:
                for input_socket in all_with_name:
                    State.current_node_tree.links.new(x._socket, input_socket)
        elif _is_tuple_for_multiple_inputs(all_with_name, value):
            for i, x in enumerate(value):
                set_or_create_link(x, all_with_name[i])
        else:
            for input_socket in all_with_name:
                set_or_create_link(value, input_socket)


def _create_outputs(node: Any) -> Union[Type, OutputsList]:
    """Create output objects from node outputs."""
    outputs = {}
    for node_output in node.outputs:
        if not node_output.enabled:
            continue
        outputs[node_output.name.lower().replace(" ", "_")] = Type(node_output)
    if len(outputs) == 1:
        return list(outputs.values())[0]
    else:
        return OutputsList(outputs)


def build_node(node_type: TypingType) -> Any:
    def build(_primary_arg=None, **kwargs):
        kwargs = _process_kwargs(kwargs)
        node = State.current_node_tree.nodes.new(node_type.__name__)
        if _primary_arg is not None:
            State.current_node_tree.links.new(_primary_arg._socket, node.inputs[0])
        _set_node_properties(node, kwargs)
        _set_node_inputs(node, kwargs, _primary_arg)
        return _create_outputs(node)

    return build


documentation: Dict[str, Any] = {}
registered_nodes: Set[Any] = set()


def _create_enum_type(
    node_type: TypingType, prop: Any, node_namespace_name: str
) -> None:
    """Create enum type for node property."""
    if node_namespace_name not in globals():

        class NodeNamespace:
            pass

        NodeNamespace.__name__ = node_namespace_name
        globals()[node_namespace_name] = NodeNamespace
    enum_type_name = prop.identifier.replace("_", " ").title().replace(" ", "")
    enum_type = enum.Enum(
        enum_type_name, {map_case_name(i): i.identifier for i in prop.enum_items}
    )
    setattr(globals()[node_namespace_name], enum_type_name, enum_type)


def register_node(node_type: TypingType, category_path: Optional[str] = None) -> None:
    if node_type in registered_nodes:
        return
    snake_case_name = node_type.bl_rna.name.lower().replace(" ", "_")
    node_namespace_name = snake_case_name.replace("_", " ").title().replace(" ", "")
    globals()[snake_case_name] = build_node(node_type)
    globals()[snake_case_name].bl_category_path = category_path
    globals()[snake_case_name].bl_node_type = node_type
    documentation[snake_case_name] = globals()[snake_case_name]

    def build_node_method(node_type_inner):
        def build(self, *args, **kwargs):
            return build_node(node_type_inner)(self, *args, **kwargs)

        return build

    setattr(Type, snake_case_name, build_node_method(node_type))

    parent_props = [
        prop.identifier
        for base in node_type.__bases__
        for prop in base.bl_rna.properties
    ]
    for prop in node_type.bl_rna.properties:
        if prop.identifier not in parent_props and prop.type == "ENUM":
            _create_enum_type(node_type, prop, node_namespace_name)
    registered_nodes.add(node_type)


def _discover_and_register_node_types() -> None:
    """Discover and register all available Blender node types."""
    node_types_to_register = []

    # Discover all node types from bpy.types
    for node_type_name in dir(bpy.types):
        node_type = getattr(bpy.types, node_type_name)
        if isinstance(node_type, type) and issubclass(node_type, bpy.types.Node):
            if (
                node_type.is_registered_node_type()
                and node_type.bl_rna.name.lower() not in DENYLIST_NODES
                and node_type.__name__ not in DENYLIST_CLASSES
            ):
                node_types_to_register.append(node_type)

    # Sort to prioritize GeometryNode types
    node_types_to_register.sort(
        key=lambda node_type: node_type.__name__.startswith("GeometryNode")
    )

    # Register all discovered node types
    for node_type in node_types_to_register:
        register_node(node_type)


def _collect_symbols_and_enums() -> tuple[List[str], Dict[str, List[str]]]:
    """Collect symbols and enums from all registered nodes for type stub generation."""
    temp_node_group = bpy.data.node_groups.new(TEMP_NODE_GROUP_NAME, NODE_TREE_TYPE)
    color_mappings = SOCKET_COLORS
    default_color = DEFAULT_SOCKET_COLOR
    symbols = []
    enums = {}
    skipped_nodes = []

    for func in sorted(documentation.keys()):
        try:
            method = documentation[func]
            node_instance = temp_node_group.nodes.new(method.bl_node_type.__name__)
            props_inputs = {}
            symbol_inputs = {}
            parent_props = [
                prop.identifier
                for base in method.bl_node_type.__bases__
                for prop in base.bl_rna.properties
            ]
            node_namespace_name = func.replace("_", " ").title().replace(" ", "")

            for prop in method.bl_node_type.bl_rna.properties:
                if prop.identifier not in parent_props:
                    if prop.type == "ENUM":
                        enum_name = (
                            prop.identifier.replace("_", " ").title().replace(" ", "")
                        )
                        enum_cases = "\n    ".join(
                            map(
                                lambda i: f"{map_case_name(i)} = '{i.identifier}'",
                                prop.enum_items,
                            )
                        )
                        if node_namespace_name not in enums:
                            enums[node_namespace_name] = []
                        enums[
                            node_namespace_name
                        ].append(f"""  class {enum_name}(enum.Enum):
    {enum_cases}""")
                        props_inputs[prop.identifier] = {
                            f'<span style="color: {color_mappings["STRING"]};">{node_namespace_name}.{enum_name}</span>': 1
                        }
                        symbol_inputs[prop.identifier] = {
                            f"{node_namespace_name}.{enum_name}": 1
                        }
                    else:
                        props_inputs[prop.identifier] = {
                            f'<span style="color: {color_mappings.get(prop.type, default_color)};">{prop.type.title()}</span>': 1
                        }
                        symbol_inputs[prop.identifier] = {prop.type.title(): 1}

            primary_arg = None
            for node_input in node_instance.inputs:
                name = node_input.name.lower().replace(" ", "_")
                typename = type(node_input).__name__.replace("NodeSocket", "")
                if node_input.is_multi_input:
                    typename = f"List[{typename}]"
                if name in props_inputs:
                    if typename in symbol_inputs[name]:
                        symbol_inputs[name][typename] += 1
                    else:
                        symbol_inputs[name][typename] = 1
                else:
                    symbol_inputs[name] = {typename: 1}
                if primary_arg is None:
                    primary_arg = (name, list(symbol_inputs[name].keys())[0])

            def collapse_inputs(inputs):
                for k, v in inputs.items():
                    values = []
                    for t, c in v.items():
                        for count in range(1, c + 1):
                            value = ""
                            if count > 1:
                                value += "Tuple["
                            value += ", ".join([t] * count)
                            if count > 1:
                                value += "]"
                            values.append(value)
                    inputs[k] = " | ".join(values)

            collapse_inputs(symbol_inputs)
            symbol_args = []
            for name, value in symbol_inputs.items():
                symbol_args.append(f"{name}: {value} | None = None")

            symbol_outputs = {}
            for node_output in node_instance.outputs:
                output_name = node_output.name.lower().replace(" ", "_")
                output_type = type(node_output).__name__.replace("NodeSocket", "")
                symbol_outputs[output_name] = output_type

            output_symbols = []
            for name, value in symbol_outputs.items():
                output_symbols.append(f"{name}: {value}")

            if len(output_symbols) > 1:
                if node_namespace_name not in enums:
                    enums[node_namespace_name] = []
                output_symbol_separator = "\n    "
                enums[node_namespace_name].append(f"""  class Result:
    {output_symbol_separator.join(output_symbols)}""")

            return_type_hint = (
                list(symbol_outputs.values())[0]
                if len(output_symbols) == 1
                else f"{node_namespace_name}.Result"
            )
            symbols.append(
                f"""def {func}({", ".join(symbol_args)}) -> {return_type_hint}: \"\"\"![](image_placeholder.webp)\"\"\""""
            )
        except Exception:
            skipped_nodes.append(documentation[func].bl_node_type.__name__)
            continue

    bpy.data.node_groups.remove(temp_node_group)
    return symbols, enums


def _create_type_stubs(symbols: List[str], enums: Dict[str, List[str]]) -> None:
    """Create geometry_script.pyi and geometry_script.py type stub files."""

    def type_symbol(t):
        return f"class {t.__name__}(Type): pass"

    def enum_namespace(k):
        newline = "\n"
        return f"""class {k}:
{newline.join(enums[k])}"""

    def add_self_arg(x):
        return re.sub(r"\(", "(self, ", x, 1)

    newline = "\n"
    contents = f"""from typing import *
import enum
def tree(builder):
  \"\"\"
  Marks a function as a node tree.
  \"\"\"
  pass
_SomeType = TypeVar('_SomeType', bound='Type')
class Type:
  def __add__(self, other) -> Type: return self
  def __radd__(self, other) -> Type: return self
  def __sub__(self, other) -> Type: return self
  def __rsub__(self, other) -> Type: return self
  def __mul__(self, other) -> Type: return self
  def __rmul__(self, other) -> Type: return self
  def __truediv__(self, other) -> Type: return self
  def __rtruediv__(self, other) -> Type: return self
  def __mod__(self, other) -> Type: return self
  def __rmod__(self, other) -> Type: return self
  def __eq__(self, other) -> Type: return self
  def __ne__(self, other) -> Type: return self
  def __lt__(self, other) -> Type: return self
  def __le__(self, other) -> Type: return self
  def __gt__(self, other) -> Type: return self
  def __ge__(self, other) -> Type: return self
  def __invert__(self) -> Type: return self
  def __getitem__(
    self,
    subscript: _SomeType | slice | Tuple[_SomeType | slice, SampleMode]
  ) -> Type: return self
  x = Type()
  y = Type()
  z = Type()
  def capture(self, attribute: Type, **kwargs) -> (Geometry, Type): return Geometry(), Type()
  def transfer(self, attribute: Type, **kwargs) -> Type: return Type()
  {(newline + "  ").join(map(add_self_arg, filter(lambda x: x.startswith("def"), symbols)))}
  
{newline.join(map(type_symbol, Type.__subclasses__()))}
{newline.join(map(enum_namespace, enums.keys()))}
{newline.join(symbols)}"""

    # Add static API content
    static_path = absolute_path("api/static")
    static_path.mkdir(exist_ok=True, parents=True)
    for path in static_path.glob("*.py"):
        if path.suffix != ".py":
            continue
        with open(path, "r") as static_api:
            contents += f"\n\n# {path.name}\n{static_api.read()}"

    # Write both .pyi and .py files
    typeshed_path = absolute_path("typeshed")
    typeshed_path.mkdir(exist_ok=True, parents=True)
    with open(typeshed_path / "geometry_script.pyi", "w") as fpyi:
        fpyi.write(contents)
    with open(typeshed_path / "geometry_script.py", "w") as fpy:
        fpy.write(contents)


def create_type_stubs() -> None:
    """Create type stub files without generating HTML documentation."""
    _discover_and_register_node_types()  # Ensure all nodes are registered
    symbols, enums = _collect_symbols_and_enums()
    _create_type_stubs(symbols, enums)


def initialize_node_mapper() -> None:
    """Initialize the node mapper by discovering and registering all node types."""
    _discover_and_register_node_types()


def setup_types() -> None:
    """Setup types by creating type stubs."""
    initialize_node_mapper()
    create_type_stubs()
