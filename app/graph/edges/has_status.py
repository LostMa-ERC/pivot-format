from app.graph.edges.utils.edge_dataclass import Edge
from app.graph.edges.utils.from_to_relation import FromToEdgeRelation

HasStatus = Edge(
    edge_label="HAS_STATUS",
    relations=[
        FromToEdgeRelation(
            from_node="Text",
            to_node="TraditionStatus",
            sql_query_for_selecting_data="""
                SELECT
                    "H-ID" as "from",
                    CAST("tradition_status TRM-ID" AS INT64) as "to"
                FROM TextTable
                WHERE "tradition_status TRM-ID" is not null
            """,
        )
    ],
)
