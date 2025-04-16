from dataclasses import dataclass, field

from app.graph import Property


@dataclass
class FromToPair:
    from_node: str
    to_node: str


@dataclass
class Edge:
    label: str
    from_to_pairs: list[FromToPair]
    properties: list[Property] = field(default_factory=list)

    def create_table_stmt(self) -> str:
        props = [f"FROM {p.from_node} TO {p.to_node}" for p in self.from_to_pairs]
        props.extend([f"{p.name} {p.type.value}" for p in self.properties])
        return f"CREATE REL TABLE {self.label} ({", ".join(props)});"

    def copy_stmt(self, from_node: str, to_node: str, fp: str) -> str:
        return f"COPY {self.label} FROM '{fp}' (FROM='{from_node}', TO='{to_node}')"
