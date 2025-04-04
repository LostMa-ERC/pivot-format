from .property_metadata import PropertyMetadata


class Node:
    def __init__(
        self,
        node_label: str,
        pk: str,
        node_properties: list[PropertyMetadata],
        duckdb_query: str | None = None,
        duckdb_table: str | None = None,
    ):
        self.node_label = node_label
        self.pk = pk
        self.properties = node_properties
        self.duckdb_table = duckdb_table
        self.duckdb_query = duckdb_query
        if duckdb_query:
            self.duckdb_query = duckdb_query
        else:
            aliases = ", ".join([m.sql_alias for m in self.properties])
            self.duckdb_query = f"SELECT {aliases} FROM {self.duckdb_table}"

    def list_cypher_props(self) -> list[str]:
        return [m.cypher_alias for m in self.properties]

    @property
    def create_statement(self) -> str:
        params = self.list_cypher_props() + [f"PRIMARY KEY ({self.pk})"]
        return f"""
    CREATE NODE TABLE {self.node_label}
    (
        {', '.join(params)}
    )"""
