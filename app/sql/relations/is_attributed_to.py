from .core import Relation, Selector

IS_ATTRIBUTED_TO = Relation(
    alias="IS_ATTRIBTUED_TO",
    selectors=[
        Selector(
            query="""
SELECT
    "H-ID" AS "from",
    unnest("is_written_by H-ID") AS "to",
    'author' AS role
FROM TextTable
WHERE length("is_written_by H-ID") > 1
""",
            from_node="Text",
            to_node="Person",
        )
    ],
    property_names=["role"],
)
