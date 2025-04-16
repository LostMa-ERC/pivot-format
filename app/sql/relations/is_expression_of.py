from .core import Relation, Selector

IS_EXPRESSION_OF = Relation(
    alias="IS_EXPRESSION_OF",
    selectors=[
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    unnest("is_expression_of H-ID") as "to"
FROM TextTable
WHERE "is_expression_of H-ID" != []
""",
            from_node="Text",
            to_node="Story",
        )
    ],
)
