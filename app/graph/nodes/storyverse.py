from app.graph import Property, Type

from .core import Node

STORYVERSE_PROPS = [
    Property(name="id", type=Type.int),
    Property(name="name", type=Type.string),
    Property(name="alternative_names", type=Type.string_list),
    Property(name="urls", type=Type.string_list),
]

Storyverse = Node(label="Storyverse", pk="id", properties=STORYVERSE_PROPS)
