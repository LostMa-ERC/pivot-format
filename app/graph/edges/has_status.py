from .core import Edge, FromToPair

HAS_STATUS = Edge(
    label="HAS_STATUS",
    from_to_pairs=[
        FromToPair(from_node="Text", to_node="TraditionStatus"),
    ],
)
