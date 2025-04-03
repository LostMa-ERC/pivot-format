from app.graph.edges.utils.edge_dataclass import Edge
from app.graph.edges.utils.from_to_relation import FromToEdgeRelation


IsModeledOn = Edge(
    table_name="IS_MODELED_ON",
    relations=[
        FromToEdgeRelation(
            from_node="Story",
            to_node="Story",
            duckdb_query="""
                SELECT
                    "H-ID" as "from",
                    unnest("is_modeled_on H-ID") as "to"
                FROM Story
                WHERE "is_modeled_on H-ID" != []
                """,
        )
    ],
)
