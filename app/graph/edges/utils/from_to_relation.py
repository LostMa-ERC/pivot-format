from dataclasses import dataclass


@dataclass
class FromToEdgeRelation:
    from_node: str
    to_node: str
    duckdb_query: str
