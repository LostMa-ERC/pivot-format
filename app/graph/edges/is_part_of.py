from .core import Edge, FromToPair

IS_PART_OF = Edge(
    label="IS_PART_OF",
    from_to_pairs=[
        FromToPair(from_node="Story", to_node="Storyverse"),
        FromToPair(from_node="Storyverse", to_node="Storyverse"),
    ],
)
