from .core import Relation, Selector

IS_MODELED_ON = Relation(
    alias="IS_MODELED_ON",
    selectors=[
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    unnest("is_modeled_on H-ID") as "to"
FROM Story
WHERE "is_modeled_on H-ID" != []
""",
            from_node="Story",
            to_node="Story",
        )
    ],
)
