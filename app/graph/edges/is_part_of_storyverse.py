from app.graph.edges.utils.edge_dataclass import Edge
from app.graph.edges.utils.from_to_relation import FromToEdgeRelation

IsPartOfStoryverse = Edge(
    edge_label="IS_PART_OF_STORYVERSE",
    relations=[
        FromToEdgeRelation(
            from_node="Story",
            to_node="Storyverse",
            sql_query_for_selecting_data="""
                SELECT
                    "H-ID" as "from",
                    unnest("is_part_of_storyverse H-ID") as "to"
                FROM Story
                WHERE "is_part_of_storyverse H-ID" != []
            """,
        ),
        FromToEdgeRelation(
            from_node="Storyverse",
            to_node="Storyverse",
            sql_query_for_selecting_data="""
                SELECT
                    "H-ID" as "from",
                    unnest("member_of_cycle H-ID") as "to"
                FROM Storyverse
                WHERE "member_of_cycle H-ID" != []
            """,
        ),
    ],
)
