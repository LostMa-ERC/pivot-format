from app.graph import Property, Type

from .core import Node

TRADITION_STATUS_PROPS = [
    Property(name="id", type=Type.int),
    Property(name="name", type=Type.string),
    Property(name="code", type=Type.string),
    Property(name="description", type=Type.string),
    Property(name="url", type=Type.string),
]

TraditionStatus = Node(
    label="TraditionStatus", pk="id", properties=TRADITION_STATUS_PROPS
)
