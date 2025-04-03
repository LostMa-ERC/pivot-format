from app.graph.edges.utils.edge_dataclass import Edge
from app.graph.edges.utils.from_to_relation import FromToEdgeRelation

TextHasGenre = Edge(
    table_name="HAS_GENRE",
    relations=[
        FromToEdgeRelation(
            from_node="Text",
            to_node="Genre",
            duckdb_query="""
                SELECT
                    "H-ID" as "from",
                    "specific_genre H-ID" as "to"
                FROM TextTable
                WHERE "specific_genre H-ID" IS NOT NULL
            """,
        )
    ],
)
