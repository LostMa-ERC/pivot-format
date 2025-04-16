from .core import Edge, FromToPair

IS_MANIFESTATION_OF = Edge(
    label="IS_MANIFESTATION_OF",
    from_to_pairs=[
        FromToPair(from_node="Witness", to_node="Text"),
    ],
)
