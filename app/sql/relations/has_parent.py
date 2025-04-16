from .core import Relation, Selector

HAS_PARENT = Relation(
    alias="HAS_PARENT",
    selectors=[
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    "parent_genre H-ID" as "to"
FROM Genre
WHERE "parent_genre H-ID" IS NOT NULL
""",
            from_node="Genre",
            to_node="Genre",
        )
    ],
)
