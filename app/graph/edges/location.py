from .core import Edge, FromToPair

LOCATION = Edge(
    label="LOCATION",
    from_to_pairs=[
        FromToPair(from_node="Document", to_node="Repository"),
        FromToPair(from_node="Repository", to_node="Place"),
        FromToPair(from_node="Place", to_node="Country"),
    ],
)
