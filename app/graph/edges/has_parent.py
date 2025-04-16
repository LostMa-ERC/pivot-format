from .core import Edge, FromToPair

HAS_PARENT = Edge(
    label="HAS_PARENT",
    from_to_pairs=[
        FromToPair(from_node="Genre", to_node="Genre"),
    ],
)
