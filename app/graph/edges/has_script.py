from .core import Edge, FromToPair

HAS_SCRIPT = Edge(
    label="HAS_SCRIPT",
    from_to_pairs=[
        FromToPair(from_node="Witness", to_node="Scripta"),
        FromToPair(from_node="Text", to_node="Scripta"),
    ],
)
