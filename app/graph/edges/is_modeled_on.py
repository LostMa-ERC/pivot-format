from .core import Edge, FromToPair

IS_MODELED_ON = Edge(
    label="IS_MODELED_ON",
    from_to_pairs=[
        FromToPair(from_node="Story", to_node="Story"),
    ],
)
