from app.graph import Property, Type

from .core import Node

STORY_PROPS = [
    Property(name="id", type=Type.int),
    Property(name="name", type=Type.string),
    Property(name="alternative_names", type=Type.string_list),
    Property(name="matter", type=Type.string),
    Property(name="peripheral", type=Type.boolean),
    Property(name="urls", type=Type.string_list),
]

Story = Node(label="Story", pk="id", properties=STORY_PROPS)
