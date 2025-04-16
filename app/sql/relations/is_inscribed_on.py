from .core import Relation, Selector

IS_INSCRIBED_ON = Relation(
    alias="IS_INSCRIBED_ON",
    selectors=[
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    "is_inscribed_on H-ID" as "to"
FROM Part
WHERE "is_inscribed_on H-ID" is not null
""",
            from_node="Part",
            to_node="Document",
        )
    ],
)
