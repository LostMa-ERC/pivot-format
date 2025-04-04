from app.graph.edges.utils.edge_dataclass import Edge
from app.graph.edges.utils.from_to_relation import FromToEdgeRelation

HasLangauge = Edge(
    edge_label="HAS_LANGAUGE",
    relations=[
        FromToEdgeRelation(
            from_node="Text",
            to_node="Language",
            sql_query_for_selecting_data="""
                SELECT
                    "H-ID" as "from",
                    CAST("language_COLUMN TRM-ID" AS INT64) as "to"
                FROM TextTable
                WHERE "language_COLUMN TRM-ID" is not null
            """,
        )
    ],
)
