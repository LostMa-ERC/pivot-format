from kuzu import Connection, QueryResult
from duckdb import DuckDBPyConnection

from .node_class import Node


class NodeBuilder:
    def __init__(self, kconn: Connection, dconn: DuckDBPyConnection) -> None:
        self.kconn = kconn
        self.dconn = dconn

    def __call__(
        self, node: Node, drop: bool = True, fill_null: bool = True
    ) -> QueryResult:
        # Build the node table in the connected Kuzu database
        if drop:
            self.kconn.execute(f"DROP TABLE IF EXISTS {node.table_name}")
        self.kconn.execute(node.create_statement)

        # Select data from the connected DuckDB database
        try:
            rel = self.dconn.sql(node.duckdb_query)
            df = rel.pl()
        except Exception as e:
            print(node.duckdb_query)
            raise e
        if fill_null:
            df = df.fill_null("")

        # Insert the DuckDB data into the Kuzu database
        query = f"COPY {node.table_name} FROM df"
        try:
            self.kconn.execute(query)
        except Exception as e:
            print(node.table_name)
            print(df)
            print(rel.select("creation_date"))
            raise e

        # Fetch the nodes createdin in the Kuzu database
        query = f"MATCH (n:{node.table_name}) return n"
        return self.kconn.execute(query)
