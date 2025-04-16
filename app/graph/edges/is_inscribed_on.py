from .core import Edge, FromToPair

IS_INSCRIBED_ON = Edge(
    label="IS_INSCRIBED_ON",
    from_to_pairs=[
        FromToPair(from_node="Part", to_node="Document"),
    ],
)
