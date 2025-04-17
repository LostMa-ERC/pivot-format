from app.graph import Property, Type

from .core import Node

REPOSITORY_PROPS = [
    Property(name="id", type=Type.int),
    Property(name="name", type=Type.string),
    Property(name="alternative_names", type=Type.string_list),
    Property(name="viaf", type=Type.string),
    Property(name="isni", type=Type.string),
    Property(name="biblissima_identifier", type=Type.string),
    Property(name="website", type=Type.string),
]

Repository = Node(label="Repository", pk="id", properties=REPOSITORY_PROPS)
