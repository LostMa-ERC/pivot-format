from app.graph import Property, Type

from .core import Node

PHYSDESC_PROPS = [
    Property(name="id", type=Type.int),
    Property(name="material", type=Type.string),
    Property(name="form", type=Type.string),
    Property(name="folio_size_width", type=Type.string),
    Property(name="folio_size_height", type=Type.string),
    Property(name="estimated_folio_size_height", type=Type.string),
    Property(name="estimated_folio_size_width", type=Type.string),
    Property(name="has_decorations", type=Type.string_list),
    Property(name="amount_of_illustrations", type=Type.string),
    Property(name="writing_surface_area_height", type=Type.string),
    Property(name="writing_surface_area_width", type=Type.string),
    Property(name="number_of_columns", type=Type.string),
    Property(name="number_of_lines_in_writing_area", type=Type.string),
    Property(name="above_top_line", type=Type.string),
    Property(name="script_type", type=Type.string),
    Property(name="subscript_type", type=Type.string),
]

PhysDesc = Node(label="PhysDesc", pk="id", properties=PHYSDESC_PROPS)
