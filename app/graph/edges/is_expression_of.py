from .core import Edge, FromToPair

IS_EXPRESSION_OF = Edge(
    label="IS_EXPRESSION_OF",
    from_to_pairs=[
        FromToPair(from_node="Text", to_node="Story"),
    ],
)
