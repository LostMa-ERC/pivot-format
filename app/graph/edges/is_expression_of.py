from app.graph.edges.utils.edge_dataclass import Edge
from app.graph.edges.utils.from_to_relation import FromToEdgeRelation

TextIsExpressionOf = Edge(
    edge_label="IS_EXPRESSION_OF",
    relations=[
        FromToEdgeRelation(
            from_node="Text",
            to_node="Story",
            sql_query_for_selecting_data="""
                SELECT
                    "H-ID" as "from",
                    unnest("is_expression_of H-ID") as "to"
                FROM TextTable
                WHERE "is_expression_of H-ID" != []
                """,
        )
    ],
)
