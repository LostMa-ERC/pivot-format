from .core import Edge, FromToPair

HAS_DESCRIPTION = Edge(
    label="HAS_DESCRIPTION",
    from_to_pairs=[
        FromToPair(from_node="Part", to_node="PhysDesc"),
    ],
)
