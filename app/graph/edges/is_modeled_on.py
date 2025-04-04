from app.graph.edges.utils.edge_dataclass import Edge
from app.graph.edges.utils.from_to_relation import FromToEdgeRelation

IsModeledOn = Edge(
    edge_label="IS_MODELED_ON",
    relations=[
        FromToEdgeRelation(
            from_node="Story",
            to_node="Story",
            sql_query_for_selecting_data="""
                SELECT
                    "H-ID" as "from",
                    unnest("is_modeled_on H-ID") as "to"
                FROM Story
                WHERE "is_modeled_on H-ID" != []
                """,
        )
    ],
)
