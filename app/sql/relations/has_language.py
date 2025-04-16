from .core import Relation, Selector

HAS_LANGUAGE = Relation(
    alias="HAS_LANGUAGE",
    selectors=[
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    CAST("language_COLUMN TRM-ID" AS INT64) as "to"
FROM TextTable
WHERE "language_COLUMN TRM-ID" is not null
""",
            from_node="Text",
            to_node="Language",
        )
    ],
)
