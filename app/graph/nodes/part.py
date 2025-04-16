from app.graph import Property, Type

from .core import Node

PART_PROPS = [
    Property(name="id", type=Type.int),
    Property(name="div_order", type=Type.int),
    Property(name="number_of_verses", type=Type.int),
    Property(name="part_of_text", type=Type.string),
    Property(name="volume_number", type=Type.string),
    Property(name="number_of_lines", type=Type.int),
    Property(name="verses_per_line", type=Type.string),
    Property(name="lines_are_incomplete", type=Type.boolean),
]

Part = Node(label="Part", pk="id", properties=PART_PROPS)
