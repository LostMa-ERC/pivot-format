from app.graph.edges.utils.edge_dataclass import Edge
from app.graph.edges.utils.from_to_relation import FromToEdgeRelation


GenreHasParent = Edge(
    table_name="HAS_PARENT",
    relations=[
        FromToEdgeRelation(
            from_node="Genre",
            to_node="Genre",
            duckdb_query="""
                SELECT
                    "H-ID" as "from",
                    "parent_genre H-ID" as "to"
                FROM Genre
                WHERE "parent_genre H-ID" IS NOT NULL
                """,
        )
    ],
)
