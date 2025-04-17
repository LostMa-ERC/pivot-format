from .core import Relation, Selector

HAS_SCRIPT = Relation(
    alias="HAS_SCRIPT",
    selectors=[
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    CAST("regional_writing_style H-ID" AS INT64) as "to"
FROM Witness
WHERE "regional_writing_style H-ID" is not null
""",
            from_node="Witness",
            to_node="Scripta",
        ),
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    CAST("regional_writing_style H-ID" AS INT64) as "to"
FROM TextTable
WHERE "regional_writing_style H-ID" is not null
""",
            from_node="Text",
            to_node="Scripta",
        ),
    ],
)
