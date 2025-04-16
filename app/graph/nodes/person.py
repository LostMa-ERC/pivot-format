from app.graph import Property, Type

from .core import Node

PERSON_RPOPS = [
    Property(name="id", type=Type.int),
    Property(name="family_name", type=Type.string),
    Property(name="given_names", type=Type.string),
    Property(name="alternative_names", type=Type.string_list),
    Property(name="urls", type=Type.string_list),
]

Person = Node(label="Person", pk="id", properties=PERSON_RPOPS)
