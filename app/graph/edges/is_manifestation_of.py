from app.graph.edges.utils.edge_dataclass import Edge
from app.graph.edges.utils.from_to_relation import FromToEdgeRelation


WitnessIsManifestationOf = Edge(
    table_name="IS_MANIFESTATION_OF",
    relations=[
        FromToEdgeRelation(
            from_node="Witness",
            to_node="Text",
            duckdb_query="""
                SELECT
                    "H-ID" as "to",
                    "is_manifestation_of H-ID" as "from"
                FROM Witness
                WHERE "is_manifestation_of H-ID" IS NOT NULL
                """,
        )
    ],
)
