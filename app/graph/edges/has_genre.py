from .core import Edge, FromToPair

HAS_GENRE = Edge(
    label="HAS_GENRE",
    from_to_pairs=[
        FromToPair(from_node="Text", to_node="Genre"),
    ],
)
