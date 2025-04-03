from app.graph.edges.utils.edge_dataclass import Edge
from app.graph.edges.utils.from_to_relation import FromToEdgeRelation


TextHasLanguage = Edge(
    table_name="HAS_LANGAUGE",
    relations=[
        FromToEdgeRelation(
            from_node="Text",
            to_node="Language",
            duckdb_query="""
                SELECT
                    "H-ID" as "from",
                    CAST("language_COLUMN TRM-ID" AS INT64) as "to"
                FROM TextTable
                WHERE "language_COLUMN TRM-ID" is not null
            """,
        )
    ],
)
