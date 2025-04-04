from pathlib import Path

from duckdb import DuckDBPyConnection
from kuzu import Connection, QueryResult

from .edge_dataclass import Edge
from .from_to_relation import FromToEdgeRelation


class EdgeBuilder:
    def __init__(self, kconn: Connection, dconn: DuckDBPyConnection):
        self.kconn = kconn
        self.dconn = dconn

    @classmethod
    def compose_create_statement(cls, edge: Edge) -> str:
        pairs = [f"FROM {r.from_node} TO {r.to_node}" for r in edge.relations]
        props = pairs + edge.properties
        return f"""
CREATE REL TABLE IF NOT EXISTS {edge.edge_label} (
    {', '.join(props)}
)
"""

    def __call__(self, edge: Edge) -> QueryResult:
        # Build the edge table in the connected Kuzu database
        creation_stmt = self.compose_create_statement(edge=edge)
        self.kconn.execute(f"DROP TABLE IF EXISTS {edge.edge_label}")
        self.kconn.execute(creation_stmt)

        # For each relation (from-to node pair) in the edge table, select its
        # data from the DuckDB database and copy it into the edge table
        for from_to_relation in edge.relations:
            self.copy_data_into_table(
                from_to_relation=from_to_relation,
                edge=edge,
            )

        query = f"MATCH ()-[r:{edge.edge_label}]->() RETURN r"
        return self.kconn.execute(query)

    def copy_data_into_table(
        self,
        from_to_relation: FromToEdgeRelation,
        edge: Edge,
    ):
        # Get the edge data from DuckDB
        df = self.dconn.sql(from_to_relation.sql_query_for_selecting_data).pl()

        # Write the dataframe to a temporary parquet file
        tmp = Path("tmp.parquet")
        df.write_parquet(tmp)

        # Copy the dataframe to the relational table in Kuzu
        try:
            self.kconn.execute(
                f"""
    COPY {edge.edge_label} FROM '{tmp}'
    (from='{from_to_relation.from_node}', to='{from_to_relation.to_node}')
    """
            )
        except Exception as e:
            print(edge.edge_label)
            print(df)
            raise e

        # Delete the temporary parquet file
        tmp.unlink()
