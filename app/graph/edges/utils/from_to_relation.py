from dataclasses import dataclass


@dataclass
class FromToEdgeRelation:
    from_node: str
    to_node: str
    sql_query_for_selecting_data: str
