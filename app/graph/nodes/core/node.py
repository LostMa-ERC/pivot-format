from dataclasses import dataclass

from app.graph import Property


@dataclass
class Node:
    label: str
    pk: str
    properties: list[Property]

    def create_table_stmt(self) -> str:
        cols = ", ".join([f"{p.name} {p.type.value}" for p in self.properties])
        return f"CREATE NODE TABLE {self.label} ({cols}, PRIMARY KEY({self.pk}));"
