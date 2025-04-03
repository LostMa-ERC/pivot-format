from app.graph.edges.utils.edge_dataclass import Edge
from app.graph.edges.utils.from_to_relation import FromToEdgeRelation

HasStatus = Edge(
    table_name="HAS_STATUS",
    relations=[
        FromToEdgeRelation(
            from_node="Text",
            to_node="TraditionStatus",
            duckdb_query="""
                SELECT
                    "H-ID" as "from",
                    CAST("tradition_status TRM-ID" AS INT64) as "to"
                FROM TextTable
                WHERE "tradition_status TRM-ID" is not null
            """,
        )
    ],
)
