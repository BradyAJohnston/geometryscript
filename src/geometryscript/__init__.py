"""
Geometry Script - A Python API for Blender's Geometry Nodes

A scripting API for creating Geometry Nodes with code, providing all the 
performance and capabilities of Geometry Nodes in a more manageable format.
"""

from .api.tree import *
from .api.types import *
from .api.node_mapper import *
from .api.static.attribute import *
from .api.static.curve import *
from .api.static.expression import *
from .api.static.input_group import *
from .api.static.repeat import *
from .api.static.sample_mode import *
from .api.static.simulation import *

__version__ = "0.2.0"
__author__ = "Carson Katri"
__description__ = "Python scripting for geometry nodes"