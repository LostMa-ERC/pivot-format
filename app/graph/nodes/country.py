from app.graph import Property, Type

from .core import Node

COUNTRY_PROPS = [
    Property(name="id", type=Type.int),
    Property(name="name", type=Type.string),
    Property(name="code", type=Type.string),
]

Country = Node(label="Country", pk="id", properties=COUNTRY_PROPS)
