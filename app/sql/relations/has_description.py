from .core import Relation, Selector

HAS_DESCRIPTION = Relation(
    alias="HAS_DESCRIPTION",
    selectors=[
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    CAST("physical_description H-ID" AS INT) as "to"
FROM Part
WHERE "physical_description H-ID" is not null
""",
            from_node="Part",
            to_node="PhysDesc",
        )
    ],
)
