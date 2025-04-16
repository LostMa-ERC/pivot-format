from .core import Relation, Selector

IS_PART_OF = Relation(
    alias="IS_PART_OF",
    selectors=[
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    unnest("is_part_of_storyverse H-ID") as "to"
FROM Story
WHERE "is_part_of_storyverse H-ID" != []
""",
            from_node="Story",
            to_node="Storyverse",
        ),
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    unnest("member_of_cycle H-ID") as "to"
FROM Storyverse
WHERE "member_of_cycle H-ID" != []
""",
            from_node="Storyverse",
            to_node="Storyverse",
        ),
    ],
)
