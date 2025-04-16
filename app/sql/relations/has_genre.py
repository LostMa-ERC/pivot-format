from .core import Relation, Selector

HAS_GENRE = Relation(
    alias="HAS_GENRE",
    selectors=[
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    CAST("specific_genre H-ID" AS INT) as "to"
FROM TextTable
WHERE "specific_genre H-ID" IS NOT NULL
""",
            from_node="Text",
            to_node="Genre",
        ),
    ],
)
