from dataclasses import dataclass

from app.graph import Property


@dataclass
class Node:
    label: str
    pk: str
    properties: list[Property]

    @property
    def kuzu_create_table_stmt(self) -> str:
        props = ", ".join([f"{p.name} {p.type.value}" for p in self.properties])
        return f"CREATE NODE TABLE {self.label} ({props}, PRIMARY KEY({self.pk}));"

    @property
    def pk_constraint_label(self) -> str:
        return f"{self.label}_primary_key"

    @property
    def neo4j_create_multiple_nodes_stmt(self) -> str:
        return f"""\
UNWIND $data AS properties
CREATE (n:{self.label})
SET n = properties
RETURN n
"""

    @property
    def neo4j_node_constraint(self) -> str:
        return f"""\
CREATE CONSTRAINT {self.pk_constraint_label} IF NOT EXISTS FOR (n:{self.label}) \
REQUIRE n.{self.pk} IS UNIQUE"""
