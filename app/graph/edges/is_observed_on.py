from .core import Edge, FromToPair

IS_OBSERVED_ON = Edge(
    label="IS_OBSERVED_ON",
    from_to_pairs=[
        FromToPair(from_node="Witness", to_node="Part"),
    ],
)
