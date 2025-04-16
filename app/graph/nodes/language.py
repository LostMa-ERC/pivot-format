from app.graph import Property, Type

from .core import Node

LANGUAGE_PROPS = [
    Property(name="id", type=Type.int),
    Property(name="name", type=Type.string),
    Property(name="code", type=Type.string),
    Property(name="description", type=Type.string),
    Property(name="url", type=Type.string),
]

Language = Node(label="Language", pk="id", properties=LANGUAGE_PROPS)
