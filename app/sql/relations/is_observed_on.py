from .core import Relation, Selector

IS_OBSERVED_ON = Relation(
    alias="IS_OBSERVED_ON",
    selectors=[
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    unnest("observed_on_pages H-ID") as "to"
FROM Witness
WHERE "observed_on_pages H-ID" is not null
""",
            from_node="Witness",
            to_node="Part",
        ),
    ],
)
