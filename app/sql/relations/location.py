from .core import Relation, Selector

LOCATION = Relation(
    alias="LOCATION",
    selectors=[
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    "location H-ID" as "to"
FROM DocumentTable
WHERE "location H-ID" is not null
""",
            from_node="Document",
            to_node="Repository",
        ),
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    "city H-ID" as "to"
FROM Repository
WHERE "city H-ID" is not null
""",
            from_node="Repository",
            to_node="Place",
        ),
        Selector(
            query="""
SELECT
    "H-ID" as "from",
    "country TRM-ID" as "to"
FROM Place
WHERE "country TRM-ID" is not null
""",
            from_node="Place",
            to_node="Country",
        ),
    ],
)
