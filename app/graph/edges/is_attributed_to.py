from app.graph.edges.utils.edge_dataclass import Edge
from app.graph.edges.utils.from_to_relation import FromToEdgeRelation


IsAttributedTo = Edge(
    table_name="IS_ATTRIBUTED_TO",
    relations=[
        FromToEdgeRelation(
            from_node="Text",
            to_node="Person",
            duckdb_query="""
                SELECT
                    "H-ID" as "from",
                    unnest("is_written_by H-ID") as "to",
                    'author'
                FROM TextTable
                WHERE length("is_written_by H-ID") > 1
            """,
        )
    ],
    properties=["role STRING"],
)
