from app.graph import Property, Type

from .core import Node

SCRIPTA_PROPS = [
    Property(name="id", type=Type.int),
    Property(name="name", type=Type.string),
    Property(name="description", type=Type.string),
    Property(name="region_note", type=Type.string),
    Property(name="urls", type=Type.string_list),
]

Scripta = Node(label="Scripta", pk="id", properties=SCRIPTA_PROPS)
