from .core import Edge, FromToPair

HAS_LANGAUGE = Edge(
    label="HAS_LANGUAGE",
    from_to_pairs=[
        FromToPair(from_node="Text", to_node="Language"),
    ],
)
