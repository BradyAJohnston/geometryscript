from typing import *
import enum
def tree(builder):
  """
  Marks a function as a node tree.
  """
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
  def 3d_cursor(self, ) -> 3DCursor.Result: """![](image_placeholder.webp)"""
  def accumulate_field(self, data_type: AccumulateField.DataType | None = None, domain: AccumulateField.Domain | None = None, value: Float | None = None, group_id: Int | None = None) -> AccumulateField.Result: """![](image_placeholder.webp)"""
  def active_camera(self, ) -> Object: """![](image_placeholder.webp)"""
  def active_element(self, domain: ActiveElement.Domain | None = None) -> ActiveElement.Result: """![](image_placeholder.webp)"""
  def align_euler_to_vector(self, axis: AlignEulerToVector.Axis | None = None, pivot_axis: AlignEulerToVector.PivotAxis | None = None, rotation: VectorEuler | None = None, factor: FloatFactor | None = None, vector: Vector | None = None) -> VectorEuler: """![](image_placeholder.webp)"""
  def align_rotation_to_vector(self, axis: AlignRotationToVector.Axis | None = None, pivot_axis: AlignRotationToVector.PivotAxis | None = None, rotation: Rotation | None = None, factor: FloatFactor | None = None, vector: VectorXYZ | None = None) -> Rotation: """![](image_placeholder.webp)"""
  def arc(self, mode: Arc.Mode | None = None, resolution: IntUnsigned | None = None, start: VectorTranslation | None = None, middle: VectorTranslation | None = None, end: VectorTranslation | None = None, radius: FloatDistance | None = None, start_angle: FloatAngle | None = None, sweep_angle: FloatAngle | None = None, offset_angle: FloatAngle | None = None, connect_center: Bool | None = None, invert_arc: Bool | None = None) -> Arc.Result: """![](image_placeholder.webp)"""
  def attribute_statistic(self, data_type: AttributeStatistic.DataType | None = None, domain: AttributeStatistic.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None, attribute: Float | None = None) -> AttributeStatistic.Result: """![](image_placeholder.webp)"""
  def axes_to_rotation(self, primary_axis: AxesToRotation.PrimaryAxis | Vector | None = None, secondary_axis: AxesToRotation.SecondaryAxis | Vector | None = None) -> Rotation: """![](image_placeholder.webp)"""
  def axis_angle_to_rotation(self, axis: Vector | None = None, angle: FloatAngle | None = None) -> Rotation: """![](image_placeholder.webp)"""
  def bake(self, bake_items: Collection | None = None, active_index: Int | None = None, active_item: Pointer | None = None, geometry: Geometry | None = None, : Virtual | None = None) -> Bake.Result: """![](image_placeholder.webp)"""
  def bit_math(self, operation: BitMath.Operation | None = None, a: Int | None = None, b: Int | None = None, shift: Int | None = None) -> Int: """![](image_placeholder.webp)"""
  def blackbody(self, temperature: FloatColorTemperature | None = None) -> Color: """![](image_placeholder.webp)"""
  def blur_attribute(self, data_type: BlurAttribute.DataType | None = None, value: Float | None = None, iterations: Int | None = None, weight: FloatFactor | None = None) -> Float: """![](image_placeholder.webp)"""
  def boolean(self, boolean: Boolean | None = None) -> Bool: """![](image_placeholder.webp)"""
  def boolean_math(self, operation: BooleanMath.Operation | None = None, boolean: Bool | None = None) -> Bool: """![](image_placeholder.webp)"""
  def bounding_box(self, geometry: Geometry | None = None, use_radius: Bool | None = None) -> BoundingBox.Result: """![](image_placeholder.webp)"""
  def brick_texture(self, texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, offset_frequency: Int | None = None, squash_frequency: Int | None = None, offset: Float | None = None, squash: Float | None = None, vector: Vector | None = None, color1: Color | None = None, color2: Color | None = None, mortar: Color | None = None, scale: Float | None = None, mortar_size: Float | None = None, mortar_smooth: Float | None = None, bias: Float | None = None, brick_width: Float | None = None, row_height: Float | None = None) -> BrickTexture.Result: """![](image_placeholder.webp)"""
  def bézier_segment(self, mode: BézierSegment.Mode | None = None, resolution: IntUnsigned | None = None, start: VectorTranslation | None = None, start_handle: VectorTranslation | None = None, end_handle: VectorTranslation | None = None, end: VectorTranslation | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def camera_info(self, camera: Object | None = None) -> CameraInfo.Result: """![](image_placeholder.webp)"""
  def capture_attribute(self, capture_items: Collection | None = None, active_index: Int | None = None, active_item: Pointer | None = None, domain: CaptureAttribute.Domain | None = None, geometry: Geometry | None = None, : Virtual | None = None) -> CaptureAttribute.Result: """![](image_placeholder.webp)"""
  def checker_texture(self, texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, vector: Vector | None = None, color1: Color | None = None, color2: Color | None = None, scale: Float | None = None) -> CheckerTexture.Result: """![](image_placeholder.webp)"""
  def clamp(self, clamp_type: Clamp.ClampType | None = None, value: Float | None = None, min: Float | None = None, max: Float | None = None) -> Float: """![](image_placeholder.webp)"""
  def closure_input(self, paired_output: Pointer | None = None) -> Virtual: """![](image_placeholder.webp)"""
  def closure_output(self, input_items: Collection | None = None, output_items: Collection | None = None, active_input_index: Int | None = None, active_output_index: Int | None = None, : Virtual | None = None) -> Closure: """![](image_placeholder.webp)"""
  def collection(self, collection: Pointer | None = None) -> Collection: """![](image_placeholder.webp)"""
  def collection_info(self, transform_space: CollectionInfo.TransformSpace | None = None, collection: Collection | None = None, separate_children: Bool | None = None, reset_children: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def color(self, value: Float | None = None) -> Color: """![](image_placeholder.webp)"""
  def combine_bundle(self, bundle_items: Collection | None = None, active_index: Int | None = None, : Virtual | None = None) -> Bundle: """![](image_placeholder.webp)"""
  def combine_matrix(self, column_1_row_1: Float | None = None, column_1_row_2: Float | None = None, column_1_row_3: Float | None = None, column_1_row_4: Float | None = None, column_2_row_1: Float | None = None, column_2_row_2: Float | None = None, column_2_row_3: Float | None = None, column_2_row_4: Float | None = None, column_3_row_1: Float | None = None, column_3_row_2: Float | None = None, column_3_row_3: Float | None = None, column_3_row_4: Float | None = None, column_4_row_1: Float | None = None, column_4_row_2: Float | None = None, column_4_row_3: Float | None = None, column_4_row_4: Float | None = None) -> Matrix: """![](image_placeholder.webp)"""
  def combine_rgb_(self, legacy)(r: Float | None = None, g: Float | None = None, b: Float | None = None) -> Color: """![](image_placeholder.webp)"""
  def combine_transform(self, translation: VectorTranslation | None = None, rotation: Rotation | None = None, scale: VectorXYZ | None = None) -> Matrix: """![](image_placeholder.webp)"""
  def combine_xyz(self, x: Float | None = None, y: Float | None = None, z: Float | None = None) -> Vector: """![](image_placeholder.webp)"""
  def compare(self, operation: Compare.Operation | None = None, data_type: Compare.DataType | None = None, mode: Compare.Mode | None = None, a: String | None = None, b: String | None = None, c: Float | None = None, angle: FloatAngle | None = None, epsilon: Float | None = None) -> Bool: """![](image_placeholder.webp)"""
  def cone(self, fill_type: Cone.FillType | None = None, vertices: Int | None = None, side_segments: Int | None = None, fill_segments: Int | None = None, radius_top: FloatDistance | None = None, radius_bottom: FloatDistance | None = None, depth: FloatDistance | None = None) -> Cone.Result: """![](image_placeholder.webp)"""
  def convex_hull(self, geometry: Geometry | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def corners_of_edge(self, edge_index: Int | None = None, weights: Float | None = None, sort_index: Int | None = None) -> CornersOfEdge.Result: """![](image_placeholder.webp)"""
  def corners_of_face(self, face_index: Int | None = None, weights: Float | None = None, sort_index: Int | None = None) -> CornersOfFace.Result: """![](image_placeholder.webp)"""
  def corners_of_vertex(self, vertex_index: Int | None = None, weights: Float | None = None, sort_index: Int | None = None) -> CornersOfVertex.Result: """![](image_placeholder.webp)"""
  def cube(self, size: VectorTranslation | None = None, vertices_x: Int | None = None, vertices_y: Int | None = None, vertices_z: Int | None = None) -> Cube.Result: """![](image_placeholder.webp)"""
  def curve_circle(self, mode: CurveCircle.Mode | None = None, resolution: Int | None = None, point_1: VectorTranslation | None = None, point_2: VectorTranslation | None = None, point_3: VectorTranslation | None = None, radius: FloatDistance | None = None) -> CurveCircle.Result: """![](image_placeholder.webp)"""
  def curve_handle_positions(self, relative: Bool | None = None) -> CurveHandlePositions.Result: """![](image_placeholder.webp)"""
  def curve_length(self, curve: Geometry | None = None) -> Float: """![](image_placeholder.webp)"""
  def curve_line(self, mode: CurveLine.Mode | None = None, start: VectorTranslation | None = None, end: VectorTranslation | None = None, direction: Vector | None = None, length: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def curve_of_point(self, point_index: Int | None = None) -> CurveOfPoint.Result: """![](image_placeholder.webp)"""
  def curve_tangent(self, ) -> Vector: """![](image_placeholder.webp)"""
  def curve_tilt(self, ) -> Float: """![](image_placeholder.webp)"""
  def curve_to_mesh(self, curve: Geometry | None = None, profile_curve: Geometry | None = None, scale: Float | None = None, fill_caps: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def curve_to_points(self, mode: CurveToPoints.Mode | None = None, curve: Geometry | None = None, count: Int | None = None, length: FloatDistance | None = None) -> CurveToPoints.Result: """![](image_placeholder.webp)"""
  def curves_to_grease_pencil(self, curves: Geometry | None = None, selection: Bool | None = None, instances_as_layers: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def cylinder(self, fill_type: Cylinder.FillType | None = None, vertices: Int | None = None, side_segments: Int | None = None, fill_segments: Int | None = None, radius: FloatDistance | None = None, depth: FloatDistance | None = None) -> Cylinder.Result: """![](image_placeholder.webp)"""
  def deform_curves_on_surface(self, curves: Geometry | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def delete_geometry(self, mode: DeleteGeometry.Mode | None = None, domain: DeleteGeometry.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def dial_gizmo(self, color_id: DialGizmo.ColorId | None = None, value: List[Float] | None = None, position: VectorTranslation | None = None, up: VectorXYZ | None = None, screen_space: Bool | None = None, radius: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def distribute_points_in_grid(self, mode: DistributePointsInGrid.Mode | None = None, grid: Float | None = None, density: Float | None = None, seed: Int | None = None, spacing: VectorXYZ | None = None, threshold: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def distribute_points_in_volume(self, mode: DistributePointsInVolume.Mode | None = None, volume: Geometry | None = None, density: Float | None = None, seed: Int | None = None, spacing: VectorXYZ | None = None, threshold: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def distribute_points_on_faces(self, distribute_method: DistributePointsOnFaces.DistributeMethod | None = None, use_legacy_normal: Boolean | None = None, mesh: Geometry | None = None, selection: Bool | None = None, distance_min: FloatDistance | None = None, density_max: Float | None = None, density: Float | None = None, density_factor: FloatFactor | None = None, seed: Int | None = None) -> DistributePointsOnFaces.Result: """![](image_placeholder.webp)"""
  def domain_size(self, component: DomainSize.Component | None = None, geometry: Geometry | None = None) -> DomainSize.Result: """![](image_placeholder.webp)"""
  def dual_mesh(self, mesh: Geometry | None = None, keep_boundaries: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def duplicate_elements(self, domain: DuplicateElements.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None, amount: Int | None = None) -> DuplicateElements.Result: """![](image_placeholder.webp)"""
  def edge_angle(self, ) -> EdgeAngle.Result: """![](image_placeholder.webp)"""
  def edge_neighbors(self, ) -> Int: """![](image_placeholder.webp)"""
  def edge_paths_to_curves(self, mesh: Geometry | None = None, start_vertices: Bool | None = None, next_vertex_index: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def edge_paths_to_selection(self, start_vertices: Bool | None = None, next_vertex_index: Int | None = None) -> Bool: """![](image_placeholder.webp)"""
  def edge_vertices(self, ) -> EdgeVertices.Result: """![](image_placeholder.webp)"""
  def edges_of_corner(self, corner_index: Int | None = None) -> EdgesOfCorner.Result: """![](image_placeholder.webp)"""
  def edges_of_vertex(self, vertex_index: Int | None = None, weights: Float | None = None, sort_index: Int | None = None) -> EdgesOfVertex.Result: """![](image_placeholder.webp)"""
  def edges_to_face_groups(self, boundary_edges: Bool | None = None) -> Int: """![](image_placeholder.webp)"""
  def endpoint_selection(self, start_size: Int | None = None, end_size: Int | None = None) -> Bool: """![](image_placeholder.webp)"""
  def euler_to_rotation(self, euler: VectorEuler | None = None) -> Rotation: """![](image_placeholder.webp)"""
  def evaluate_at_index(self, domain: EvaluateAtIndex.Domain | None = None, data_type: EvaluateAtIndex.DataType | None = None, value: Float | None = None, index: Int | None = None) -> Float: """![](image_placeholder.webp)"""
  def evaluate_closure(self, input_items: Collection | None = None, output_items: Collection | None = None, active_input_index: Int | None = None, active_output_index: Int | None = None, closure: Closure | None = None, : Virtual | None = None) -> Virtual: """![](image_placeholder.webp)"""
  def evaluate_on_domain(self, domain: EvaluateOnDomain.Domain | None = None, data_type: EvaluateOnDomain.DataType | None = None, value: Float | None = None) -> Float: """![](image_placeholder.webp)"""
  def extrude_mesh(self, mode: ExtrudeMesh.Mode | None = None, mesh: Geometry | None = None, selection: Bool | None = None, offset: VectorTranslation | None = None, offset_scale: Float | None = None, individual: Bool | None = None) -> ExtrudeMesh.Result: """![](image_placeholder.webp)"""
  def face_area(self, ) -> Float: """![](image_placeholder.webp)"""
  def face_group_boundaries(self, face_group_id: Int | None = None) -> Bool: """![](image_placeholder.webp)"""
  def face_neighbors(self, ) -> FaceNeighbors.Result: """![](image_placeholder.webp)"""
  def face_of_corner(self, corner_index: Int | None = None) -> FaceOfCorner.Result: """![](image_placeholder.webp)"""
  def face_set(self, ) -> FaceSet.Result: """![](image_placeholder.webp)"""
  def field_average(self, data_type: FieldAverage.DataType | None = None, domain: FieldAverage.Domain | None = None, value: Float | None = None, group_id: Int | None = None) -> FieldAverage.Result: """![](image_placeholder.webp)"""
  def field_min_&_max(self, data_type: FieldMin&Max.DataType | None = None, domain: FieldMin&Max.Domain | None = None, value: Float | None = None, group_id: Int | None = None) -> FieldMin&Max.Result: """![](image_placeholder.webp)"""
  def field_variance(self, data_type: FieldVariance.DataType | None = None, domain: FieldVariance.Domain | None = None, value: Float | None = None, group_id: Int | None = None) -> FieldVariance.Result: """![](image_placeholder.webp)"""
  def fill_curve(self, mode: FillCurve.Mode | None = None, curve: Geometry | None = None, group_id: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def fillet_curve(self, mode: FilletCurve.Mode | None = None, curve: Geometry | None = None, count: Int | None = None, radius: FloatDistance | None = None, limit_radius: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def find_in_string(self, string: String | None = None, search: String | None = None) -> FindInString.Result: """![](image_placeholder.webp)"""
  def flip_faces(self, mesh: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def float_curve(self, mapping: Pointer | None = None, factor: FloatFactor | None = None, value: Float | None = None) -> Float: """![](image_placeholder.webp)"""
  def float_to_integer(self, rounding_mode: FloatToInteger.RoundingMode | None = None, float: Float | None = None) -> Int: """![](image_placeholder.webp)"""
  def for_each_geometry_element_input(self, paired_output: Pointer | None = None, geometry: Geometry | None = None, selection: Bool | None = None, : Virtual | None = None) -> ForEachGeometryElementInput.Result: """![](image_placeholder.webp)"""
  def for_each_geometry_element_output(self, input_items: Collection | None = None, main_items: Collection | None = None, generation_items: Collection | None = None, active_input_index: Int | None = None, active_generation_index: Int | None = None, active_main_index: Int | None = None, domain: ForEachGeometryElementOutput.Domain | None = None, inspection_index: Int | None = None, : Virtual | None = None, geometry: Geometry | None = None) -> ForEachGeometryElementOutput.Result: """![](image_placeholder.webp)"""
  def format_string(self, format_items: Collection | None = None, active_index: Int | None = None, format: String | None = None, : Virtual | None = None) -> String: """![](image_placeholder.webp)"""
  def frame(self, text: Pointer | None = None, shrink: Boolean | None = None, label_size: Int | None = None) -> Frame.Result: """![](image_placeholder.webp)"""
  def gabor_texture(self, texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, gabor_type: GaborTexture.GaborType | None = None, vector: Vector | None = None, scale: Float | None = None, frequency: Float | None = None, anisotropy: FloatFactor | None = None, orientation: VectorDirection | None = None) -> GaborTexture.Result: """![](image_placeholder.webp)"""
  def geometry_proximity(self, target_element: GeometryProximity.TargetElement | None = None, geometry: Geometry | None = None, group_id: Int | None = None, sample_position: Vector | None = None, sample_group_id: Int | None = None) -> GeometryProximity.Result: """![](image_placeholder.webp)"""
  def geometry_to_instance(self, geometry: List[Geometry] | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def get_named_grid(self, data_type: GetNamedGrid.DataType | None = None, volume: Geometry | None = None, name: String | None = None, remove: Bool | None = None) -> GetNamedGrid.Result: """![](image_placeholder.webp)"""
  def gradient_texture(self, texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, gradient_type: GradientTexture.GradientType | None = None, vector: Vector | None = None) -> GradientTexture.Result: """![](image_placeholder.webp)"""
  def grease_pencil_to_curves(self, grease_pencil: Geometry | None = None, selection: Bool | None = None, layers_as_instances: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def grid(self, size_x: FloatDistance | None = None, size_y: FloatDistance | None = None, vertices_x: Int | None = None, vertices_y: Int | None = None) -> Grid.Result: """![](image_placeholder.webp)"""
  def grid_info(self, data_type: GridInfo.DataType | None = None, grid: Float | None = None) -> GridInfo.Result: """![](image_placeholder.webp)"""
  def grid_to_mesh(self, grid: Float | None = None, threshold: Float | None = None, adaptivity: FloatFactor | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def group(self, node_tree: Pointer | None = None) -> Group.Result: """![](image_placeholder.webp)"""
  def group_input(self, ) -> Virtual: """![](image_placeholder.webp)"""
  def group_output(self, is_active_output: Boolean | None = None, : Virtual | None = None) -> GroupOutput.Result: """![](image_placeholder.webp)"""
  def handle_type_selection(self, handle_type: HandleTypeSelection.HandleType | None = None, mode: HandleTypeSelection.Mode | None = None) -> Bool: """![](image_placeholder.webp)"""
  def hash_value(self, data_type: HashValue.DataType | None = None, value: Int | None = None, seed: Int | None = None) -> Int: """![](image_placeholder.webp)"""
  def ico_sphere(self, radius: FloatDistance | None = None, subdivisions: Int | None = None) -> IcoSphere.Result: """![](image_placeholder.webp)"""
  def id(self, ) -> Int: """![](image_placeholder.webp)"""
  def image(self, image: Pointer | None = None) -> Image: """![](image_placeholder.webp)"""
  def image_info(self, image: Image | None = None, frame: Int | None = None) -> ImageInfo.Result: """![](image_placeholder.webp)"""
  def image_texture(self, interpolation: ImageTexture.Interpolation | None = None, extension: ImageTexture.Extension | None = None, image: Image | None = None, vector: Vector | None = None, frame: Int | None = None) -> ImageTexture.Result: """![](image_placeholder.webp)"""
  def import_csv(self, path: StringFilePath | None = None, delimiter: String | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def import_obj(self, path: StringFilePath | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def import_ply(self, path: StringFilePath | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def import_stl(self, path: StringFilePath | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def import_text(self, path: StringFilePath | None = None) -> String: """![](image_placeholder.webp)"""
  def import_vdb(self, path: StringFilePath | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def index(self, ) -> Int: """![](image_placeholder.webp)"""
  def index_of_nearest(self, position: Vector | None = None, group_id: Int | None = None) -> IndexOfNearest.Result: """![](image_placeholder.webp)"""
  def index_switch(self, index_switch_items: Collection | None = None, data_type: IndexSwitch.DataType | None = None, index: Int | None = None, 0: Geometry | None = None, 1: Geometry | None = None, : Virtual | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def instance_bounds(self, use_radius: Bool | None = None) -> InstanceBounds.Result: """![](image_placeholder.webp)"""
  def instance_on_points(self, points: Geometry | None = None, selection: Bool | None = None, instance: Geometry | None = None, pick_instance: Bool | None = None, instance_index: Int | None = None, rotation: Rotation | None = None, scale: VectorXYZ | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def instance_rotation(self, ) -> Rotation: """![](image_placeholder.webp)"""
  def instance_scale(self, ) -> Vector: """![](image_placeholder.webp)"""
  def instance_transform(self, ) -> Matrix: """![](image_placeholder.webp)"""
  def instances_to_points(self, instances: Geometry | None = None, selection: Bool | None = None, position: Vector | None = None, radius: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def integer(self, integer: Int | None = None) -> Int: """![](image_placeholder.webp)"""
  def integer_math(self, operation: IntegerMath.Operation | None = None, value: Int | None = None) -> Int: """![](image_placeholder.webp)"""
  def interpolate_curves(self, guide_curves: Geometry | None = None, guide_up: Vector | None = None, guide_group_id: Int | None = None, points: Geometry | None = None, point_up: Vector | None = None, point_group_id: Int | None = None, max_neighbors: Int | None = None) -> InterpolateCurves.Result: """![](image_placeholder.webp)"""
  def invert_matrix(self, matrix: Matrix | None = None) -> InvertMatrix.Result: """![](image_placeholder.webp)"""
  def invert_rotation(self, rotation: Rotation | None = None) -> Rotation: """![](image_placeholder.webp)"""
  def is_edge_smooth(self, ) -> Bool: """![](image_placeholder.webp)"""
  def is_face_planar(self, threshold: FloatDistance | None = None) -> Bool: """![](image_placeholder.webp)"""
  def is_face_smooth(self, ) -> Bool: """![](image_placeholder.webp)"""
  def is_spline_cyclic(self, ) -> Bool: """![](image_placeholder.webp)"""
  def is_viewport(self, ) -> Bool: """![](image_placeholder.webp)"""
  def join_geometry(self, geometry: List[Geometry] | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def join_strings(self, delimiter: String | None = None, strings: List[String] | None = None) -> String: """![](image_placeholder.webp)"""
  def linear_gizmo(self, color_id: LinearGizmo.ColorId | None = None, draw_style: LinearGizmo.DrawStyle | None = None, value: List[Float] | None = None, position: VectorTranslation | None = None, direction: VectorXYZ | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def magic_texture(self, texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, turbulence_depth: Int | None = None, vector: Vector | None = None, scale: Float | None = None, distortion: Float | None = None) -> MagicTexture.Result: """![](image_placeholder.webp)"""
  def map_range(self, clamp: Boolean | None = None, interpolation_type: MapRange.InterpolationType | None = None, data_type: MapRange.DataType | None = None, value: Float | None = None, from_min: Vector | None = None, from_max: Vector | None = None, to_min: Vector | None = None, to_max: Vector | None = None, steps: Vector | None = None, vector: Vector | None = None) -> MapRange.Result: """![](image_placeholder.webp)"""
  def match_string(self, operation: MatchString.Operation | None = None, string: String | None = None, key: String | None = None) -> Bool: """![](image_placeholder.webp)"""
  def material(self, material: Pointer | None = None) -> Material: """![](image_placeholder.webp)"""
  def material_index(self, ) -> Int: """![](image_placeholder.webp)"""
  def material_selection(self, material: Material | None = None) -> Bool: """![](image_placeholder.webp)"""
  def math(self, operation: Math.Operation | None = None, use_clamp: Boolean | None = None, value: Float | None = None) -> Float: """![](image_placeholder.webp)"""
  def matrix_determinant(self, matrix: Matrix | None = None) -> Float: """![](image_placeholder.webp)"""
  def menu_switch(self, enum_items: Collection | None = None, active_index: Int | None = None, active_item: Pointer | None = None, enum_definition: Pointer | None = None, data_type: MenuSwitch.DataType | None = None, menu: Menu | None = None, a: Geometry | None = None, b: Geometry | None = None, : Virtual | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def merge_by_distance(self, mode: MergeByDistance.Mode | None = None, geometry: Geometry | None = None, selection: Bool | None = None, distance: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def merge_layers(self, mode: MergeLayers.Mode | None = None, grease_pencil: Geometry | None = None, selection: Bool | None = None, group_id: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def mesh_boolean(self, operation: MeshBoolean.Operation | None = None, solver: MeshBoolean.Solver | None = None, mesh_1: Geometry | None = None, mesh_2: List[Geometry] | None = None, self_intersection: Bool | None = None, hole_tolerant: Bool | None = None) -> MeshBoolean.Result: """![](image_placeholder.webp)"""
  def mesh_circle(self, fill_type: MeshCircle.FillType | None = None, vertices: Int | None = None, radius: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def mesh_island(self, ) -> MeshIsland.Result: """![](image_placeholder.webp)"""
  def mesh_line(self, mode: MeshLine.Mode | None = None, count_mode: MeshLine.CountMode | None = None, count: Int | None = None, resolution: FloatDistance | None = None, start_location: VectorTranslation | None = None, offset: VectorTranslation | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def mesh_to_curve(self, mode: MeshToCurve.Mode | None = None, mesh: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def mesh_to_density_grid(self, mesh: Geometry | None = None, density: Float | None = None, voxel_size: FloatDistance | None = None, gradient_width: FloatDistance | None = None) -> Float: """![](image_placeholder.webp)"""
  def mesh_to_points(self, mode: MeshToPoints.Mode | None = None, mesh: Geometry | None = None, selection: Bool | None = None, position: Vector | None = None, radius: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def mesh_to_sdf_grid(self, mesh: Geometry | None = None, voxel_size: FloatDistance | None = None, band_width: Int | None = None) -> Float: """![](image_placeholder.webp)"""
  def mesh_to_volume(self, resolution_mode: MeshToVolume.ResolutionMode | None = None, mesh: Geometry | None = None, density: Float | None = None, voxel_size: FloatDistance | None = None, voxel_amount: Float | None = None, interior_band_width: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def mix_(self, legacy)(blend_type: Mix(Legacy).BlendType | None = None, use_alpha: Boolean | None = None, use_clamp: Boolean | None = None, fac: FloatFactor | None = None, color1: Color | None = None, color2: Color | None = None) -> Color: """![](image_placeholder.webp)"""
  def mouse_position(self, ) -> MousePosition.Result: """![](image_placeholder.webp)"""
  def multiply_matrices(self, matrix: Matrix | None = None) -> Matrix: """![](image_placeholder.webp)"""
  def named_attribute(self, data_type: NamedAttribute.DataType | None = None, name: String | None = None) -> NamedAttribute.Result: """![](image_placeholder.webp)"""
  def named_layer_selection(self, name: String | None = None) -> Bool: """![](image_placeholder.webp)"""
  def noise_texture(self, texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, noise_dimensions: NoiseTexture.NoiseDimensions | None = None, noise_type: NoiseTexture.NoiseType | None = None, normalize: Boolean | None = None, vector: Vector | None = None, w: Float | None = None, scale: Float | None = None, detail: Float | None = None, roughness: FloatFactor | None = None, lacunarity: Float | None = None, offset: Float | None = None, gain: Float | None = None, distortion: Float | None = None) -> NoiseTexture.Result: """![](image_placeholder.webp)"""
  def normal(self, legacy_corner_normals: Boolean | None = None) -> Normal.Result: """![](image_placeholder.webp)"""
  def object(self, object: Pointer | None = None) -> Object: """![](image_placeholder.webp)"""
  def object_info(self, transform_space: ObjectInfo.TransformSpace | None = None, object: Object | None = None, as_instance: Bool | None = None) -> ObjectInfo.Result: """![](image_placeholder.webp)"""
  def offset_corner_in_face(self, corner_index: Int | None = None, offset: Int | None = None) -> Int: """![](image_placeholder.webp)"""
  def offset_point_in_curve(self, point_index: Int | None = None, offset: Int | None = None) -> OffsetPointInCurve.Result: """![](image_placeholder.webp)"""
  def pack_uv_islands(self, uv: Vector | None = None, selection: Bool | None = None, margin: Float | None = None, rotate: Bool | None = None) -> Vector: """![](image_placeholder.webp)"""
  def points(self, count: Int | None = None, position: VectorTranslation | None = None, radius: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def points_of_curve(self, curve_index: Int | None = None, weights: Float | None = None, sort_index: Int | None = None) -> PointsOfCurve.Result: """![](image_placeholder.webp)"""
  def points_to_curves(self, points: Geometry | None = None, curve_group_id: Int | None = None, weight: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def points_to_sdf_grid(self, points: Geometry | None = None, radius: FloatDistance | None = None, voxel_size: FloatDistance | None = None) -> Float: """![](image_placeholder.webp)"""
  def points_to_vertices(self, points: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def points_to_volume(self, resolution_mode: PointsToVolume.ResolutionMode | None = None, points: Geometry | None = None, density: Float | None = None, voxel_size: FloatDistance | None = None, voxel_amount: Float | None = None, radius: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def position(self, ) -> Vector: """![](image_placeholder.webp)"""
  def project_point(self, vector: VectorXYZ | None = None, transform: Matrix | None = None) -> VectorXYZ: """![](image_placeholder.webp)"""
  def quadratic_bézier(self, resolution: IntUnsigned | None = None, start: VectorTranslation | None = None, middle: VectorTranslation | None = None, end: VectorTranslation | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def quadrilateral(self, mode: Quadrilateral.Mode | None = None, width: FloatDistance | None = None, height: FloatDistance | None = None, bottom_width: FloatDistance | None = None, top_width: FloatDistance | None = None, offset: FloatDistance | None = None, bottom_height: FloatDistance | None = None, top_height: FloatDistance | None = None, point_1: VectorTranslation | None = None, point_2: VectorTranslation | None = None, point_3: VectorTranslation | None = None, point_4: VectorTranslation | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def quaternion_to_rotation(self, w: Float | None = None, x: Float | None = None, y: Float | None = None, z: Float | None = None) -> Rotation: """![](image_placeholder.webp)"""
  def radius(self, ) -> Float: """![](image_placeholder.webp)"""
  def random_value(self, data_type: RandomValue.DataType | None = None, min: Int | None = None, max: Int | None = None, probability: FloatFactor | None = None, id: Int | None = None, seed: Int | None = None) -> Bool: """![](image_placeholder.webp)"""
  def raycast(self, mapping: Raycast.Mapping | None = None, data_type: Raycast.DataType | None = None, target_geometry: Geometry | None = None, attribute: Float | None = None, source_position: Vector | None = None, ray_direction: Vector | None = None, ray_length: FloatDistance | None = None) -> Raycast.Result: """![](image_placeholder.webp)"""
  def realize_instances(self, geometry: Geometry | None = None, selection: Bool | None = None, realize_all: Bool | None = None, depth: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def remove_named_attribute(self, pattern_mode: RemoveNamedAttribute.PatternMode | None = None, geometry: Geometry | None = None, name: String | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def repeat_input(self, paired_output: Pointer | None = None, iterations: Int | None = None, : Virtual | None = None) -> RepeatInput.Result: """![](image_placeholder.webp)"""
  def repeat_output(self, repeat_items: Collection | None = None, active_index: Int | None = None, active_item: Pointer | None = None, inspection_index: Int | None = None, geometry: Geometry | None = None, : Virtual | None = None) -> RepeatOutput.Result: """![](image_placeholder.webp)"""
  def replace_material(self, geometry: Geometry | None = None, old: Material | None = None, new: Material | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def replace_string(self, string: String | None = None, find: String | None = None, replace: String | None = None) -> String: """![](image_placeholder.webp)"""
  def reroute(self, socket_idname: String | None = None, input: Color | None = None) -> Color: """![](image_placeholder.webp)"""
  def resample_curve(self, mode: ResampleCurve.Mode | None = None, keep_last_segment: Boolean | None = None, curve: Geometry | None = None, selection: Bool | None = None, count: Int | None = None, length: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def reverse_curve(self, curve: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def rotate_euler(self, rotation_type: RotateEuler.RotationType | None = None, space: RotateEuler.Space | None = None, rotation: VectorEuler | None = None, rotate_by: VectorEuler | None = None, axis: VectorXYZ | None = None, angle: FloatAngle | None = None) -> Vector: """![](image_placeholder.webp)"""
  def rotate_instances(self, instances: Geometry | None = None, selection: Bool | None = None, rotation: Rotation | None = None, pivot_point: VectorTranslation | None = None, local_space: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def rotate_rotation(self, rotation_space: RotateRotation.RotationSpace | None = None, rotation: Rotation | None = None, rotate_by: Rotation | None = None) -> Rotation: """![](image_placeholder.webp)"""
  def rotate_vector(self, vector: Vector | None = None, rotation: Rotation | None = None) -> Vector: """![](image_placeholder.webp)"""
  def rotation(self, rotation_euler: Float | None = None) -> Rotation: """![](image_placeholder.webp)"""
  def rotation_to_axis_angle(self, rotation: Rotation | None = None) -> RotationToAxisAngle.Result: """![](image_placeholder.webp)"""
  def rotation_to_euler(self, rotation: Rotation | None = None) -> VectorEuler: """![](image_placeholder.webp)"""
  def rotation_to_quaternion(self, rotation: Rotation | None = None) -> RotationToQuaternion.Result: """![](image_placeholder.webp)"""
  def sample_curve(self, mode: SampleCurve.Mode | None = None, use_all_curves: Boolean | None = None, data_type: SampleCurve.DataType | None = None, curves: Geometry | None = None, value: Float | None = None, factor: FloatFactor | None = None, length: FloatDistance | None = None, curve_index: Int | None = None) -> SampleCurve.Result: """![](image_placeholder.webp)"""
  def sample_grid(self, data_type: SampleGrid.DataType | None = None, interpolation_mode: SampleGrid.InterpolationMode | None = None, grid: Float | None = None, position: Vector | None = None) -> Float: """![](image_placeholder.webp)"""
  def sample_grid_index(self, data_type: SampleGridIndex.DataType | None = None, grid: Float | None = None, x: Int | None = None, y: Int | None = None, z: Int | None = None) -> Float: """![](image_placeholder.webp)"""
  def sample_index(self, data_type: SampleIndex.DataType | None = None, domain: SampleIndex.Domain | None = None, clamp: Boolean | None = None, geometry: Geometry | None = None, value: Float | None = None, index: Int | None = None) -> Float: """![](image_placeholder.webp)"""
  def sample_nearest(self, domain: SampleNearest.Domain | None = None, geometry: Geometry | None = None, sample_position: Vector | None = None) -> Int: """![](image_placeholder.webp)"""
  def sample_nearest_surface(self, data_type: SampleNearestSurface.DataType | None = None, mesh: Geometry | None = None, value: Float | None = None, group_id: Int | None = None, sample_position: Vector | None = None, sample_group_id: Int | None = None) -> SampleNearestSurface.Result: """![](image_placeholder.webp)"""
  def sample_uv_surface(self, data_type: SampleUvSurface.DataType | None = None, mesh: Geometry | None = None, value: Float | None = None, uv_map: Vector | None = None, sample_uv: Vector | None = None) -> SampleUvSurface.Result: """![](image_placeholder.webp)"""
  def scale_elements(self, domain: ScaleElements.Domain | None = None, scale_mode: ScaleElements.ScaleMode | None = None, geometry: Geometry | None = None, selection: Bool | None = None, scale: Float | None = None, center: VectorTranslation | None = None, axis: Vector | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def scale_instances(self, instances: Geometry | None = None, selection: Bool | None = None, scale: VectorXYZ | None = None, center: VectorTranslation | None = None, local_space: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def scene_time(self, ) -> SceneTime.Result: """![](image_placeholder.webp)"""
  def sdf_grid_boolean(self, operation: SdfGridBoolean.Operation | None = None, grid_1: Float | None = None, grid_2: List[Float] | None = None) -> Float: """![](image_placeholder.webp)"""
  def selection(self, ) -> Selection.Result: """![](image_placeholder.webp)"""
  def self_object(self, ) -> Object: """![](image_placeholder.webp)"""
  def separate_bundle(self, bundle_items: Collection | None = None, active_index: Int | None = None, bundle: Bundle | None = None) -> Virtual: """![](image_placeholder.webp)"""
  def separate_components(self, geometry: Geometry | None = None) -> SeparateComponents.Result: """![](image_placeholder.webp)"""
  def separate_geometry(self, domain: SeparateGeometry.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None) -> SeparateGeometry.Result: """![](image_placeholder.webp)"""
  def separate_matrix(self, matrix: Matrix | None = None) -> SeparateMatrix.Result: """![](image_placeholder.webp)"""
  def separate_rgb_(self, legacy)(image: Color | None = None) -> SeparateRgb(Legacy).Result: """![](image_placeholder.webp)"""
  def separate_transform(self, transform: Matrix | None = None) -> SeparateTransform.Result: """![](image_placeholder.webp)"""
  def separate_xyz(self, vector: Vector | None = None) -> SeparateXyz.Result: """![](image_placeholder.webp)"""
  def set_curve_normal(self, mode: SetCurveNormal.Mode | None = None, curve: Geometry | None = None, selection: Bool | None = None, normal: VectorXYZ | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_curve_radius(self, curve: Geometry | None = None, selection: Bool | None = None, radius: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_curve_tilt(self, curve: Geometry | None = None, selection: Bool | None = None, tilt: FloatAngle | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_face_set(self, mesh: Geometry | None = None, selection: Bool | None = None, face_set: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_geometry_name(self, geometry: Geometry | None = None, name: String | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_grease_pencil_color(self, mode: SetGreasePencilColor.Mode | None = None, grease_pencil: Geometry | None = None, selection: Bool | None = None, color: Color | None = None, opacity: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_grease_pencil_depth(self, depth_order: SetGreasePencilDepth.DepthOrder | None = None, grease_pencil: Geometry | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_grease_pencil_softness(self, grease_pencil: Geometry | None = None, selection: Bool | None = None, softness: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_handle_positions(self, mode: SetHandlePositions.Mode | None = None, curve: Geometry | None = None, selection: Bool | None = None, position: Vector | None = None, offset: VectorTranslation | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_handle_type(self, handle_type: SetHandleType.HandleType | None = None, mode: SetHandleType.Mode | None = None, curve: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_id(self, geometry: Geometry | None = None, selection: Bool | None = None, id: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_instance_transform(self, instances: Geometry | None = None, selection: Bool | None = None, transform: Matrix | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_material(self, geometry: Geometry | None = None, selection: Bool | None = None, material: Material | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_material_index(self, geometry: Geometry | None = None, selection: Bool | None = None, material_index: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_mesh_normal(self, mode: SetMeshNormal.Mode | None = None, domain: SetMeshNormal.Domain | None = None, mesh: Geometry | None = None, remove_custom: Bool | None = None, edge_sharpness: Bool | None = None, face_sharpness: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_point_radius(self, points: Geometry | None = None, selection: Bool | None = None, radius: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_position(self, geometry: Geometry | None = None, selection: Bool | None = None, position: Vector | None = None, offset: VectorTranslation | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_selection(self, domain: SetSelection.Domain | None = None, selection_type: SetSelection.SelectionType | None = None, geometry: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_shade_smooth(self, domain: SetShadeSmooth.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None, shade_smooth: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_spline_cyclic(self, geometry: Geometry | None = None, selection: Bool | None = None, cyclic: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_spline_resolution(self, geometry: Geometry | None = None, selection: Bool | None = None, resolution: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def set_spline_type(self, spline_type: SetSplineType.SplineType | None = None, curve: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def shortest_edge_paths(self, end_vertex: Bool | None = None, edge_cost: Float | None = None) -> ShortestEdgePaths.Result: """![](image_placeholder.webp)"""
  def simulation_input(self, paired_output: Pointer | None = None) -> Float: """![](image_placeholder.webp)"""
  def simulation_output(self, state_items: Collection | None = None, active_index: Int | None = None, active_item: Pointer | None = None, skip: Bool | None = None, geometry: Geometry | None = None, : Virtual | None = None) -> SimulationOutput.Result: """![](image_placeholder.webp)"""
  def slice_string(self, string: String | None = None, position: Int | None = None, length: Int | None = None) -> String: """![](image_placeholder.webp)"""
  def sort_elements(self, domain: SortElements.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None, group_id: Int | None = None, sort_weight: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def special_characters(self, ) -> SpecialCharacters.Result: """![](image_placeholder.webp)"""
  def spiral(self, resolution: IntUnsigned | None = None, rotations: Float | None = None, start_radius: FloatDistance | None = None, end_radius: FloatDistance | None = None, height: FloatDistance | None = None, reverse: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def spline_length(self, ) -> SplineLength.Result: """![](image_placeholder.webp)"""
  def spline_parameter(self, ) -> SplineParameter.Result: """![](image_placeholder.webp)"""
  def spline_resolution(self, ) -> Int: """![](image_placeholder.webp)"""
  def split_edges(self, mesh: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def split_to_instances(self, domain: SplitToInstances.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None, group_id: Int | None = None) -> SplitToInstances.Result: """![](image_placeholder.webp)"""
  def star(self, points: IntUnsigned | None = None, inner_radius: FloatDistance | None = None, outer_radius: FloatDistance | None = None, twist: FloatAngle | None = None) -> Star.Result: """![](image_placeholder.webp)"""
  def store_named_attribute(self, data_type: StoreNamedAttribute.DataType | None = None, domain: StoreNamedAttribute.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None, name: String | None = None, value: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def store_named_grid(self, data_type: StoreNamedGrid.DataType | None = None, volume: Geometry | None = None, name: String | None = None, grid: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def string(self, string: String | None = None) -> String: """![](image_placeholder.webp)"""
  def string_length(self, string: String | None = None) -> Int: """![](image_placeholder.webp)"""
  def string_to_curves(self, font: Pointer | None = None, overflow: StringToCurves.Overflow | None = None, align_x: StringToCurves.AlignX | None = None, align_y: StringToCurves.AlignY | None = None, pivot_mode: StringToCurves.PivotMode | None = None, string: String | None = None, size: FloatDistance | None = None, character_spacing: Float | None = None, word_spacing: Float | None = None, line_spacing: Float | None = None, text_box_width: FloatDistance | None = None, text_box_height: FloatDistance | None = None) -> StringToCurves.Result: """![](image_placeholder.webp)"""
  def subdivide_curve(self, curve: Geometry | None = None, cuts: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def subdivide_mesh(self, mesh: Geometry | None = None, level: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def subdivision_surface(self, uv_smooth: SubdivisionSurface.UvSmooth | None = None, boundary_smooth: SubdivisionSurface.BoundarySmooth | None = None, mesh: Geometry | None = None, level: Int | None = None, edge_crease: FloatFactor | None = None, vertex_crease: FloatFactor | None = None, limit_surface: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def switch(self, input_type: Switch.InputType | None = None, switch: Bool | None = None, false: Geometry | None = None, true: Geometry | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def transform_direction(self, direction: VectorXYZ | None = None, transform: Matrix | None = None) -> VectorXYZ: """![](image_placeholder.webp)"""
  def transform_geometry(self, mode: TransformGeometry.Mode | None = None, geometry: Geometry | None = None, translation: VectorTranslation | None = None, rotation: Rotation | None = None, scale: VectorXYZ | None = None, transform: Matrix | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def transform_gizmo(self, use_translation_x: Boolean | None = None, use_translation_y: Boolean | None = None, use_translation_z: Boolean | None = None, use_rotation_x: Boolean | None = None, use_rotation_y: Boolean | None = None, use_rotation_z: Boolean | None = None, use_scale_x: Boolean | None = None, use_scale_y: Boolean | None = None, use_scale_z: Boolean | None = None, value: List[Matrix] | None = None, position: VectorTranslation | None = None, rotation: Rotation | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def transform_point(self, vector: VectorXYZ | None = None, transform: Matrix | None = None) -> VectorXYZ: """![](image_placeholder.webp)"""
  def translate_instances(self, instances: Geometry | None = None, selection: Bool | None = None, translation: VectorTranslation | None = None, local_space: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def transpose_matrix(self, matrix: Matrix | None = None) -> Matrix: """![](image_placeholder.webp)"""
  def triangulate(self, quad_method: Triangulate.QuadMethod | None = None, ngon_method: Triangulate.NgonMethod | None = None, mesh: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def trim_curve(self, mode: TrimCurve.Mode | None = None, curve: Geometry | None = None, selection: Bool | None = None, start: FloatDistance | None = None, end: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def uv_sphere(self, segments: Int | None = None, rings: Int | None = None, radius: FloatDistance | None = None) -> UvSphere.Result: """![](image_placeholder.webp)"""
  def uv_unwrap(self, method: UvUnwrap.Method | None = None, selection: Bool | None = None, seam: Bool | None = None, margin: Float | None = None, fill_holes: Bool | None = None) -> Vector: """![](image_placeholder.webp)"""
  def value(self, ) -> Float: """![](image_placeholder.webp)"""
  def value_to_string(self, data_type: ValueToString.DataType | None = None, value: Float | None = None, decimals: Int | None = None) -> String: """![](image_placeholder.webp)"""
  def vector(self, vector: Float | None = None) -> Vector: """![](image_placeholder.webp)"""
  def vector_curves(self, mapping: Pointer | None = None, fac: FloatFactor | None = None, vector: Vector | None = None) -> Vector: """![](image_placeholder.webp)"""
  def vector_math(self, operation: VectorMath.Operation | None = None, vector: Vector | None = None, scale: Float | None = None) -> VectorMath.Result: """![](image_placeholder.webp)"""
  def vector_rotate(self, rotation_type: VectorRotate.RotationType | None = None, invert: Boolean | None = None, vector: Vector | None = None, center: Vector | None = None, axis: Vector | None = None, angle: FloatAngle | None = None, rotation: VectorEuler | None = None) -> Vector: """![](image_placeholder.webp)"""
  def vertex_neighbors(self, ) -> VertexNeighbors.Result: """![](image_placeholder.webp)"""
  def vertex_of_corner(self, corner_index: Int | None = None) -> Int: """![](image_placeholder.webp)"""
  def viewer(self, data_type: Viewer.DataType | None = None, domain: Viewer.Domain | None = None, ui_shortcut: Int | None = None, geometry: Geometry | None = None, value: Float | None = None) -> Viewer.Result: """![](image_placeholder.webp)"""
  def viewport_transform(self, ) -> ViewportTransform.Result: """![](image_placeholder.webp)"""
  def volume_cube(self, density: Float | None = None, background: Float | None = None, min: Vector | None = None, max: Vector | None = None, resolution_x: Int | None = None, resolution_y: Int | None = None, resolution_z: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def volume_to_mesh(self, resolution_mode: VolumeToMesh.ResolutionMode | None = None, volume: Geometry | None = None, voxel_size: FloatDistance | None = None, voxel_amount: Float | None = None, threshold: Float | None = None, adaptivity: FloatFactor | None = None) -> Geometry: """![](image_placeholder.webp)"""
  def voronoi_texture(self, texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, voronoi_dimensions: VoronoiTexture.VoronoiDimensions | None = None, distance: VoronoiTexture.Distance | None = None, feature: VoronoiTexture.Feature | None = None, normalize: Boolean | None = None, vector: Vector | None = None, w: Float | None = None, scale: Float | None = None, detail: Float | None = None, roughness: FloatFactor | None = None, lacunarity: Float | None = None, smoothness: FloatFactor | None = None, exponent: Float | None = None, randomness: FloatFactor | None = None) -> VoronoiTexture.Result: """![](image_placeholder.webp)"""
  def warning(self, warning_type: Warning.WarningType | None = None, show: Bool | None = None, message: String | None = None) -> Bool: """![](image_placeholder.webp)"""
  def wave_texture(self, texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, wave_type: WaveTexture.WaveType | None = None, bands_direction: WaveTexture.BandsDirection | None = None, rings_direction: WaveTexture.RingsDirection | None = None, wave_profile: WaveTexture.WaveProfile | None = None, vector: Vector | None = None, scale: Float | None = None, distortion: Float | None = None, detail: Float | None = None, detail_scale: Float | None = None, detail_roughness: FloatFactor | None = None, phase_offset: Float | None = None) -> WaveTexture.Result: """![](image_placeholder.webp)"""
  def white_noise_texture(self, noise_dimensions: WhiteNoiseTexture.NoiseDimensions | None = None, vector: Vector | None = None, w: Float | None = None) -> WhiteNoiseTexture.Result: """![](image_placeholder.webp)"""
  
class Bool(Type): pass
class Bundle(Type): pass
class Closure(Type): pass
class Collection(Type): pass
class Color(Type): pass
class Float(Type): pass
class FloatAngle(Type): pass
class FloatColorTemperature(Type): pass
class FloatDistance(Type): pass
class FloatFactor(Type): pass
class FloatFrequency(Type): pass
class FloatPercentage(Type): pass
class FloatTime(Type): pass
class FloatTimeAbsolute(Type): pass
class FloatUnsigned(Type): pass
class FloatWavelength(Type): pass
class Geometry(Type): pass
class Image(Type): pass
class Int(Type): pass
class IntFactor(Type): pass
class IntPercentage(Type): pass
class IntUnsigned(Type): pass
class Material(Type): pass
class Matrix(Type): pass
class Menu(Type): pass
class Object(Type): pass
class Rotation(Type): pass
class Shader(Type): pass
class Standard(Type): pass
class String(Type): pass
class StringFilePath(Type): pass
class Texture(Type): pass
class Vector(Type): pass
class Vector2D(Type): pass
class Vector4D(Type): pass
class VectorAcceleration(Type): pass
class VectorAcceleration2D(Type): pass
class VectorAcceleration4D(Type): pass
class VectorDirection(Type): pass
class VectorDirection2D(Type): pass
class VectorDirection4D(Type): pass
class VectorEuler(Type): pass
class VectorEuler2D(Type): pass
class VectorEuler4D(Type): pass
class VectorFactor(Type): pass
class VectorFactor2D(Type): pass
class VectorFactor4D(Type): pass
class VectorPercentage(Type): pass
class VectorPercentage2D(Type): pass
class VectorPercentage4D(Type): pass
class VectorTranslation(Type): pass
class VectorTranslation2D(Type): pass
class VectorTranslation4D(Type): pass
class VectorVelocity(Type): pass
class VectorVelocity2D(Type): pass
class VectorVelocity4D(Type): pass
class VectorXYZ(Type): pass
class VectorXYZ2D(Type): pass
class VectorXYZ4D(Type): pass
class Virtual(Type): pass
class 3DCursor:
  class Result:
    location: VectorTranslation
    rotation: Rotation
class AccumulateField:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
    TRANSFORM = 'TRANSFORM'
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CORNER = 'CORNER'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
  class Result:
    leading: Float
    trailing: Float
    total: Float
class ActiveElement:
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    LAYER = 'LAYER'
  class Result:
    index: Int
    exists: Bool
class AlignEulerToVector:
  class Axis(enum.Enum):
    X = 'X'
    Y = 'Y'
    Z = 'Z'
  class PivotAxis(enum.Enum):
    AUTO = 'AUTO'
    X = 'X'
    Y = 'Y'
    Z = 'Z'
class AlignRotationToVector:
  class Axis(enum.Enum):
    X = 'X'
    Y = 'Y'
    Z = 'Z'
  class PivotAxis(enum.Enum):
    AUTO = 'AUTO'
    X = 'X'
    Y = 'Y'
    Z = 'Z'
class Arc:
  class Mode(enum.Enum):
    POINTS = 'POINTS'
    RADIUS = 'RADIUS'
  class Result:
    curve: Geometry
    center: Vector
    normal: Vector
    radius: Float
class AttributeStatistic:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
    FLOAT_COLOR = 'FLOAT_COLOR'
    BYTE_COLOR = 'BYTE_COLOR'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    FLOAT2 = 'FLOAT2'
    INT8 = 'INT8'
    INT16_2D = 'INT16_2D'
    INT32_2D = 'INT32_2D'
    QUATERNION = 'QUATERNION'
    FLOAT4X4 = 'FLOAT4X4'
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CORNER = 'CORNER'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
  class Result:
    mean: Float
    median: Float
    sum: Float
    min: Float
    max: Float
    range: Float
    standard_deviation: Float
    variance: Float
class AxesToRotation:
  class PrimaryAxis(enum.Enum):
    X = 'X'
    Y = 'Y'
    Z = 'Z'
  class SecondaryAxis(enum.Enum):
    X = 'X'
    Y = 'Y'
    Z = 'Z'
class Bake:
  class Result:
    geometry: Geometry
    : Virtual
class BitMath:
  class Operation(enum.Enum):
    AND = 'AND'
    OR = 'OR'
    XOR = 'XOR'
    NOT = 'NOT'
    SHIFT = 'SHIFT'
    ROTATE = 'ROTATE'
class BlurAttribute:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
    FLOAT_COLOR = 'FLOAT_COLOR'
    BYTE_COLOR = 'BYTE_COLOR'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    FLOAT2 = 'FLOAT2'
    INT8 = 'INT8'
    INT16_2D = 'INT16_2D'
    INT32_2D = 'INT32_2D'
    QUATERNION = 'QUATERNION'
    FLOAT4X4 = 'FLOAT4X4'
class BooleanMath:
  class Operation(enum.Enum):
    AND = 'AND'
    OR = 'OR'
    NOT = 'NOT'
    NAND = 'NAND'
    NOR = 'NOR'
    XNOR = 'XNOR'
    XOR = 'XOR'
    IMPLY = 'IMPLY'
    NIMPLY = 'NIMPLY'
class BoundingBox:
  class Result:
    bounding_box: Geometry
    min: Vector
    max: Vector
class BrickTexture:
  class Result:
    color: Color
    fac: Float
class BézierSegment:
  class Mode(enum.Enum):
    POSITION = 'POSITION'
    OFFSET = 'OFFSET'
class CameraInfo:
  class Result:
    projection_matrix: Matrix
    focal_length: Float
    sensor: Vector
    shift: Vector
    clip_start: Float
    clip_end: Float
    focus_distance: Float
    is_orthographic: Bool
    orthographic_scale: Float
class CaptureAttribute:
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CORNER = 'CORNER'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
  class Result:
    geometry: Geometry
    : Virtual
class CheckerTexture:
  class Result:
    color: Color
    fac: Float
class Clamp:
  class ClampType(enum.Enum):
    MINMAX = 'MINMAX'
    RANGE = 'RANGE'
class CollectionInfo:
  class TransformSpace(enum.Enum):
    ORIGINAL = 'ORIGINAL'
    RELATIVE = 'RELATIVE'
class Compare:
  class Operation(enum.Enum):
    LESS_THAN = 'LESS_THAN'
    LESS_EQUAL = 'LESS_EQUAL'
    GREATER_THAN = 'GREATER_THAN'
    GREATER_EQUAL = 'GREATER_EQUAL'
    EQUAL = 'EQUAL'
    NOT_EQUAL = 'NOT_EQUAL'
    BRIGHTER = 'BRIGHTER'
    DARKER = 'DARKER'
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    BOOLEAN = 'BOOLEAN'
    VECTOR = 'VECTOR'
    ROTATION = 'ROTATION'
    MATRIX = 'MATRIX'
    STRING = 'STRING'
    MENU = 'MENU'
    RGBA = 'RGBA'
    OBJECT = 'OBJECT'
    IMAGE = 'IMAGE'
    GEOMETRY = 'GEOMETRY'
    COLLECTION = 'COLLECTION'
    TEXTURE = 'TEXTURE'
    MATERIAL = 'MATERIAL'
    BUNDLE = 'BUNDLE'
    CLOSURE = 'CLOSURE'
  class Mode(enum.Enum):
    ELEMENT = 'ELEMENT'
    LENGTH = 'LENGTH'
    AVERAGE = 'AVERAGE'
    DOT_PRODUCT = 'DOT_PRODUCT'
    DIRECTION = 'DIRECTION'
class Cone:
  class FillType(enum.Enum):
    NONE = 'NONE'
    NGON = 'NGON'
    TRIANGLE_FAN = 'TRIANGLE_FAN'
  class Result:
    mesh: Geometry
    top: Bool
    bottom: Bool
    side: Bool
    uv_map: Vector
class CornersOfEdge:
  class Result:
    corner_index: Int
    total: Int
class CornersOfFace:
  class Result:
    corner_index: Int
    total: Int
class CornersOfVertex:
  class Result:
    corner_index: Int
    total: Int
class Cube:
  class Result:
    mesh: Geometry
    uv_map: Vector
class CurveCircle:
  class Mode(enum.Enum):
    POINTS = 'POINTS'
    RADIUS = 'RADIUS'
  class Result:
    curve: Geometry
    center: Vector
class CurveHandlePositions:
  class Result:
    left: Vector
    right: Vector
class CurveLine:
  class Mode(enum.Enum):
    POINTS = 'POINTS'
    DIRECTION = 'DIRECTION'
class CurveOfPoint:
  class Result:
    curve_index: Int
    index_in_curve: Int
class CurveToPoints:
  class Mode(enum.Enum):
    EVALUATED = 'EVALUATED'
    COUNT = 'COUNT'
    LENGTH = 'LENGTH'
  class Result:
    points: Geometry
    tangent: Vector
    normal: Vector
    rotation: Rotation
class Cylinder:
  class FillType(enum.Enum):
    NONE = 'NONE'
    NGON = 'NGON'
    TRIANGLE_FAN = 'TRIANGLE_FAN'
  class Result:
    mesh: Geometry
    top: Bool
    side: Bool
    bottom: Bool
    uv_map: Vector
class DeleteGeometry:
  class Mode(enum.Enum):
    ALL = 'ALL'
    EDGE_FACE = 'EDGE_FACE'
    ONLY_FACE = 'ONLY_FACE'
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
class DialGizmo:
  class ColorId(enum.Enum):
    PRIMARY = 'PRIMARY'
    SECONDARY = 'SECONDARY'
    X = 'X'
    Y = 'Y'
    Z = 'Z'
class DistributePointsInGrid:
  class Mode(enum.Enum):
    DENSITY_RANDOM = 'DENSITY_RANDOM'
    DENSITY_GRID = 'DENSITY_GRID'
class DistributePointsInVolume:
  class Mode(enum.Enum):
    DENSITY_RANDOM = 'DENSITY_RANDOM'
    DENSITY_GRID = 'DENSITY_GRID'
class DistributePointsOnFaces:
  class DistributeMethod(enum.Enum):
    RANDOM = 'RANDOM'
    POISSON = 'POISSON'
  class Result:
    points: Geometry
    normal: Vector
    rotation: Rotation
class DomainSize:
  class Component(enum.Enum):
    MESH = 'MESH'
    POINTCLOUD = 'POINTCLOUD'
    CURVE = 'CURVE'
    INSTANCES = 'INSTANCES'
    GREASEPENCIL = 'GREASEPENCIL'
  class Result:
    point_count: Int
    edge_count: Int
    face_count: Int
    face_corner_count: Int
    spline_count: Int
    instance_count: Int
    layer_count: Int
class DuplicateElements:
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    SPLINE = 'SPLINE'
    LAYER = 'LAYER'
    INSTANCE = 'INSTANCE'
  class Result:
    geometry: Geometry
    duplicate_index: Int
class EdgeAngle:
  class Result:
    unsigned_angle: Float
    signed_angle: Float
class EdgeVertices:
  class Result:
    vertex_index_1: Int
    vertex_index_2: Int
    position_1: Vector
    position_2: Vector
class EdgesOfCorner:
  class Result:
    next_edge_index: Int
    previous_edge_index: Int
class EdgesOfVertex:
  class Result:
    edge_index: Int
    total: Int
class EvaluateAtIndex:
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CORNER = 'CORNER'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
    FLOAT_COLOR = 'FLOAT_COLOR'
    BYTE_COLOR = 'BYTE_COLOR'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    FLOAT2 = 'FLOAT2'
    INT8 = 'INT8'
    INT16_2D = 'INT16_2D'
    INT32_2D = 'INT32_2D'
    QUATERNION = 'QUATERNION'
    FLOAT4X4 = 'FLOAT4X4'
class EvaluateOnDomain:
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CORNER = 'CORNER'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
    FLOAT_COLOR = 'FLOAT_COLOR'
    BYTE_COLOR = 'BYTE_COLOR'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    FLOAT2 = 'FLOAT2'
    INT8 = 'INT8'
    INT16_2D = 'INT16_2D'
    INT32_2D = 'INT32_2D'
    QUATERNION = 'QUATERNION'
    FLOAT4X4 = 'FLOAT4X4'
class ExtrudeMesh:
  class Mode(enum.Enum):
    VERTICES = 'VERTICES'
    EDGES = 'EDGES'
    FACES = 'FACES'
  class Result:
    mesh: Geometry
    top: Bool
    side: Bool
class FaceNeighbors:
  class Result:
    vertex_count: Int
    face_count: Int
class FaceOfCorner:
  class Result:
    face_index: Int
    index_in_face: Int
class FaceSet:
  class Result:
    face_set: Int
    exists: Bool
class FieldAverage:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CORNER = 'CORNER'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
  class Result:
    mean: Float
    median: Float
class FieldMin&Max:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CORNER = 'CORNER'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
  class Result:
    min: Float
    max: Float
class FieldVariance:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CORNER = 'CORNER'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
  class Result:
    standard_deviation: Float
    variance: Float
class FillCurve:
  class Mode(enum.Enum):
    TRIANGLES = 'TRIANGLES'
    NGONS = 'NGONS'
class FilletCurve:
  class Mode(enum.Enum):
    BEZIER = 'BEZIER'
    POLY = 'POLY'
class FindInString:
  class Result:
    first_found: Int
    count: Int
class FloatToInteger:
  class RoundingMode(enum.Enum):
    ROUND = 'ROUND'
    FLOOR = 'FLOOR'
    CEILING = 'CEILING'
    TRUNCATE = 'TRUNCATE'
class ForEachGeometryElementInput:
  class Result:
    index: Int
    element: Geometry
    : Virtual
class ForEachGeometryElementOutput:
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CORNER = 'CORNER'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
  class Result:
    geometry: Geometry
    : Virtual
class GaborTexture:
  class GaborType(enum.Enum):
    _2D = '2D'
    _3D = '3D'
  class Result:
    value: Float
    phase: Float
    intensity: Float
class GeometryProximity:
  class TargetElement(enum.Enum):
    POINTS = 'POINTS'
    EDGES = 'EDGES'
    FACES = 'FACES'
  class Result:
    position: Vector
    distance: Float
    is_valid: Bool
class GetNamedGrid:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    BOOLEAN = 'BOOLEAN'
    VECTOR = 'VECTOR'
    ROTATION = 'ROTATION'
    MATRIX = 'MATRIX'
    STRING = 'STRING'
    MENU = 'MENU'
    RGBA = 'RGBA'
    OBJECT = 'OBJECT'
    IMAGE = 'IMAGE'
    GEOMETRY = 'GEOMETRY'
    COLLECTION = 'COLLECTION'
    TEXTURE = 'TEXTURE'
    MATERIAL = 'MATERIAL'
    BUNDLE = 'BUNDLE'
    CLOSURE = 'CLOSURE'
  class Result:
    volume: Geometry
    grid: Float
class GradientTexture:
  class GradientType(enum.Enum):
    LINEAR = 'LINEAR'
    QUADRATIC = 'QUADRATIC'
    EASING = 'EASING'
    DIAGONAL = 'DIAGONAL'
    SPHERICAL = 'SPHERICAL'
    QUADRATIC_SPHERE = 'QUADRATIC_SPHERE'
    RADIAL = 'RADIAL'
  class Result:
    color: Color
    fac: Float
class Grid:
  class Result:
    mesh: Geometry
    uv_map: Vector
class GridInfo:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    BOOLEAN = 'BOOLEAN'
    VECTOR = 'VECTOR'
    ROTATION = 'ROTATION'
    MATRIX = 'MATRIX'
    STRING = 'STRING'
    MENU = 'MENU'
    RGBA = 'RGBA'
    OBJECT = 'OBJECT'
    IMAGE = 'IMAGE'
    GEOMETRY = 'GEOMETRY'
    COLLECTION = 'COLLECTION'
    TEXTURE = 'TEXTURE'
    MATERIAL = 'MATERIAL'
    BUNDLE = 'BUNDLE'
    CLOSURE = 'CLOSURE'
  class Result:
    transform: Matrix
    background_value: Float
class HandleTypeSelection:
  class HandleType(enum.Enum):
    FREE = 'FREE'
    AUTO = 'AUTO'
    VECTOR = 'VECTOR'
    ALIGN = 'ALIGN'
  class Mode(enum.Enum):
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
class HashValue:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    BOOLEAN = 'BOOLEAN'
    VECTOR = 'VECTOR'
    ROTATION = 'ROTATION'
    MATRIX = 'MATRIX'
    STRING = 'STRING'
    MENU = 'MENU'
    RGBA = 'RGBA'
    OBJECT = 'OBJECT'
    IMAGE = 'IMAGE'
    GEOMETRY = 'GEOMETRY'
    COLLECTION = 'COLLECTION'
    TEXTURE = 'TEXTURE'
    MATERIAL = 'MATERIAL'
    BUNDLE = 'BUNDLE'
    CLOSURE = 'CLOSURE'
class IcoSphere:
  class Result:
    mesh: Geometry
    uv_map: Vector
class ImageInfo:
  class Result:
    width: Int
    height: Int
    has_alpha: Bool
    frame_count: Int
    fps: Float
class ImageTexture:
  class Interpolation(enum.Enum):
    LINEAR = 'Linear'
    CLOSEST = 'Closest'
    CUBIC = 'Cubic'
  class Extension(enum.Enum):
    REPEAT = 'REPEAT'
    EXTEND = 'EXTEND'
    CLIP = 'CLIP'
    MIRROR = 'MIRROR'
  class Result:
    color: Color
    alpha: Float
class IndexOfNearest:
  class Result:
    index: Int
    has_neighbor: Bool
class IndexSwitch:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    BOOLEAN = 'BOOLEAN'
    VECTOR = 'VECTOR'
    ROTATION = 'ROTATION'
    MATRIX = 'MATRIX'
    STRING = 'STRING'
    MENU = 'MENU'
    RGBA = 'RGBA'
    OBJECT = 'OBJECT'
    IMAGE = 'IMAGE'
    GEOMETRY = 'GEOMETRY'
    COLLECTION = 'COLLECTION'
    TEXTURE = 'TEXTURE'
    MATERIAL = 'MATERIAL'
    BUNDLE = 'BUNDLE'
    CLOSURE = 'CLOSURE'
class InstanceBounds:
  class Result:
    min: Vector
    max: Vector
class IntegerMath:
  class Operation(enum.Enum):
    ADD = 'ADD'
    SUBTRACT = 'SUBTRACT'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    MULTIPLY_ADD = 'MULTIPLY_ADD'
    ABSOLUTE = 'ABSOLUTE'
    NEGATE = 'NEGATE'
    POWER = 'POWER'
    MINIMUM = 'MINIMUM'
    MAXIMUM = 'MAXIMUM'
    SIGN = 'SIGN'
    DIVIDE_ROUND = 'DIVIDE_ROUND'
    DIVIDE_FLOOR = 'DIVIDE_FLOOR'
    DIVIDE_CEIL = 'DIVIDE_CEIL'
    FLOORED_MODULO = 'FLOORED_MODULO'
    MODULO = 'MODULO'
    GCD = 'GCD'
    LCM = 'LCM'
class InterpolateCurves:
  class Result:
    curves: Geometry
    closest_index: Int
    closest_weight: Float
class InvertMatrix:
  class Result:
    matrix: Matrix
    invertible: Bool
class LinearGizmo:
  class ColorId(enum.Enum):
    PRIMARY = 'PRIMARY'
    SECONDARY = 'SECONDARY'
    X = 'X'
    Y = 'Y'
    Z = 'Z'
  class DrawStyle(enum.Enum):
    ARROW = 'ARROW'
    CROSS = 'CROSS'
    BOX = 'BOX'
class MagicTexture:
  class Result:
    color: Color
    fac: Float
class MapRange:
  class InterpolationType(enum.Enum):
    LINEAR = 'LINEAR'
    STEPPED = 'STEPPED'
    SMOOTHSTEP = 'SMOOTHSTEP'
    SMOOTHERSTEP = 'SMOOTHERSTEP'
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
  class Result:
    result: Float
    vector: Vector
class MatchString:
  class Operation(enum.Enum):
    STARTS_WITH = 'STARTS_WITH'
    ENDS_WITH = 'ENDS_WITH'
    CONTAINS = 'CONTAINS'
class Math:
  class Operation(enum.Enum):
    ADD = 'ADD'
    SUBTRACT = 'SUBTRACT'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    MULTIPLY_ADD = 'MULTIPLY_ADD'
    POWER = 'POWER'
    LOGARITHM = 'LOGARITHM'
    SQRT = 'SQRT'
    INVERSE_SQRT = 'INVERSE_SQRT'
    ABSOLUTE = 'ABSOLUTE'
    EXPONENT = 'EXPONENT'
    MINIMUM = 'MINIMUM'
    MAXIMUM = 'MAXIMUM'
    LESS_THAN = 'LESS_THAN'
    GREATER_THAN = 'GREATER_THAN'
    SIGN = 'SIGN'
    COMPARE = 'COMPARE'
    SMOOTH_MIN = 'SMOOTH_MIN'
    SMOOTH_MAX = 'SMOOTH_MAX'
    ROUND = 'ROUND'
    FLOOR = 'FLOOR'
    CEIL = 'CEIL'
    TRUNC = 'TRUNC'
    FRACT = 'FRACT'
    MODULO = 'MODULO'
    FLOORED_MODULO = 'FLOORED_MODULO'
    WRAP = 'WRAP'
    SNAP = 'SNAP'
    PINGPONG = 'PINGPONG'
    SINE = 'SINE'
    COSINE = 'COSINE'
    TANGENT = 'TANGENT'
    ARCSINE = 'ARCSINE'
    ARCCOSINE = 'ARCCOSINE'
    ARCTANGENT = 'ARCTANGENT'
    ARCTAN2 = 'ARCTAN2'
    SINH = 'SINH'
    COSH = 'COSH'
    TANH = 'TANH'
    RADIANS = 'RADIANS'
    DEGREES = 'DEGREES'
class MenuSwitch:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    BOOLEAN = 'BOOLEAN'
    VECTOR = 'VECTOR'
    ROTATION = 'ROTATION'
    MATRIX = 'MATRIX'
    STRING = 'STRING'
    MENU = 'MENU'
    RGBA = 'RGBA'
    OBJECT = 'OBJECT'
    IMAGE = 'IMAGE'
    GEOMETRY = 'GEOMETRY'
    COLLECTION = 'COLLECTION'
    TEXTURE = 'TEXTURE'
    MATERIAL = 'MATERIAL'
    BUNDLE = 'BUNDLE'
    CLOSURE = 'CLOSURE'
class MergeByDistance:
  class Mode(enum.Enum):
    ALL = 'ALL'
    CONNECTED = 'CONNECTED'
class MergeLayers:
  class Mode(enum.Enum):
    MERGE_BY_NAME = 'MERGE_BY_NAME'
    MERGE_BY_ID = 'MERGE_BY_ID'
class MeshBoolean:
  class Operation(enum.Enum):
    INTERSECT = 'INTERSECT'
    UNION = 'UNION'
    DIFFERENCE = 'DIFFERENCE'
  class Solver(enum.Enum):
    EXACT = 'EXACT'
    FLOAT = 'FLOAT'
    MANIFOLD = 'MANIFOLD'
  class Result:
    mesh: Geometry
    intersecting_edges: Bool
class MeshCircle:
  class FillType(enum.Enum):
    NONE = 'NONE'
    NGON = 'NGON'
    TRIANGLE_FAN = 'TRIANGLE_FAN'
class MeshIsland:
  class Result:
    island_index: Int
    island_count: Int
class MeshLine:
  class Mode(enum.Enum):
    OFFSET = 'OFFSET'
    END_POINTS = 'END_POINTS'
  class CountMode(enum.Enum):
    TOTAL = 'TOTAL'
    RESOLUTION = 'RESOLUTION'
class MeshToCurve:
  class Mode(enum.Enum):
    EDGES = 'EDGES'
    FACES = 'FACES'
class MeshToPoints:
  class Mode(enum.Enum):
    VERTICES = 'VERTICES'
    EDGES = 'EDGES'
    FACES = 'FACES'
    CORNERS = 'CORNERS'
class MeshToVolume:
  class ResolutionMode(enum.Enum):
    VOXEL_AMOUNT = 'VOXEL_AMOUNT'
    VOXEL_SIZE = 'VOXEL_SIZE'
class Mix(Legacy):
  class BlendType(enum.Enum):
    MIX = 'MIX'
    DARKEN = 'DARKEN'
    MULTIPLY = 'MULTIPLY'
    BURN = 'BURN'
    LIGHTEN = 'LIGHTEN'
    SCREEN = 'SCREEN'
    DODGE = 'DODGE'
    ADD = 'ADD'
    OVERLAY = 'OVERLAY'
    SOFT_LIGHT = 'SOFT_LIGHT'
    LINEAR_LIGHT = 'LINEAR_LIGHT'
    DIFFERENCE = 'DIFFERENCE'
    EXCLUSION = 'EXCLUSION'
    SUBTRACT = 'SUBTRACT'
    DIVIDE = 'DIVIDE'
    HUE = 'HUE'
    SATURATION = 'SATURATION'
    COLOR = 'COLOR'
    VALUE = 'VALUE'
class MousePosition:
  class Result:
    mouse_x: Int
    mouse_y: Int
    region_width: Int
    region_height: Int
class NamedAttribute:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
    FLOAT_COLOR = 'FLOAT_COLOR'
    BYTE_COLOR = 'BYTE_COLOR'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    FLOAT2 = 'FLOAT2'
    INT8 = 'INT8'
    INT16_2D = 'INT16_2D'
    INT32_2D = 'INT32_2D'
    QUATERNION = 'QUATERNION'
    FLOAT4X4 = 'FLOAT4X4'
  class Result:
    attribute: Float
    exists: Bool
class NoiseTexture:
  class NoiseDimensions(enum.Enum):
    _1D = '1D'
    _2D = '2D'
    _3D = '3D'
    _4D = '4D'
  class NoiseType(enum.Enum):
    MULTIFRACTAL = 'MULTIFRACTAL'
    RIDGED_MULTIFRACTAL = 'RIDGED_MULTIFRACTAL'
    HYBRID_MULTIFRACTAL = 'HYBRID_MULTIFRACTAL'
    FBM = 'FBM'
    HETERO_TERRAIN = 'HETERO_TERRAIN'
  class Result:
    fac: Float
    color: Color
class Normal:
  class Result:
    normal: Vector
    true_normal: Vector
class ObjectInfo:
  class TransformSpace(enum.Enum):
    ORIGINAL = 'ORIGINAL'
    RELATIVE = 'RELATIVE'
  class Result:
    transform: Matrix
    location: Vector
    rotation: Rotation
    scale: Vector
    geometry: Geometry
class OffsetPointInCurve:
  class Result:
    is_valid_offset: Bool
    point_index: Int
class PointsOfCurve:
  class Result:
    point_index: Int
    total: Int
class PointsToVolume:
  class ResolutionMode(enum.Enum):
    VOXEL_AMOUNT = 'VOXEL_AMOUNT'
    VOXEL_SIZE = 'VOXEL_SIZE'
class Quadrilateral:
  class Mode(enum.Enum):
    RECTANGLE = 'RECTANGLE'
    PARALLELOGRAM = 'PARALLELOGRAM'
    TRAPEZOID = 'TRAPEZOID'
    KITE = 'KITE'
    POINTS = 'POINTS'
class RandomValue:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
    FLOAT_COLOR = 'FLOAT_COLOR'
    BYTE_COLOR = 'BYTE_COLOR'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    FLOAT2 = 'FLOAT2'
    INT8 = 'INT8'
    INT16_2D = 'INT16_2D'
    INT32_2D = 'INT32_2D'
    QUATERNION = 'QUATERNION'
    FLOAT4X4 = 'FLOAT4X4'
class Raycast:
  class Mapping(enum.Enum):
    INTERPOLATED = 'INTERPOLATED'
    NEAREST = 'NEAREST'
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
    FLOAT_COLOR = 'FLOAT_COLOR'
    BYTE_COLOR = 'BYTE_COLOR'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    FLOAT2 = 'FLOAT2'
    INT8 = 'INT8'
    INT16_2D = 'INT16_2D'
    INT32_2D = 'INT32_2D'
    QUATERNION = 'QUATERNION'
    FLOAT4X4 = 'FLOAT4X4'
  class Result:
    is_hit: Bool
    hit_position: Vector
    hit_normal: Vector
    hit_distance: Float
    attribute: Float
class RemoveNamedAttribute:
  class PatternMode(enum.Enum):
    EXACT = 'EXACT'
    WILDCARD = 'WILDCARD'
class RepeatInput:
  class Result:
    iteration: Int
    : Virtual
class RepeatOutput:
  class Result:
    geometry: Geometry
    : Virtual
class ResampleCurve:
  class Mode(enum.Enum):
    EVALUATED = 'EVALUATED'
    COUNT = 'COUNT'
    LENGTH = 'LENGTH'
class RotateEuler:
  class RotationType(enum.Enum):
    AXIS_ANGLE = 'AXIS_ANGLE'
    EULER = 'EULER'
  class Space(enum.Enum):
    OBJECT = 'OBJECT'
    LOCAL = 'LOCAL'
class RotateRotation:
  class RotationSpace(enum.Enum):
    GLOBAL = 'GLOBAL'
    LOCAL = 'LOCAL'
class RotationToAxisAngle:
  class Result:
    axis: Vector
    angle: FloatAngle
class RotationToQuaternion:
  class Result:
    w: Float
    x: Float
    y: Float
    z: Float
class SampleCurve:
  class Mode(enum.Enum):
    FACTOR = 'FACTOR'
    LENGTH = 'LENGTH'
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
    FLOAT_COLOR = 'FLOAT_COLOR'
    BYTE_COLOR = 'BYTE_COLOR'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    FLOAT2 = 'FLOAT2'
    INT8 = 'INT8'
    INT16_2D = 'INT16_2D'
    INT32_2D = 'INT32_2D'
    QUATERNION = 'QUATERNION'
    FLOAT4X4 = 'FLOAT4X4'
  class Result:
    value: Float
    position: Vector
    tangent: Vector
    normal: Vector
class SampleGrid:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    BOOLEAN = 'BOOLEAN'
    VECTOR = 'VECTOR'
    ROTATION = 'ROTATION'
    MATRIX = 'MATRIX'
    STRING = 'STRING'
    MENU = 'MENU'
    RGBA = 'RGBA'
    OBJECT = 'OBJECT'
    IMAGE = 'IMAGE'
    GEOMETRY = 'GEOMETRY'
    COLLECTION = 'COLLECTION'
    TEXTURE = 'TEXTURE'
    MATERIAL = 'MATERIAL'
    BUNDLE = 'BUNDLE'
    CLOSURE = 'CLOSURE'
  class InterpolationMode(enum.Enum):
    NEAREST = 'NEAREST'
    TRILINEAR = 'TRILINEAR'
    TRIQUADRATIC = 'TRIQUADRATIC'
class SampleGridIndex:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    BOOLEAN = 'BOOLEAN'
    VECTOR = 'VECTOR'
    ROTATION = 'ROTATION'
    MATRIX = 'MATRIX'
    STRING = 'STRING'
    MENU = 'MENU'
    RGBA = 'RGBA'
    OBJECT = 'OBJECT'
    IMAGE = 'IMAGE'
    GEOMETRY = 'GEOMETRY'
    COLLECTION = 'COLLECTION'
    TEXTURE = 'TEXTURE'
    MATERIAL = 'MATERIAL'
    BUNDLE = 'BUNDLE'
    CLOSURE = 'CLOSURE'
class SampleIndex:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
    FLOAT_COLOR = 'FLOAT_COLOR'
    BYTE_COLOR = 'BYTE_COLOR'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    FLOAT2 = 'FLOAT2'
    INT8 = 'INT8'
    INT16_2D = 'INT16_2D'
    INT32_2D = 'INT32_2D'
    QUATERNION = 'QUATERNION'
    FLOAT4X4 = 'FLOAT4X4'
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CORNER = 'CORNER'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
class SampleNearest:
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CORNER = 'CORNER'
class SampleNearestSurface:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
    FLOAT_COLOR = 'FLOAT_COLOR'
    BYTE_COLOR = 'BYTE_COLOR'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    FLOAT2 = 'FLOAT2'
    INT8 = 'INT8'
    INT16_2D = 'INT16_2D'
    INT32_2D = 'INT32_2D'
    QUATERNION = 'QUATERNION'
    FLOAT4X4 = 'FLOAT4X4'
  class Result:
    value: Float
    is_valid: Bool
class SampleUvSurface:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
    FLOAT_COLOR = 'FLOAT_COLOR'
    BYTE_COLOR = 'BYTE_COLOR'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    FLOAT2 = 'FLOAT2'
    INT8 = 'INT8'
    INT16_2D = 'INT16_2D'
    INT32_2D = 'INT32_2D'
    QUATERNION = 'QUATERNION'
    FLOAT4X4 = 'FLOAT4X4'
  class Result:
    value: Float
    is_valid: Bool
class ScaleElements:
  class Domain(enum.Enum):
    FACE = 'FACE'
    EDGE = 'EDGE'
  class ScaleMode(enum.Enum):
    UNIFORM = 'UNIFORM'
    SINGLE_AXIS = 'SINGLE_AXIS'
class SceneTime:
  class Result:
    seconds: Float
    frame: Float
class SdfGridBoolean:
  class Operation(enum.Enum):
    INTERSECT = 'INTERSECT'
    UNION = 'UNION'
    DIFFERENCE = 'DIFFERENCE'
class Selection:
  class Result:
    boolean: Bool
    float: Float
class SeparateComponents:
  class Result:
    mesh: Geometry
    curve: Geometry
    grease_pencil: Geometry
    point_cloud: Geometry
    volume: Geometry
    instances: Geometry
class SeparateGeometry:
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
  class Result:
    selection: Geometry
    inverted: Geometry
class SeparateMatrix:
  class Result:
    column_1_row_1: Float
    column_1_row_2: Float
    column_1_row_3: Float
    column_1_row_4: Float
    column_2_row_1: Float
    column_2_row_2: Float
    column_2_row_3: Float
    column_2_row_4: Float
    column_3_row_1: Float
    column_3_row_2: Float
    column_3_row_3: Float
    column_3_row_4: Float
    column_4_row_1: Float
    column_4_row_2: Float
    column_4_row_3: Float
    column_4_row_4: Float
class SeparateRgb(Legacy):
  class Result:
    r: Float
    g: Float
    b: Float
class SeparateTransform:
  class Result:
    translation: VectorTranslation
    rotation: Rotation
    scale: VectorXYZ
class SeparateXyz:
  class Result:
    x: Float
    y: Float
    z: Float
class SetCurveNormal:
  class Mode(enum.Enum):
    MINIMUM_TWIST = 'MINIMUM_TWIST'
    Z_UP = 'Z_UP'
    FREE = 'FREE'
class SetGreasePencilColor:
  class Mode(enum.Enum):
    STROKE = 'STROKE'
    FILL = 'FILL'
class SetGreasePencilDepth:
  class DepthOrder(enum.Enum):
    _2D = '2D'
    _3D = '3D'
class SetHandlePositions:
  class Mode(enum.Enum):
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
class SetHandleType:
  class HandleType(enum.Enum):
    FREE = 'FREE'
    AUTO = 'AUTO'
    VECTOR = 'VECTOR'
    ALIGN = 'ALIGN'
  class Mode(enum.Enum):
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
class SetMeshNormal:
  class Mode(enum.Enum):
    SHARPNESS = 'SHARPNESS'
    FREE = 'FREE'
    TANGENT_SPACE = 'TANGENT_SPACE'
  class Domain(enum.Enum):
    POINT = 'POINT'
    FACE = 'FACE'
    CORNER = 'CORNER'
class SetSelection:
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CURVE = 'CURVE'
  class SelectionType(enum.Enum):
    BOOLEAN = 'BOOLEAN'
    FLOAT = 'FLOAT'
class SetShadeSmooth:
  class Domain(enum.Enum):
    EDGE = 'EDGE'
    FACE = 'FACE'
class SetSplineType:
  class SplineType(enum.Enum):
    CATMULL_ROM = 'CATMULL_ROM'
    POLY = 'POLY'
    BEZIER = 'BEZIER'
    NURBS = 'NURBS'
class ShortestEdgePaths:
  class Result:
    next_vertex_index: Int
    total_cost: Float
class SimulationOutput:
  class Result:
    geometry: Geometry
    : Virtual
class SortElements:
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
class SpecialCharacters:
  class Result:
    line_break: String
    tab: String
class SplineLength:
  class Result:
    length: Float
    point_count: Int
class SplineParameter:
  class Result:
    factor: Float
    length: Float
    index: Int
class SplitToInstances:
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
  class Result:
    instances: Geometry
    group_id: Int
class Star:
  class Result:
    curve: Geometry
    outer_points: Bool
class StoreNamedAttribute:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
    FLOAT_COLOR = 'FLOAT_COLOR'
    BYTE_COLOR = 'BYTE_COLOR'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    FLOAT2 = 'FLOAT2'
    INT8 = 'INT8'
    INT16_2D = 'INT16_2D'
    INT32_2D = 'INT32_2D'
    QUATERNION = 'QUATERNION'
    FLOAT4X4 = 'FLOAT4X4'
  class Domain(enum.Enum):
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CORNER = 'CORNER'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
class StoreNamedGrid:
  class DataType(enum.Enum):
    BOOLEAN = 'BOOLEAN'
    FLOAT = 'FLOAT'
    DOUBLE = 'DOUBLE'
    INT = 'INT'
    INT64 = 'INT64'
    MASK = 'MASK'
    VECTOR_FLOAT = 'VECTOR_FLOAT'
    VECTOR_DOUBLE = 'VECTOR_DOUBLE'
    VECTOR_INT = 'VECTOR_INT'
    POINTS = 'POINTS'
    UNKNOWN = 'UNKNOWN'
class StringToCurves:
  class Overflow(enum.Enum):
    OVERFLOW = 'OVERFLOW'
    SCALE_TO_FIT = 'SCALE_TO_FIT'
    TRUNCATE = 'TRUNCATE'
  class AlignX(enum.Enum):
    LEFT = 'LEFT'
    CENTER = 'CENTER'
    RIGHT = 'RIGHT'
    JUSTIFY = 'JUSTIFY'
    FLUSH = 'FLUSH'
  class AlignY(enum.Enum):
    TOP = 'TOP'
    TOP_BASELINE = 'TOP_BASELINE'
    MIDDLE = 'MIDDLE'
    BOTTOM_BASELINE = 'BOTTOM_BASELINE'
    BOTTOM = 'BOTTOM'
  class PivotMode(enum.Enum):
    MIDPOINT = 'MIDPOINT'
    TOP_LEFT = 'TOP_LEFT'
    TOP_CENTER = 'TOP_CENTER'
    TOP_RIGHT = 'TOP_RIGHT'
    BOTTOM_LEFT = 'BOTTOM_LEFT'
    BOTTOM_CENTER = 'BOTTOM_CENTER'
    BOTTOM_RIGHT = 'BOTTOM_RIGHT'
  class Result:
    curve_instances: Geometry
    remainder: String
    line: Int
    pivot_point: Vector
class SubdivisionSurface:
  class UvSmooth(enum.Enum):
    NONE = 'NONE'
    PRESERVE_CORNERS = 'PRESERVE_CORNERS'
    PRESERVE_CORNERS_AND_JUNCTIONS = 'PRESERVE_CORNERS_AND_JUNCTIONS'
    PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE = 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE'
    PRESERVE_BOUNDARIES = 'PRESERVE_BOUNDARIES'
    SMOOTH_ALL = 'SMOOTH_ALL'
  class BoundarySmooth(enum.Enum):
    PRESERVE_CORNERS = 'PRESERVE_CORNERS'
    ALL = 'ALL'
class Switch:
  class InputType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    BOOLEAN = 'BOOLEAN'
    VECTOR = 'VECTOR'
    ROTATION = 'ROTATION'
    MATRIX = 'MATRIX'
    STRING = 'STRING'
    MENU = 'MENU'
    RGBA = 'RGBA'
    OBJECT = 'OBJECT'
    IMAGE = 'IMAGE'
    GEOMETRY = 'GEOMETRY'
    COLLECTION = 'COLLECTION'
    TEXTURE = 'TEXTURE'
    MATERIAL = 'MATERIAL'
    BUNDLE = 'BUNDLE'
    CLOSURE = 'CLOSURE'
class TransformGeometry:
  class Mode(enum.Enum):
    COMPONENTS = 'COMPONENTS'
    MATRIX = 'MATRIX'
class Triangulate:
  class QuadMethod(enum.Enum):
    BEAUTY = 'BEAUTY'
    FIXED = 'FIXED'
    FIXED_ALTERNATE = 'FIXED_ALTERNATE'
    SHORTEST_DIAGONAL = 'SHORTEST_DIAGONAL'
    LONGEST_DIAGONAL = 'LONGEST_DIAGONAL'
  class NgonMethod(enum.Enum):
    BEAUTY = 'BEAUTY'
    CLIP = 'CLIP'
class TrimCurve:
  class Mode(enum.Enum):
    FACTOR = 'FACTOR'
    LENGTH = 'LENGTH'
class UvSphere:
  class Result:
    mesh: Geometry
    uv_map: Vector
class UvUnwrap:
  class Method(enum.Enum):
    ANGLE_BASED = 'ANGLE_BASED'
    CONFORMAL = 'CONFORMAL'
class ValueToString:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
class VectorMath:
  class Operation(enum.Enum):
    ADD = 'ADD'
    SUBTRACT = 'SUBTRACT'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    MULTIPLY_ADD = 'MULTIPLY_ADD'
    CROSS_PRODUCT = 'CROSS_PRODUCT'
    PROJECT = 'PROJECT'
    REFLECT = 'REFLECT'
    REFRACT = 'REFRACT'
    FACEFORWARD = 'FACEFORWARD'
    DOT_PRODUCT = 'DOT_PRODUCT'
    DISTANCE = 'DISTANCE'
    LENGTH = 'LENGTH'
    SCALE = 'SCALE'
    NORMALIZE = 'NORMALIZE'
    ABSOLUTE = 'ABSOLUTE'
    POWER = 'POWER'
    SIGN = 'SIGN'
    MINIMUM = 'MINIMUM'
    MAXIMUM = 'MAXIMUM'
    FLOOR = 'FLOOR'
    CEIL = 'CEIL'
    FRACTION = 'FRACTION'
    MODULO = 'MODULO'
    WRAP = 'WRAP'
    SNAP = 'SNAP'
    SINE = 'SINE'
    COSINE = 'COSINE'
    TANGENT = 'TANGENT'
  class Result:
    vector: Vector
    value: Float
class VectorRotate:
  class RotationType(enum.Enum):
    AXIS_ANGLE = 'AXIS_ANGLE'
    X_AXIS = 'X_AXIS'
    Y_AXIS = 'Y_AXIS'
    Z_AXIS = 'Z_AXIS'
    EULER_XYZ = 'EULER_XYZ'
class VertexNeighbors:
  class Result:
    vertex_count: Int
    face_count: Int
class Viewer:
  class DataType(enum.Enum):
    FLOAT = 'FLOAT'
    INT = 'INT'
    FLOAT_VECTOR = 'FLOAT_VECTOR'
    FLOAT_COLOR = 'FLOAT_COLOR'
    BYTE_COLOR = 'BYTE_COLOR'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    FLOAT2 = 'FLOAT2'
    INT8 = 'INT8'
    INT16_2D = 'INT16_2D'
    INT32_2D = 'INT32_2D'
    QUATERNION = 'QUATERNION'
    FLOAT4X4 = 'FLOAT4X4'
  class Domain(enum.Enum):
    AUTO = 'AUTO'
    POINT = 'POINT'
    EDGE = 'EDGE'
    FACE = 'FACE'
    CORNER = 'CORNER'
    CURVE = 'CURVE'
    INSTANCE = 'INSTANCE'
    LAYER = 'LAYER'
class ViewportTransform:
  class Result:
    projection: Matrix
    view: Matrix
    is_orthographic: Bool
class VolumeToMesh:
  class ResolutionMode(enum.Enum):
    GRID = 'GRID'
    VOXEL_AMOUNT = 'VOXEL_AMOUNT'
    VOXEL_SIZE = 'VOXEL_SIZE'
class VoronoiTexture:
  class VoronoiDimensions(enum.Enum):
    _1D = '1D'
    _2D = '2D'
    _3D = '3D'
    _4D = '4D'
  class Distance(enum.Enum):
    EUCLIDEAN = 'EUCLIDEAN'
    MANHATTAN = 'MANHATTAN'
    CHEBYCHEV = 'CHEBYCHEV'
    MINKOWSKI = 'MINKOWSKI'
  class Feature(enum.Enum):
    F1 = 'F1'
    F2 = 'F2'
    SMOOTH_F1 = 'SMOOTH_F1'
    DISTANCE_TO_EDGE = 'DISTANCE_TO_EDGE'
    N_SPHERE_RADIUS = 'N_SPHERE_RADIUS'
  class Result:
    distance: Float
    color: Color
    position: Vector
    w: Float
    radius: Float
class Warning:
  class WarningType(enum.Enum):
    ERROR = 'ERROR'
    WARNING = 'WARNING'
    INFO = 'INFO'
class WaveTexture:
  class WaveType(enum.Enum):
    BANDS = 'BANDS'
    RINGS = 'RINGS'
  class BandsDirection(enum.Enum):
    X = 'X'
    Y = 'Y'
    Z = 'Z'
    DIAGONAL = 'DIAGONAL'
  class RingsDirection(enum.Enum):
    X = 'X'
    Y = 'Y'
    Z = 'Z'
    SPHERICAL = 'SPHERICAL'
  class WaveProfile(enum.Enum):
    SIN = 'SIN'
    SAW = 'SAW'
    TRI = 'TRI'
  class Result:
    color: Color
    fac: Float
class WhiteNoiseTexture:
  class NoiseDimensions(enum.Enum):
    _1D = '1D'
    _2D = '2D'
    _3D = '3D'
    _4D = '4D'
  class Result:
    value: Float
    color: Color
def 3d_cursor() -> 3DCursor.Result: """![](image_placeholder.webp)"""
def accumulate_field(data_type: AccumulateField.DataType | None = None, domain: AccumulateField.Domain | None = None, value: Float | None = None, group_id: Int | None = None) -> AccumulateField.Result: """![](image_placeholder.webp)"""
def active_camera() -> Object: """![](image_placeholder.webp)"""
def active_element(domain: ActiveElement.Domain | None = None) -> ActiveElement.Result: """![](image_placeholder.webp)"""
def align_euler_to_vector(axis: AlignEulerToVector.Axis | None = None, pivot_axis: AlignEulerToVector.PivotAxis | None = None, rotation: VectorEuler | None = None, factor: FloatFactor | None = None, vector: Vector | None = None) -> VectorEuler: """![](image_placeholder.webp)"""
def align_rotation_to_vector(axis: AlignRotationToVector.Axis | None = None, pivot_axis: AlignRotationToVector.PivotAxis | None = None, rotation: Rotation | None = None, factor: FloatFactor | None = None, vector: VectorXYZ | None = None) -> Rotation: """![](image_placeholder.webp)"""
def arc(mode: Arc.Mode | None = None, resolution: IntUnsigned | None = None, start: VectorTranslation | None = None, middle: VectorTranslation | None = None, end: VectorTranslation | None = None, radius: FloatDistance | None = None, start_angle: FloatAngle | None = None, sweep_angle: FloatAngle | None = None, offset_angle: FloatAngle | None = None, connect_center: Bool | None = None, invert_arc: Bool | None = None) -> Arc.Result: """![](image_placeholder.webp)"""
def attribute_statistic(data_type: AttributeStatistic.DataType | None = None, domain: AttributeStatistic.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None, attribute: Float | None = None) -> AttributeStatistic.Result: """![](image_placeholder.webp)"""
def axes_to_rotation(primary_axis: AxesToRotation.PrimaryAxis | Vector | None = None, secondary_axis: AxesToRotation.SecondaryAxis | Vector | None = None) -> Rotation: """![](image_placeholder.webp)"""
def axis_angle_to_rotation(axis: Vector | None = None, angle: FloatAngle | None = None) -> Rotation: """![](image_placeholder.webp)"""
def bake(bake_items: Collection | None = None, active_index: Int | None = None, active_item: Pointer | None = None, geometry: Geometry | None = None, : Virtual | None = None) -> Bake.Result: """![](image_placeholder.webp)"""
def bit_math(operation: BitMath.Operation | None = None, a: Int | None = None, b: Int | None = None, shift: Int | None = None) -> Int: """![](image_placeholder.webp)"""
def blackbody(temperature: FloatColorTemperature | None = None) -> Color: """![](image_placeholder.webp)"""
def blur_attribute(data_type: BlurAttribute.DataType | None = None, value: Float | None = None, iterations: Int | None = None, weight: FloatFactor | None = None) -> Float: """![](image_placeholder.webp)"""
def boolean(boolean: Boolean | None = None) -> Bool: """![](image_placeholder.webp)"""
def boolean_math(operation: BooleanMath.Operation | None = None, boolean: Bool | None = None) -> Bool: """![](image_placeholder.webp)"""
def bounding_box(geometry: Geometry | None = None, use_radius: Bool | None = None) -> BoundingBox.Result: """![](image_placeholder.webp)"""
def brick_texture(texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, offset_frequency: Int | None = None, squash_frequency: Int | None = None, offset: Float | None = None, squash: Float | None = None, vector: Vector | None = None, color1: Color | None = None, color2: Color | None = None, mortar: Color | None = None, scale: Float | None = None, mortar_size: Float | None = None, mortar_smooth: Float | None = None, bias: Float | None = None, brick_width: Float | None = None, row_height: Float | None = None) -> BrickTexture.Result: """![](image_placeholder.webp)"""
def bézier_segment(mode: BézierSegment.Mode | None = None, resolution: IntUnsigned | None = None, start: VectorTranslation | None = None, start_handle: VectorTranslation | None = None, end_handle: VectorTranslation | None = None, end: VectorTranslation | None = None) -> Geometry: """![](image_placeholder.webp)"""
def camera_info(camera: Object | None = None) -> CameraInfo.Result: """![](image_placeholder.webp)"""
def capture_attribute(capture_items: Collection | None = None, active_index: Int | None = None, active_item: Pointer | None = None, domain: CaptureAttribute.Domain | None = None, geometry: Geometry | None = None, : Virtual | None = None) -> CaptureAttribute.Result: """![](image_placeholder.webp)"""
def checker_texture(texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, vector: Vector | None = None, color1: Color | None = None, color2: Color | None = None, scale: Float | None = None) -> CheckerTexture.Result: """![](image_placeholder.webp)"""
def clamp(clamp_type: Clamp.ClampType | None = None, value: Float | None = None, min: Float | None = None, max: Float | None = None) -> Float: """![](image_placeholder.webp)"""
def closure_input(paired_output: Pointer | None = None) -> Virtual: """![](image_placeholder.webp)"""
def closure_output(input_items: Collection | None = None, output_items: Collection | None = None, active_input_index: Int | None = None, active_output_index: Int | None = None, : Virtual | None = None) -> Closure: """![](image_placeholder.webp)"""
def collection(collection: Pointer | None = None) -> Collection: """![](image_placeholder.webp)"""
def collection_info(transform_space: CollectionInfo.TransformSpace | None = None, collection: Collection | None = None, separate_children: Bool | None = None, reset_children: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def color(value: Float | None = None) -> Color: """![](image_placeholder.webp)"""
def combine_bundle(bundle_items: Collection | None = None, active_index: Int | None = None, : Virtual | None = None) -> Bundle: """![](image_placeholder.webp)"""
def combine_matrix(column_1_row_1: Float | None = None, column_1_row_2: Float | None = None, column_1_row_3: Float | None = None, column_1_row_4: Float | None = None, column_2_row_1: Float | None = None, column_2_row_2: Float | None = None, column_2_row_3: Float | None = None, column_2_row_4: Float | None = None, column_3_row_1: Float | None = None, column_3_row_2: Float | None = None, column_3_row_3: Float | None = None, column_3_row_4: Float | None = None, column_4_row_1: Float | None = None, column_4_row_2: Float | None = None, column_4_row_3: Float | None = None, column_4_row_4: Float | None = None) -> Matrix: """![](image_placeholder.webp)"""
def combine_rgb_(legacy)(r: Float | None = None, g: Float | None = None, b: Float | None = None) -> Color: """![](image_placeholder.webp)"""
def combine_transform(translation: VectorTranslation | None = None, rotation: Rotation | None = None, scale: VectorXYZ | None = None) -> Matrix: """![](image_placeholder.webp)"""
def combine_xyz(x: Float | None = None, y: Float | None = None, z: Float | None = None) -> Vector: """![](image_placeholder.webp)"""
def compare(operation: Compare.Operation | None = None, data_type: Compare.DataType | None = None, mode: Compare.Mode | None = None, a: String | None = None, b: String | None = None, c: Float | None = None, angle: FloatAngle | None = None, epsilon: Float | None = None) -> Bool: """![](image_placeholder.webp)"""
def cone(fill_type: Cone.FillType | None = None, vertices: Int | None = None, side_segments: Int | None = None, fill_segments: Int | None = None, radius_top: FloatDistance | None = None, radius_bottom: FloatDistance | None = None, depth: FloatDistance | None = None) -> Cone.Result: """![](image_placeholder.webp)"""
def convex_hull(geometry: Geometry | None = None) -> Geometry: """![](image_placeholder.webp)"""
def corners_of_edge(edge_index: Int | None = None, weights: Float | None = None, sort_index: Int | None = None) -> CornersOfEdge.Result: """![](image_placeholder.webp)"""
def corners_of_face(face_index: Int | None = None, weights: Float | None = None, sort_index: Int | None = None) -> CornersOfFace.Result: """![](image_placeholder.webp)"""
def corners_of_vertex(vertex_index: Int | None = None, weights: Float | None = None, sort_index: Int | None = None) -> CornersOfVertex.Result: """![](image_placeholder.webp)"""
def cube(size: VectorTranslation | None = None, vertices_x: Int | None = None, vertices_y: Int | None = None, vertices_z: Int | None = None) -> Cube.Result: """![](image_placeholder.webp)"""
def curve_circle(mode: CurveCircle.Mode | None = None, resolution: Int | None = None, point_1: VectorTranslation | None = None, point_2: VectorTranslation | None = None, point_3: VectorTranslation | None = None, radius: FloatDistance | None = None) -> CurveCircle.Result: """![](image_placeholder.webp)"""
def curve_handle_positions(relative: Bool | None = None) -> CurveHandlePositions.Result: """![](image_placeholder.webp)"""
def curve_length(curve: Geometry | None = None) -> Float: """![](image_placeholder.webp)"""
def curve_line(mode: CurveLine.Mode | None = None, start: VectorTranslation | None = None, end: VectorTranslation | None = None, direction: Vector | None = None, length: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
def curve_of_point(point_index: Int | None = None) -> CurveOfPoint.Result: """![](image_placeholder.webp)"""
def curve_tangent() -> Vector: """![](image_placeholder.webp)"""
def curve_tilt() -> Float: """![](image_placeholder.webp)"""
def curve_to_mesh(curve: Geometry | None = None, profile_curve: Geometry | None = None, scale: Float | None = None, fill_caps: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def curve_to_points(mode: CurveToPoints.Mode | None = None, curve: Geometry | None = None, count: Int | None = None, length: FloatDistance | None = None) -> CurveToPoints.Result: """![](image_placeholder.webp)"""
def curves_to_grease_pencil(curves: Geometry | None = None, selection: Bool | None = None, instances_as_layers: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def cylinder(fill_type: Cylinder.FillType | None = None, vertices: Int | None = None, side_segments: Int | None = None, fill_segments: Int | None = None, radius: FloatDistance | None = None, depth: FloatDistance | None = None) -> Cylinder.Result: """![](image_placeholder.webp)"""
def deform_curves_on_surface(curves: Geometry | None = None) -> Geometry: """![](image_placeholder.webp)"""
def delete_geometry(mode: DeleteGeometry.Mode | None = None, domain: DeleteGeometry.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def dial_gizmo(color_id: DialGizmo.ColorId | None = None, value: List[Float] | None = None, position: VectorTranslation | None = None, up: VectorXYZ | None = None, screen_space: Bool | None = None, radius: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
def distribute_points_in_grid(mode: DistributePointsInGrid.Mode | None = None, grid: Float | None = None, density: Float | None = None, seed: Int | None = None, spacing: VectorXYZ | None = None, threshold: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
def distribute_points_in_volume(mode: DistributePointsInVolume.Mode | None = None, volume: Geometry | None = None, density: Float | None = None, seed: Int | None = None, spacing: VectorXYZ | None = None, threshold: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
def distribute_points_on_faces(distribute_method: DistributePointsOnFaces.DistributeMethod | None = None, use_legacy_normal: Boolean | None = None, mesh: Geometry | None = None, selection: Bool | None = None, distance_min: FloatDistance | None = None, density_max: Float | None = None, density: Float | None = None, density_factor: FloatFactor | None = None, seed: Int | None = None) -> DistributePointsOnFaces.Result: """![](image_placeholder.webp)"""
def domain_size(component: DomainSize.Component | None = None, geometry: Geometry | None = None) -> DomainSize.Result: """![](image_placeholder.webp)"""
def dual_mesh(mesh: Geometry | None = None, keep_boundaries: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def duplicate_elements(domain: DuplicateElements.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None, amount: Int | None = None) -> DuplicateElements.Result: """![](image_placeholder.webp)"""
def edge_angle() -> EdgeAngle.Result: """![](image_placeholder.webp)"""
def edge_neighbors() -> Int: """![](image_placeholder.webp)"""
def edge_paths_to_curves(mesh: Geometry | None = None, start_vertices: Bool | None = None, next_vertex_index: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
def edge_paths_to_selection(start_vertices: Bool | None = None, next_vertex_index: Int | None = None) -> Bool: """![](image_placeholder.webp)"""
def edge_vertices() -> EdgeVertices.Result: """![](image_placeholder.webp)"""
def edges_of_corner(corner_index: Int | None = None) -> EdgesOfCorner.Result: """![](image_placeholder.webp)"""
def edges_of_vertex(vertex_index: Int | None = None, weights: Float | None = None, sort_index: Int | None = None) -> EdgesOfVertex.Result: """![](image_placeholder.webp)"""
def edges_to_face_groups(boundary_edges: Bool | None = None) -> Int: """![](image_placeholder.webp)"""
def endpoint_selection(start_size: Int | None = None, end_size: Int | None = None) -> Bool: """![](image_placeholder.webp)"""
def euler_to_rotation(euler: VectorEuler | None = None) -> Rotation: """![](image_placeholder.webp)"""
def evaluate_at_index(domain: EvaluateAtIndex.Domain | None = None, data_type: EvaluateAtIndex.DataType | None = None, value: Float | None = None, index: Int | None = None) -> Float: """![](image_placeholder.webp)"""
def evaluate_closure(input_items: Collection | None = None, output_items: Collection | None = None, active_input_index: Int | None = None, active_output_index: Int | None = None, closure: Closure | None = None, : Virtual | None = None) -> Virtual: """![](image_placeholder.webp)"""
def evaluate_on_domain(domain: EvaluateOnDomain.Domain | None = None, data_type: EvaluateOnDomain.DataType | None = None, value: Float | None = None) -> Float: """![](image_placeholder.webp)"""
def extrude_mesh(mode: ExtrudeMesh.Mode | None = None, mesh: Geometry | None = None, selection: Bool | None = None, offset: VectorTranslation | None = None, offset_scale: Float | None = None, individual: Bool | None = None) -> ExtrudeMesh.Result: """![](image_placeholder.webp)"""
def face_area() -> Float: """![](image_placeholder.webp)"""
def face_group_boundaries(face_group_id: Int | None = None) -> Bool: """![](image_placeholder.webp)"""
def face_neighbors() -> FaceNeighbors.Result: """![](image_placeholder.webp)"""
def face_of_corner(corner_index: Int | None = None) -> FaceOfCorner.Result: """![](image_placeholder.webp)"""
def face_set() -> FaceSet.Result: """![](image_placeholder.webp)"""
def field_average(data_type: FieldAverage.DataType | None = None, domain: FieldAverage.Domain | None = None, value: Float | None = None, group_id: Int | None = None) -> FieldAverage.Result: """![](image_placeholder.webp)"""
def field_min_&_max(data_type: FieldMin&Max.DataType | None = None, domain: FieldMin&Max.Domain | None = None, value: Float | None = None, group_id: Int | None = None) -> FieldMin&Max.Result: """![](image_placeholder.webp)"""
def field_variance(data_type: FieldVariance.DataType | None = None, domain: FieldVariance.Domain | None = None, value: Float | None = None, group_id: Int | None = None) -> FieldVariance.Result: """![](image_placeholder.webp)"""
def fill_curve(mode: FillCurve.Mode | None = None, curve: Geometry | None = None, group_id: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
def fillet_curve(mode: FilletCurve.Mode | None = None, curve: Geometry | None = None, count: Int | None = None, radius: FloatDistance | None = None, limit_radius: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def find_in_string(string: String | None = None, search: String | None = None) -> FindInString.Result: """![](image_placeholder.webp)"""
def flip_faces(mesh: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def float_curve(mapping: Pointer | None = None, factor: FloatFactor | None = None, value: Float | None = None) -> Float: """![](image_placeholder.webp)"""
def float_to_integer(rounding_mode: FloatToInteger.RoundingMode | None = None, float: Float | None = None) -> Int: """![](image_placeholder.webp)"""
def for_each_geometry_element_input(paired_output: Pointer | None = None, geometry: Geometry | None = None, selection: Bool | None = None, : Virtual | None = None) -> ForEachGeometryElementInput.Result: """![](image_placeholder.webp)"""
def for_each_geometry_element_output(input_items: Collection | None = None, main_items: Collection | None = None, generation_items: Collection | None = None, active_input_index: Int | None = None, active_generation_index: Int | None = None, active_main_index: Int | None = None, domain: ForEachGeometryElementOutput.Domain | None = None, inspection_index: Int | None = None, : Virtual | None = None, geometry: Geometry | None = None) -> ForEachGeometryElementOutput.Result: """![](image_placeholder.webp)"""
def format_string(format_items: Collection | None = None, active_index: Int | None = None, format: String | None = None, : Virtual | None = None) -> String: """![](image_placeholder.webp)"""
def frame(text: Pointer | None = None, shrink: Boolean | None = None, label_size: Int | None = None) -> Frame.Result: """![](image_placeholder.webp)"""
def gabor_texture(texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, gabor_type: GaborTexture.GaborType | None = None, vector: Vector | None = None, scale: Float | None = None, frequency: Float | None = None, anisotropy: FloatFactor | None = None, orientation: VectorDirection | None = None) -> GaborTexture.Result: """![](image_placeholder.webp)"""
def geometry_proximity(target_element: GeometryProximity.TargetElement | None = None, geometry: Geometry | None = None, group_id: Int | None = None, sample_position: Vector | None = None, sample_group_id: Int | None = None) -> GeometryProximity.Result: """![](image_placeholder.webp)"""
def geometry_to_instance(geometry: List[Geometry] | None = None) -> Geometry: """![](image_placeholder.webp)"""
def get_named_grid(data_type: GetNamedGrid.DataType | None = None, volume: Geometry | None = None, name: String | None = None, remove: Bool | None = None) -> GetNamedGrid.Result: """![](image_placeholder.webp)"""
def gradient_texture(texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, gradient_type: GradientTexture.GradientType | None = None, vector: Vector | None = None) -> GradientTexture.Result: """![](image_placeholder.webp)"""
def grease_pencil_to_curves(grease_pencil: Geometry | None = None, selection: Bool | None = None, layers_as_instances: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def grid(size_x: FloatDistance | None = None, size_y: FloatDistance | None = None, vertices_x: Int | None = None, vertices_y: Int | None = None) -> Grid.Result: """![](image_placeholder.webp)"""
def grid_info(data_type: GridInfo.DataType | None = None, grid: Float | None = None) -> GridInfo.Result: """![](image_placeholder.webp)"""
def grid_to_mesh(grid: Float | None = None, threshold: Float | None = None, adaptivity: FloatFactor | None = None) -> Geometry: """![](image_placeholder.webp)"""
def group(node_tree: Pointer | None = None) -> Group.Result: """![](image_placeholder.webp)"""
def group_input() -> Virtual: """![](image_placeholder.webp)"""
def group_output(is_active_output: Boolean | None = None, : Virtual | None = None) -> GroupOutput.Result: """![](image_placeholder.webp)"""
def handle_type_selection(handle_type: HandleTypeSelection.HandleType | None = None, mode: HandleTypeSelection.Mode | None = None) -> Bool: """![](image_placeholder.webp)"""
def hash_value(data_type: HashValue.DataType | None = None, value: Int | None = None, seed: Int | None = None) -> Int: """![](image_placeholder.webp)"""
def ico_sphere(radius: FloatDistance | None = None, subdivisions: Int | None = None) -> IcoSphere.Result: """![](image_placeholder.webp)"""
def id() -> Int: """![](image_placeholder.webp)"""
def image(image: Pointer | None = None) -> Image: """![](image_placeholder.webp)"""
def image_info(image: Image | None = None, frame: Int | None = None) -> ImageInfo.Result: """![](image_placeholder.webp)"""
def image_texture(interpolation: ImageTexture.Interpolation | None = None, extension: ImageTexture.Extension | None = None, image: Image | None = None, vector: Vector | None = None, frame: Int | None = None) -> ImageTexture.Result: """![](image_placeholder.webp)"""
def import_csv(path: StringFilePath | None = None, delimiter: String | None = None) -> Geometry: """![](image_placeholder.webp)"""
def import_obj(path: StringFilePath | None = None) -> Geometry: """![](image_placeholder.webp)"""
def import_ply(path: StringFilePath | None = None) -> Geometry: """![](image_placeholder.webp)"""
def import_stl(path: StringFilePath | None = None) -> Geometry: """![](image_placeholder.webp)"""
def import_text(path: StringFilePath | None = None) -> String: """![](image_placeholder.webp)"""
def import_vdb(path: StringFilePath | None = None) -> Geometry: """![](image_placeholder.webp)"""
def index() -> Int: """![](image_placeholder.webp)"""
def index_of_nearest(position: Vector | None = None, group_id: Int | None = None) -> IndexOfNearest.Result: """![](image_placeholder.webp)"""
def index_switch(index_switch_items: Collection | None = None, data_type: IndexSwitch.DataType | None = None, index: Int | None = None, 0: Geometry | None = None, 1: Geometry | None = None, : Virtual | None = None) -> Geometry: """![](image_placeholder.webp)"""
def instance_bounds(use_radius: Bool | None = None) -> InstanceBounds.Result: """![](image_placeholder.webp)"""
def instance_on_points(points: Geometry | None = None, selection: Bool | None = None, instance: Geometry | None = None, pick_instance: Bool | None = None, instance_index: Int | None = None, rotation: Rotation | None = None, scale: VectorXYZ | None = None) -> Geometry: """![](image_placeholder.webp)"""
def instance_rotation() -> Rotation: """![](image_placeholder.webp)"""
def instance_scale() -> Vector: """![](image_placeholder.webp)"""
def instance_transform() -> Matrix: """![](image_placeholder.webp)"""
def instances_to_points(instances: Geometry | None = None, selection: Bool | None = None, position: Vector | None = None, radius: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
def integer(integer: Int | None = None) -> Int: """![](image_placeholder.webp)"""
def integer_math(operation: IntegerMath.Operation | None = None, value: Int | None = None) -> Int: """![](image_placeholder.webp)"""
def interpolate_curves(guide_curves: Geometry | None = None, guide_up: Vector | None = None, guide_group_id: Int | None = None, points: Geometry | None = None, point_up: Vector | None = None, point_group_id: Int | None = None, max_neighbors: Int | None = None) -> InterpolateCurves.Result: """![](image_placeholder.webp)"""
def invert_matrix(matrix: Matrix | None = None) -> InvertMatrix.Result: """![](image_placeholder.webp)"""
def invert_rotation(rotation: Rotation | None = None) -> Rotation: """![](image_placeholder.webp)"""
def is_edge_smooth() -> Bool: """![](image_placeholder.webp)"""
def is_face_planar(threshold: FloatDistance | None = None) -> Bool: """![](image_placeholder.webp)"""
def is_face_smooth() -> Bool: """![](image_placeholder.webp)"""
def is_spline_cyclic() -> Bool: """![](image_placeholder.webp)"""
def is_viewport() -> Bool: """![](image_placeholder.webp)"""
def join_geometry(geometry: List[Geometry] | None = None) -> Geometry: """![](image_placeholder.webp)"""
def join_strings(delimiter: String | None = None, strings: List[String] | None = None) -> String: """![](image_placeholder.webp)"""
def linear_gizmo(color_id: LinearGizmo.ColorId | None = None, draw_style: LinearGizmo.DrawStyle | None = None, value: List[Float] | None = None, position: VectorTranslation | None = None, direction: VectorXYZ | None = None) -> Geometry: """![](image_placeholder.webp)"""
def magic_texture(texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, turbulence_depth: Int | None = None, vector: Vector | None = None, scale: Float | None = None, distortion: Float | None = None) -> MagicTexture.Result: """![](image_placeholder.webp)"""
def map_range(clamp: Boolean | None = None, interpolation_type: MapRange.InterpolationType | None = None, data_type: MapRange.DataType | None = None, value: Float | None = None, from_min: Vector | None = None, from_max: Vector | None = None, to_min: Vector | None = None, to_max: Vector | None = None, steps: Vector | None = None, vector: Vector | None = None) -> MapRange.Result: """![](image_placeholder.webp)"""
def match_string(operation: MatchString.Operation | None = None, string: String | None = None, key: String | None = None) -> Bool: """![](image_placeholder.webp)"""
def material(material: Pointer | None = None) -> Material: """![](image_placeholder.webp)"""
def material_index() -> Int: """![](image_placeholder.webp)"""
def material_selection(material: Material | None = None) -> Bool: """![](image_placeholder.webp)"""
def math(operation: Math.Operation | None = None, use_clamp: Boolean | None = None, value: Float | None = None) -> Float: """![](image_placeholder.webp)"""
def matrix_determinant(matrix: Matrix | None = None) -> Float: """![](image_placeholder.webp)"""
def menu_switch(enum_items: Collection | None = None, active_index: Int | None = None, active_item: Pointer | None = None, enum_definition: Pointer | None = None, data_type: MenuSwitch.DataType | None = None, menu: Menu | None = None, a: Geometry | None = None, b: Geometry | None = None, : Virtual | None = None) -> Geometry: """![](image_placeholder.webp)"""
def merge_by_distance(mode: MergeByDistance.Mode | None = None, geometry: Geometry | None = None, selection: Bool | None = None, distance: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
def merge_layers(mode: MergeLayers.Mode | None = None, grease_pencil: Geometry | None = None, selection: Bool | None = None, group_id: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
def mesh_boolean(operation: MeshBoolean.Operation | None = None, solver: MeshBoolean.Solver | None = None, mesh_1: Geometry | None = None, mesh_2: List[Geometry] | None = None, self_intersection: Bool | None = None, hole_tolerant: Bool | None = None) -> MeshBoolean.Result: """![](image_placeholder.webp)"""
def mesh_circle(fill_type: MeshCircle.FillType | None = None, vertices: Int | None = None, radius: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
def mesh_island() -> MeshIsland.Result: """![](image_placeholder.webp)"""
def mesh_line(mode: MeshLine.Mode | None = None, count_mode: MeshLine.CountMode | None = None, count: Int | None = None, resolution: FloatDistance | None = None, start_location: VectorTranslation | None = None, offset: VectorTranslation | None = None) -> Geometry: """![](image_placeholder.webp)"""
def mesh_to_curve(mode: MeshToCurve.Mode | None = None, mesh: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def mesh_to_density_grid(mesh: Geometry | None = None, density: Float | None = None, voxel_size: FloatDistance | None = None, gradient_width: FloatDistance | None = None) -> Float: """![](image_placeholder.webp)"""
def mesh_to_points(mode: MeshToPoints.Mode | None = None, mesh: Geometry | None = None, selection: Bool | None = None, position: Vector | None = None, radius: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
def mesh_to_sdf_grid(mesh: Geometry | None = None, voxel_size: FloatDistance | None = None, band_width: Int | None = None) -> Float: """![](image_placeholder.webp)"""
def mesh_to_volume(resolution_mode: MeshToVolume.ResolutionMode | None = None, mesh: Geometry | None = None, density: Float | None = None, voxel_size: FloatDistance | None = None, voxel_amount: Float | None = None, interior_band_width: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
def mix_(legacy)(blend_type: Mix(Legacy).BlendType | None = None, use_alpha: Boolean | None = None, use_clamp: Boolean | None = None, fac: FloatFactor | None = None, color1: Color | None = None, color2: Color | None = None) -> Color: """![](image_placeholder.webp)"""
def mouse_position() -> MousePosition.Result: """![](image_placeholder.webp)"""
def multiply_matrices(matrix: Matrix | None = None) -> Matrix: """![](image_placeholder.webp)"""
def named_attribute(data_type: NamedAttribute.DataType | None = None, name: String | None = None) -> NamedAttribute.Result: """![](image_placeholder.webp)"""
def named_layer_selection(name: String | None = None) -> Bool: """![](image_placeholder.webp)"""
def noise_texture(texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, noise_dimensions: NoiseTexture.NoiseDimensions | None = None, noise_type: NoiseTexture.NoiseType | None = None, normalize: Boolean | None = None, vector: Vector | None = None, w: Float | None = None, scale: Float | None = None, detail: Float | None = None, roughness: FloatFactor | None = None, lacunarity: Float | None = None, offset: Float | None = None, gain: Float | None = None, distortion: Float | None = None) -> NoiseTexture.Result: """![](image_placeholder.webp)"""
def normal(legacy_corner_normals: Boolean | None = None) -> Normal.Result: """![](image_placeholder.webp)"""
def object(object: Pointer | None = None) -> Object: """![](image_placeholder.webp)"""
def object_info(transform_space: ObjectInfo.TransformSpace | None = None, object: Object | None = None, as_instance: Bool | None = None) -> ObjectInfo.Result: """![](image_placeholder.webp)"""
def offset_corner_in_face(corner_index: Int | None = None, offset: Int | None = None) -> Int: """![](image_placeholder.webp)"""
def offset_point_in_curve(point_index: Int | None = None, offset: Int | None = None) -> OffsetPointInCurve.Result: """![](image_placeholder.webp)"""
def pack_uv_islands(uv: Vector | None = None, selection: Bool | None = None, margin: Float | None = None, rotate: Bool | None = None) -> Vector: """![](image_placeholder.webp)"""
def points(count: Int | None = None, position: VectorTranslation | None = None, radius: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
def points_of_curve(curve_index: Int | None = None, weights: Float | None = None, sort_index: Int | None = None) -> PointsOfCurve.Result: """![](image_placeholder.webp)"""
def points_to_curves(points: Geometry | None = None, curve_group_id: Int | None = None, weight: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
def points_to_sdf_grid(points: Geometry | None = None, radius: FloatDistance | None = None, voxel_size: FloatDistance | None = None) -> Float: """![](image_placeholder.webp)"""
def points_to_vertices(points: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def points_to_volume(resolution_mode: PointsToVolume.ResolutionMode | None = None, points: Geometry | None = None, density: Float | None = None, voxel_size: FloatDistance | None = None, voxel_amount: Float | None = None, radius: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
def position() -> Vector: """![](image_placeholder.webp)"""
def project_point(vector: VectorXYZ | None = None, transform: Matrix | None = None) -> VectorXYZ: """![](image_placeholder.webp)"""
def quadratic_bézier(resolution: IntUnsigned | None = None, start: VectorTranslation | None = None, middle: VectorTranslation | None = None, end: VectorTranslation | None = None) -> Geometry: """![](image_placeholder.webp)"""
def quadrilateral(mode: Quadrilateral.Mode | None = None, width: FloatDistance | None = None, height: FloatDistance | None = None, bottom_width: FloatDistance | None = None, top_width: FloatDistance | None = None, offset: FloatDistance | None = None, bottom_height: FloatDistance | None = None, top_height: FloatDistance | None = None, point_1: VectorTranslation | None = None, point_2: VectorTranslation | None = None, point_3: VectorTranslation | None = None, point_4: VectorTranslation | None = None) -> Geometry: """![](image_placeholder.webp)"""
def quaternion_to_rotation(w: Float | None = None, x: Float | None = None, y: Float | None = None, z: Float | None = None) -> Rotation: """![](image_placeholder.webp)"""
def radius() -> Float: """![](image_placeholder.webp)"""
def random_value(data_type: RandomValue.DataType | None = None, min: Int | None = None, max: Int | None = None, probability: FloatFactor | None = None, id: Int | None = None, seed: Int | None = None) -> Bool: """![](image_placeholder.webp)"""
def raycast(mapping: Raycast.Mapping | None = None, data_type: Raycast.DataType | None = None, target_geometry: Geometry | None = None, attribute: Float | None = None, source_position: Vector | None = None, ray_direction: Vector | None = None, ray_length: FloatDistance | None = None) -> Raycast.Result: """![](image_placeholder.webp)"""
def realize_instances(geometry: Geometry | None = None, selection: Bool | None = None, realize_all: Bool | None = None, depth: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
def remove_named_attribute(pattern_mode: RemoveNamedAttribute.PatternMode | None = None, geometry: Geometry | None = None, name: String | None = None) -> Geometry: """![](image_placeholder.webp)"""
def repeat_input(paired_output: Pointer | None = None, iterations: Int | None = None, : Virtual | None = None) -> RepeatInput.Result: """![](image_placeholder.webp)"""
def repeat_output(repeat_items: Collection | None = None, active_index: Int | None = None, active_item: Pointer | None = None, inspection_index: Int | None = None, geometry: Geometry | None = None, : Virtual | None = None) -> RepeatOutput.Result: """![](image_placeholder.webp)"""
def replace_material(geometry: Geometry | None = None, old: Material | None = None, new: Material | None = None) -> Geometry: """![](image_placeholder.webp)"""
def replace_string(string: String | None = None, find: String | None = None, replace: String | None = None) -> String: """![](image_placeholder.webp)"""
def reroute(socket_idname: String | None = None, input: Color | None = None) -> Color: """![](image_placeholder.webp)"""
def resample_curve(mode: ResampleCurve.Mode | None = None, keep_last_segment: Boolean | None = None, curve: Geometry | None = None, selection: Bool | None = None, count: Int | None = None, length: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
def reverse_curve(curve: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def rotate_euler(rotation_type: RotateEuler.RotationType | None = None, space: RotateEuler.Space | None = None, rotation: VectorEuler | None = None, rotate_by: VectorEuler | None = None, axis: VectorXYZ | None = None, angle: FloatAngle | None = None) -> Vector: """![](image_placeholder.webp)"""
def rotate_instances(instances: Geometry | None = None, selection: Bool | None = None, rotation: Rotation | None = None, pivot_point: VectorTranslation | None = None, local_space: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def rotate_rotation(rotation_space: RotateRotation.RotationSpace | None = None, rotation: Rotation | None = None, rotate_by: Rotation | None = None) -> Rotation: """![](image_placeholder.webp)"""
def rotate_vector(vector: Vector | None = None, rotation: Rotation | None = None) -> Vector: """![](image_placeholder.webp)"""
def rotation(rotation_euler: Float | None = None) -> Rotation: """![](image_placeholder.webp)"""
def rotation_to_axis_angle(rotation: Rotation | None = None) -> RotationToAxisAngle.Result: """![](image_placeholder.webp)"""
def rotation_to_euler(rotation: Rotation | None = None) -> VectorEuler: """![](image_placeholder.webp)"""
def rotation_to_quaternion(rotation: Rotation | None = None) -> RotationToQuaternion.Result: """![](image_placeholder.webp)"""
def sample_curve(mode: SampleCurve.Mode | None = None, use_all_curves: Boolean | None = None, data_type: SampleCurve.DataType | None = None, curves: Geometry | None = None, value: Float | None = None, factor: FloatFactor | None = None, length: FloatDistance | None = None, curve_index: Int | None = None) -> SampleCurve.Result: """![](image_placeholder.webp)"""
def sample_grid(data_type: SampleGrid.DataType | None = None, interpolation_mode: SampleGrid.InterpolationMode | None = None, grid: Float | None = None, position: Vector | None = None) -> Float: """![](image_placeholder.webp)"""
def sample_grid_index(data_type: SampleGridIndex.DataType | None = None, grid: Float | None = None, x: Int | None = None, y: Int | None = None, z: Int | None = None) -> Float: """![](image_placeholder.webp)"""
def sample_index(data_type: SampleIndex.DataType | None = None, domain: SampleIndex.Domain | None = None, clamp: Boolean | None = None, geometry: Geometry | None = None, value: Float | None = None, index: Int | None = None) -> Float: """![](image_placeholder.webp)"""
def sample_nearest(domain: SampleNearest.Domain | None = None, geometry: Geometry | None = None, sample_position: Vector | None = None) -> Int: """![](image_placeholder.webp)"""
def sample_nearest_surface(data_type: SampleNearestSurface.DataType | None = None, mesh: Geometry | None = None, value: Float | None = None, group_id: Int | None = None, sample_position: Vector | None = None, sample_group_id: Int | None = None) -> SampleNearestSurface.Result: """![](image_placeholder.webp)"""
def sample_uv_surface(data_type: SampleUvSurface.DataType | None = None, mesh: Geometry | None = None, value: Float | None = None, uv_map: Vector | None = None, sample_uv: Vector | None = None) -> SampleUvSurface.Result: """![](image_placeholder.webp)"""
def scale_elements(domain: ScaleElements.Domain | None = None, scale_mode: ScaleElements.ScaleMode | None = None, geometry: Geometry | None = None, selection: Bool | None = None, scale: Float | None = None, center: VectorTranslation | None = None, axis: Vector | None = None) -> Geometry: """![](image_placeholder.webp)"""
def scale_instances(instances: Geometry | None = None, selection: Bool | None = None, scale: VectorXYZ | None = None, center: VectorTranslation | None = None, local_space: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def scene_time() -> SceneTime.Result: """![](image_placeholder.webp)"""
def sdf_grid_boolean(operation: SdfGridBoolean.Operation | None = None, grid_1: Float | None = None, grid_2: List[Float] | None = None) -> Float: """![](image_placeholder.webp)"""
def selection() -> Selection.Result: """![](image_placeholder.webp)"""
def self_object() -> Object: """![](image_placeholder.webp)"""
def separate_bundle(bundle_items: Collection | None = None, active_index: Int | None = None, bundle: Bundle | None = None) -> Virtual: """![](image_placeholder.webp)"""
def separate_components(geometry: Geometry | None = None) -> SeparateComponents.Result: """![](image_placeholder.webp)"""
def separate_geometry(domain: SeparateGeometry.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None) -> SeparateGeometry.Result: """![](image_placeholder.webp)"""
def separate_matrix(matrix: Matrix | None = None) -> SeparateMatrix.Result: """![](image_placeholder.webp)"""
def separate_rgb_(legacy)(image: Color | None = None) -> SeparateRgb(Legacy).Result: """![](image_placeholder.webp)"""
def separate_transform(transform: Matrix | None = None) -> SeparateTransform.Result: """![](image_placeholder.webp)"""
def separate_xyz(vector: Vector | None = None) -> SeparateXyz.Result: """![](image_placeholder.webp)"""
def set_curve_normal(mode: SetCurveNormal.Mode | None = None, curve: Geometry | None = None, selection: Bool | None = None, normal: VectorXYZ | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_curve_radius(curve: Geometry | None = None, selection: Bool | None = None, radius: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_curve_tilt(curve: Geometry | None = None, selection: Bool | None = None, tilt: FloatAngle | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_face_set(mesh: Geometry | None = None, selection: Bool | None = None, face_set: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_geometry_name(geometry: Geometry | None = None, name: String | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_grease_pencil_color(mode: SetGreasePencilColor.Mode | None = None, grease_pencil: Geometry | None = None, selection: Bool | None = None, color: Color | None = None, opacity: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_grease_pencil_depth(depth_order: SetGreasePencilDepth.DepthOrder | None = None, grease_pencil: Geometry | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_grease_pencil_softness(grease_pencil: Geometry | None = None, selection: Bool | None = None, softness: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_handle_positions(mode: SetHandlePositions.Mode | None = None, curve: Geometry | None = None, selection: Bool | None = None, position: Vector | None = None, offset: VectorTranslation | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_handle_type(handle_type: SetHandleType.HandleType | None = None, mode: SetHandleType.Mode | None = None, curve: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_id(geometry: Geometry | None = None, selection: Bool | None = None, id: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_instance_transform(instances: Geometry | None = None, selection: Bool | None = None, transform: Matrix | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_material(geometry: Geometry | None = None, selection: Bool | None = None, material: Material | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_material_index(geometry: Geometry | None = None, selection: Bool | None = None, material_index: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_mesh_normal(mode: SetMeshNormal.Mode | None = None, domain: SetMeshNormal.Domain | None = None, mesh: Geometry | None = None, remove_custom: Bool | None = None, edge_sharpness: Bool | None = None, face_sharpness: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_point_radius(points: Geometry | None = None, selection: Bool | None = None, radius: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_position(geometry: Geometry | None = None, selection: Bool | None = None, position: Vector | None = None, offset: VectorTranslation | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_selection(domain: SetSelection.Domain | None = None, selection_type: SetSelection.SelectionType | None = None, geometry: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_shade_smooth(domain: SetShadeSmooth.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None, shade_smooth: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_spline_cyclic(geometry: Geometry | None = None, selection: Bool | None = None, cyclic: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_spline_resolution(geometry: Geometry | None = None, selection: Bool | None = None, resolution: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
def set_spline_type(spline_type: SetSplineType.SplineType | None = None, curve: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def shortest_edge_paths(end_vertex: Bool | None = None, edge_cost: Float | None = None) -> ShortestEdgePaths.Result: """![](image_placeholder.webp)"""
def simulation_input(paired_output: Pointer | None = None) -> Float: """![](image_placeholder.webp)"""
def simulation_output(state_items: Collection | None = None, active_index: Int | None = None, active_item: Pointer | None = None, skip: Bool | None = None, geometry: Geometry | None = None, : Virtual | None = None) -> SimulationOutput.Result: """![](image_placeholder.webp)"""
def slice_string(string: String | None = None, position: Int | None = None, length: Int | None = None) -> String: """![](image_placeholder.webp)"""
def sort_elements(domain: SortElements.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None, group_id: Int | None = None, sort_weight: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
def special_characters() -> SpecialCharacters.Result: """![](image_placeholder.webp)"""
def spiral(resolution: IntUnsigned | None = None, rotations: Float | None = None, start_radius: FloatDistance | None = None, end_radius: FloatDistance | None = None, height: FloatDistance | None = None, reverse: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def spline_length() -> SplineLength.Result: """![](image_placeholder.webp)"""
def spline_parameter() -> SplineParameter.Result: """![](image_placeholder.webp)"""
def spline_resolution() -> Int: """![](image_placeholder.webp)"""
def split_edges(mesh: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def split_to_instances(domain: SplitToInstances.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None, group_id: Int | None = None) -> SplitToInstances.Result: """![](image_placeholder.webp)"""
def star(points: IntUnsigned | None = None, inner_radius: FloatDistance | None = None, outer_radius: FloatDistance | None = None, twist: FloatAngle | None = None) -> Star.Result: """![](image_placeholder.webp)"""
def store_named_attribute(data_type: StoreNamedAttribute.DataType | None = None, domain: StoreNamedAttribute.Domain | None = None, geometry: Geometry | None = None, selection: Bool | None = None, name: String | None = None, value: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
def store_named_grid(data_type: StoreNamedGrid.DataType | None = None, volume: Geometry | None = None, name: String | None = None, grid: Float | None = None) -> Geometry: """![](image_placeholder.webp)"""
def string(string: String | None = None) -> String: """![](image_placeholder.webp)"""
def string_length(string: String | None = None) -> Int: """![](image_placeholder.webp)"""
def string_to_curves(font: Pointer | None = None, overflow: StringToCurves.Overflow | None = None, align_x: StringToCurves.AlignX | None = None, align_y: StringToCurves.AlignY | None = None, pivot_mode: StringToCurves.PivotMode | None = None, string: String | None = None, size: FloatDistance | None = None, character_spacing: Float | None = None, word_spacing: Float | None = None, line_spacing: Float | None = None, text_box_width: FloatDistance | None = None, text_box_height: FloatDistance | None = None) -> StringToCurves.Result: """![](image_placeholder.webp)"""
def subdivide_curve(curve: Geometry | None = None, cuts: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
def subdivide_mesh(mesh: Geometry | None = None, level: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
def subdivision_surface(uv_smooth: SubdivisionSurface.UvSmooth | None = None, boundary_smooth: SubdivisionSurface.BoundarySmooth | None = None, mesh: Geometry | None = None, level: Int | None = None, edge_crease: FloatFactor | None = None, vertex_crease: FloatFactor | None = None, limit_surface: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def switch(input_type: Switch.InputType | None = None, switch: Bool | None = None, false: Geometry | None = None, true: Geometry | None = None) -> Geometry: """![](image_placeholder.webp)"""
def transform_direction(direction: VectorXYZ | None = None, transform: Matrix | None = None) -> VectorXYZ: """![](image_placeholder.webp)"""
def transform_geometry(mode: TransformGeometry.Mode | None = None, geometry: Geometry | None = None, translation: VectorTranslation | None = None, rotation: Rotation | None = None, scale: VectorXYZ | None = None, transform: Matrix | None = None) -> Geometry: """![](image_placeholder.webp)"""
def transform_gizmo(use_translation_x: Boolean | None = None, use_translation_y: Boolean | None = None, use_translation_z: Boolean | None = None, use_rotation_x: Boolean | None = None, use_rotation_y: Boolean | None = None, use_rotation_z: Boolean | None = None, use_scale_x: Boolean | None = None, use_scale_y: Boolean | None = None, use_scale_z: Boolean | None = None, value: List[Matrix] | None = None, position: VectorTranslation | None = None, rotation: Rotation | None = None) -> Geometry: """![](image_placeholder.webp)"""
def transform_point(vector: VectorXYZ | None = None, transform: Matrix | None = None) -> VectorXYZ: """![](image_placeholder.webp)"""
def translate_instances(instances: Geometry | None = None, selection: Bool | None = None, translation: VectorTranslation | None = None, local_space: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def transpose_matrix(matrix: Matrix | None = None) -> Matrix: """![](image_placeholder.webp)"""
def triangulate(quad_method: Triangulate.QuadMethod | None = None, ngon_method: Triangulate.NgonMethod | None = None, mesh: Geometry | None = None, selection: Bool | None = None) -> Geometry: """![](image_placeholder.webp)"""
def trim_curve(mode: TrimCurve.Mode | None = None, curve: Geometry | None = None, selection: Bool | None = None, start: FloatDistance | None = None, end: FloatDistance | None = None) -> Geometry: """![](image_placeholder.webp)"""
def uv_sphere(segments: Int | None = None, rings: Int | None = None, radius: FloatDistance | None = None) -> UvSphere.Result: """![](image_placeholder.webp)"""
def uv_unwrap(method: UvUnwrap.Method | None = None, selection: Bool | None = None, seam: Bool | None = None, margin: Float | None = None, fill_holes: Bool | None = None) -> Vector: """![](image_placeholder.webp)"""
def value() -> Float: """![](image_placeholder.webp)"""
def value_to_string(data_type: ValueToString.DataType | None = None, value: Float | None = None, decimals: Int | None = None) -> String: """![](image_placeholder.webp)"""
def vector(vector: Float | None = None) -> Vector: """![](image_placeholder.webp)"""
def vector_curves(mapping: Pointer | None = None, fac: FloatFactor | None = None, vector: Vector | None = None) -> Vector: """![](image_placeholder.webp)"""
def vector_math(operation: VectorMath.Operation | None = None, vector: Vector | None = None, scale: Float | None = None) -> VectorMath.Result: """![](image_placeholder.webp)"""
def vector_rotate(rotation_type: VectorRotate.RotationType | None = None, invert: Boolean | None = None, vector: Vector | None = None, center: Vector | None = None, axis: Vector | None = None, angle: FloatAngle | None = None, rotation: VectorEuler | None = None) -> Vector: """![](image_placeholder.webp)"""
def vertex_neighbors() -> VertexNeighbors.Result: """![](image_placeholder.webp)"""
def vertex_of_corner(corner_index: Int | None = None) -> Int: """![](image_placeholder.webp)"""
def viewer(data_type: Viewer.DataType | None = None, domain: Viewer.Domain | None = None, ui_shortcut: Int | None = None, geometry: Geometry | None = None, value: Float | None = None) -> Viewer.Result: """![](image_placeholder.webp)"""
def viewport_transform() -> ViewportTransform.Result: """![](image_placeholder.webp)"""
def volume_cube(density: Float | None = None, background: Float | None = None, min: Vector | None = None, max: Vector | None = None, resolution_x: Int | None = None, resolution_y: Int | None = None, resolution_z: Int | None = None) -> Geometry: """![](image_placeholder.webp)"""
def volume_to_mesh(resolution_mode: VolumeToMesh.ResolutionMode | None = None, volume: Geometry | None = None, voxel_size: FloatDistance | None = None, voxel_amount: Float | None = None, threshold: Float | None = None, adaptivity: FloatFactor | None = None) -> Geometry: """![](image_placeholder.webp)"""
def voronoi_texture(texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, voronoi_dimensions: VoronoiTexture.VoronoiDimensions | None = None, distance: VoronoiTexture.Distance | None = None, feature: VoronoiTexture.Feature | None = None, normalize: Boolean | None = None, vector: Vector | None = None, w: Float | None = None, scale: Float | None = None, detail: Float | None = None, roughness: FloatFactor | None = None, lacunarity: Float | None = None, smoothness: FloatFactor | None = None, exponent: Float | None = None, randomness: FloatFactor | None = None) -> VoronoiTexture.Result: """![](image_placeholder.webp)"""
def warning(warning_type: Warning.WarningType | None = None, show: Bool | None = None, message: String | None = None) -> Bool: """![](image_placeholder.webp)"""
def wave_texture(texture_mapping: Pointer | None = None, color_mapping: Pointer | None = None, wave_type: WaveTexture.WaveType | None = None, bands_direction: WaveTexture.BandsDirection | None = None, rings_direction: WaveTexture.RingsDirection | None = None, wave_profile: WaveTexture.WaveProfile | None = None, vector: Vector | None = None, scale: Float | None = None, distortion: Float | None = None, detail: Float | None = None, detail_scale: Float | None = None, detail_roughness: FloatFactor | None = None, phase_offset: Float | None = None) -> WaveTexture.Result: """![](image_placeholder.webp)"""
def white_noise_texture(noise_dimensions: WhiteNoiseTexture.NoiseDimensions | None = None, vector: Vector | None = None, w: Float | None = None) -> WhiteNoiseTexture.Result: """![](image_placeholder.webp)"""

# simulation.py
import bpy
import inspect
import typing


def simulation_zone(block: typing.Callable):
    """
    Create a simulation input/output block.

    In Blender 4.0+, you must return a boolean value for the "Skip" argument as the first element in the return tuple.

    > Only available in Blender 3.6+.
    """

    def wrapped(*args, **kwargs):
        from geometry_script.api.node_mapper import OutputsList, set_or_create_link
        from geometry_script.api.state import State
        from geometry_script.api.types import Type, socket_class_to_data_type

        signature = inspect.signature(block)

        # setup zone
        simulation_in = State.current_node_tree.nodes.new(
            bpy.types.GeometryNodeSimulationInput.__name__
        )
        simulation_out = State.current_node_tree.nodes.new(
            bpy.types.GeometryNodeSimulationOutput.__name__
        )
        simulation_in.pair_with_output(simulation_out)

        # clear state items
        for item in simulation_out.state_items:
            simulation_out.state_items.remove(item)

        # create state items from block signature
        state_items = {}
        for param in [*signature.parameters.values()][1:]:
            state_items[param.name] = (param.annotation, param.default, None, None)
        for i, arg in enumerate(state_items.items()):
            simulation_out.state_items.new(
                socket_class_to_data_type(arg[1][0].socket_type),
                arg[0].replace("_", " ").title(),
            )
            set_or_create_link(
                kwargs[arg[0]] if arg[0] in kwargs else args[i], simulation_in.inputs[i]
            )

        step = block(*[Type(o) for o in simulation_in.outputs[:-1]])

        if isinstance(step, Type):
            step = (step,)
        for i, result in enumerate(step):
            set_or_create_link(result, simulation_out.inputs[i])

        if len(simulation_out.outputs[:-1]) == 1:
            return Type(simulation_out.outputs[0])
        else:
            return OutputsList(
                {
                    o.name.lower().replace(" ", "_"): Type(o)
                    for o in simulation_out.outputs[:-1]
                }
            )

    return wrapped


# attribute.py
class Attribute:
    """
    A class that represents named attributes, providing methods for accessing and storing them.

    Create an attribute with a name, data type, and optional domain.
    ```python
    height_level = Attribute(
        "height_level",
        NamedAttribute.DataType.FLOAT,
        StoreNamedAttribute.Domain.POINT # optional
    )
    ```

    Access the attribute value by calling the class instance.
    ```python
    height_level()
    ```

    Store a value for the named attribute on some geometry with `store(...)`.
    ```python
    height_level.store(geometry, value)
    ```

    Check if the attribute exists on some geometry with `exists()`.
    ```python
    selection = height_level.exists()
    ```
    """

    name: str
    data_type: "NamedAttribute.DataType"
    domain: "StoreNamedAttribute.Domain"

    def __init__(
        self,
        name: str,
        data_type: "NamedAttribute.DataType",
        domain: "StoreNamedAttribute.Domain" = "POINT",
    ):
        self.name = name
        self.data_type = data_type
        self.domain = domain

    def __call__(self, *args, **kwargs):
        """
        Creates a "Named Attribute" node with the correct arguments passed, and returns the "Attribute" socket.
        """
        from ... import named_attribute
        from ...api.types import Type

        result = named_attribute(
            data_type=self.data_type, name=self.name, *args, **kwargs
        )
        # Handle Blender 3.5+, which includes an `exists` result.
        if isinstance(result, Type):
            return result
        else:
            return result.attribute

    def exists(self, *args, **kwargs):
        """
        Creates a "Named Attribute" node with the correct arguments passed, and returns the "Exists" socket.

        > Only available in Blender 3.5+
        """
        from ... import named_attribute

        return named_attribute(
            data_type=self.data_type, name=self.name, *args, **kwargs
        ).exists

    def store(self, geometry: "Geometry", value, *args, **kwargs) -> "Geometry":
        """
        Creates a "Store Named Attribute" node with the correct arguments passed, and returns the modified `Geometry`.
        """
        from ... import store_named_attribute

        if "domain" not in kwargs:
            kwargs["domain"] = self.domain
        return store_named_attribute(
            data_type=self.data_type,
            geometry=geometry,
            name=self.name,
            value=value,
            *args,
            **kwargs,
        )


# __init__.py
"""
Static node implementations for Geometry Script
"""


# curve.py
from typing import List
import enum


class HandleType(enum.Enum):
    AUTO = "AUTO"
    VECTOR = "VECTOR"
    AUTO_CLAMPED = "AUTO_CLAMPED"


class Point:
    """
    A single point on a curve
    """

    x: float
    y: float
    handle_type: HandleType

    def __init__(self, x: float, y: float, handle_type: HandleType = HandleType.AUTO):
        self.x = x
        self.y = y
        self.handle_type = handle_type


class Curve:
    """
    A class that represents a curve.

    Create a curve from a set of `Point`s.
    ```python
    my_curve = Curve(
        Point(0, 0, Handle.AUTO_CLAMPED),
        Point(0.2, 0.3, Handle.AUTO),
        Point(1, 1, Handle.VECTOR)
    )
    ```
    """

    points: List[Point]

    def __init__(self, *points: Point):
        if len(points) == 1 and isinstance(points[0], list):
            self.points = points[0]
        else:
            self.points = list(points)

    def apply(self, curve):
        """
        Apply the points to a curve object.
        """
        for i, point in enumerate(self.points):
            if len(curve.points) > i:
                curve.points[i].location = (point.x, point.y)
                curve.points[i].handle_type = point.handle_type.value
            else:
                curve.points.new(point.x, point.y).handle_type = point.handle_type.value


# input_group.py
class _InputGroupMeta(type):
    def __getitem__(cls, args):
        if isinstance(args, str):

            class PrefixedInputGroup(InputGroup):
                prefix = args

            PrefixedInputGroup.__annotations__ = cls.__annotations__
            return PrefixedInputGroup
        return cls


class InputGroup(metaclass=_InputGroupMeta):
    """
    A group of inputs that will be expanded in the node tree.

    All properties must be annotated:
    ```python
    class MyInputGroup(InputGroup):
        my_float: Float
        my_bool: Bool
        my_string # Invalid
    ```
    """

    def __init__(self, **kwargs):
        for p in dir(self):
            if p in kwargs:
                setattr(self, p, kwargs[p])


# repeat.py
import bpy
import inspect
import typing


def repeat_zone(block: typing.Callable):
    """
    Create a repeat input/output block.

    > Only available in Blender 4.0+.
    """

    def wrapped(*args, **kwargs):
        from geometry_script.api.node_mapper import OutputsList, set_or_create_link
        from geometry_script.api.state import State
        from geometry_script.api.types import Type, socket_class_to_data_type

        signature = inspect.signature(block)

        # setup zone
        repeat_in = State.current_node_tree.nodes.new(
            bpy.types.GeometryNodeRepeatInput.__name__
        )
        repeat_out = State.current_node_tree.nodes.new(
            bpy.types.GeometryNodeRepeatOutput.__name__
        )
        repeat_in.pair_with_output(repeat_out)

        # clear state items
        for item in repeat_out.repeat_items:
            repeat_out.repeat_items.remove(item)

        # link the iteration count
        set_or_create_link(args[0], repeat_in.inputs[0])

        # create state items from block signature
        repeat_items = {}
        for param in signature.parameters.values():
            repeat_items[param.name] = (param.annotation, param.default, None, None)
        for i, arg in enumerate(repeat_items.items()):
            repeat_out.repeat_items.new(
                socket_class_to_data_type(arg[1][0].socket_type),
                arg[0].replace("_", " ").title(),
            )
            # skip the first index, which is reserved for the iteration count
            i = i + 1
            set_or_create_link(
                kwargs[arg[0]] if arg[0] in kwargs else args[i], repeat_in.inputs[i]
            )

        step = block(*[Type(o) for o in repeat_in.outputs[:-1]])

        if isinstance(step, Type):
            step = (step,)
        for i, result in enumerate(step):
            set_or_create_link(result, repeat_out.inputs[i])

        if len(repeat_out.outputs[:-1]) == 1:
            return Type(repeat_out.outputs[0])
        else:
            return OutputsList(
                {
                    o.name.lower().replace(" ", "_"): Type(o)
                    for o in repeat_out.outputs[:-1]
                }
            )

    return wrapped


# expression.py
def scripted_expression(scripted_expression: str) -> "Type":
    from ...api.types import Type
    from ...api.state import State

    value_node = State.current_node_tree.nodes.new("ShaderNodeValue")
    fcurve = value_node.outputs[0].driver_add("default_value")
    fcurve.driver.expression = scripted_expression
    return Type(value_node.outputs[0])


# sample_mode.py
import enum


class SampleMode(enum.IntEnum):
    INDEX = 0
    NEAREST_SURFACE = 1
    NEAREST = 2
