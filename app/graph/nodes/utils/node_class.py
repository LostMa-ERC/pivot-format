from .property_metadata import PropertyMetadata


class Node:
    def __init__(
        self,
        table_name: str,
        pk: str,
        metadata: list[PropertyMetadata],
        duckdb_query: str | None = None,
        table: str | None = None,
    ):
        self.table_name = table_name
        self.pk = pk
        self.metadata = metadata
        self.table = table
        self.duckdb_query = duckdb_query
        if not duckdb_query:
            self.duckdb_query = self.make_duckdb_query()

    def list_cypher_props(self) -> list[str]:
        return [m.cypher_alias for m in self.metadata]

    @property
    def create_statement(self) -> str:
        params = self.list_cypher_props() + [f"PRIMARY KEY ({self.pk})"]
        return f"""
    CREATE NODE TABLE {self.table_name}
    (
        {', '.join(params)}
    )"""

    def make_duckdb_query(self) -> str:
        aliases = ", ".join([m.sql_alias for m in self.metadata])
        return f"SELECT {aliases} FROM {self.table}"
