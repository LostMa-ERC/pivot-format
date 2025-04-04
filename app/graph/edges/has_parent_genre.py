from app.graph.edges.utils.edge_dataclass import Edge
from app.graph.edges.utils.from_to_relation import FromToEdgeRelation

GenreHasParent = Edge(
    edge_label="HAS_PARENT",
    relations=[
        FromToEdgeRelation(
            from_node="Genre",
            to_node="Genre",
            sql_query_for_selecting_data="""
                SELECT
                    "H-ID" as "from",
                    "parent_genre H-ID" as "to"
                FROM Genre
                WHERE "parent_genre H-ID" IS NOT NULL
                """,
        )
    ],
)
