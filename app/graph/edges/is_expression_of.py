from app.graph.edges.utils.edge_dataclass import Edge
from app.graph.edges.utils.from_to_relation import FromToEdgeRelation


TextIsExpressionOf = Edge(
    table_name="IS_EXPRESSION_OF",
    relations=[
        FromToEdgeRelation(
            from_node="Text",
            to_node="Story",
            duckdb_query="""
                SELECT
                    "H-ID" as "from",
                    unnest("is_expression_of H-ID") as "to"
                FROM TextTable
                WHERE "is_expression_of H-ID" != []
                """,
        )
    ],
)
