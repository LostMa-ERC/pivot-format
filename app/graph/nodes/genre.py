from app.graph import Property, Type

from .core import Node

GENRE_PROPS = [
    Property(name="id", type=Type.int),
    Property(name="name", type=Type.string),
    Property(name="alternative_names", type=Type.string_list),
    Property(name="description", type=Type.string),
    Property(name="urls", type=Type.string_list),
]

Genre = Node(label="Genre", pk="id", properties=GENRE_PROPS)
