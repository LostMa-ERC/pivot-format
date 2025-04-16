from .core import Relation, Selector

HAS_STATUS = Relation(
    alias="HAS_STATUS",
    selectors=[
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    CAST("tradition_status TRM-ID" AS INT64) as "to"
FROM TextTable
WHERE "tradition_status TRM-ID" is not null
""",
            from_node="Text",
            to_node="TraditionStatus",
        )
    ],
)
