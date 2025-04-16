from .core import Relation, Selector

IS_MANIFESTATION_OF = Relation(
    alias="IS_MANIFESTATION_OF",
    selectors=[
        Selector(
            query="""
SELECT
    "H-ID" as "to",
    "is_manifestation_of H-ID" as "from"
FROM Witness
WHERE "is_manifestation_of H-ID" IS NOT NULL
""",
            from_node="Witness",
            to_node="Text",
        )
    ],
)
