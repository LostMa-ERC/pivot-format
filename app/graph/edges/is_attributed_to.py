from app.graph import Property, Type

from .core import Edge, FromToPair

IS_ATTRIBUTED_TO = Edge(
    label="IS_ATTRIBUTED_TO",
    from_to_pairs=[
        FromToPair(from_node="Text", to_node="Person"),
    ],
    properties=[Property(name="role", type=Type.string)],
)
