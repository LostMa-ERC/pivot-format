from pathlib import Path
from kuzu import Connection, QueryResult
from duckdb import DuckDBPyConnection

from .from_to_relation import FromToEdgeRelation
from .edge_dataclass import Edge


class EdgeBuilder:
    def __init__(self, kconn: Connection, dconn: DuckDBPyConnection):
        self.kconn = kconn
        self.dconn = dconn

    @classmethod
    def compose_create_statement(cls, edge: Edge) -> str:
        pairs = [f"FROM {r.from_node} TO {r.to_node}" for r in edge.relations]
        props = pairs + edge.properties
        return f"""
CREATE REL TABLE IF NOT EXISTS {edge.table_name} (
    {', '.join(props)}
)
"""

    def __call__(
        self, edge: Edge, drop: bool = False, fill_null: bool = True
    ) -> QueryResult:
        # Build the edge table in the connected Kuzu database
        self.create_rel_table(edge=edge, drop=drop)

        # For each relation (from-to node pair) in the edge table,
        # select its data from the DuckDB database
        for rel in edge.relations:
            self.copy_data_into_table(
                rel=rel,
                edge=edge,
                fill_null=fill_null,
            )

        query = f"MATCH ()-[r:{edge.table_name}]->() RETURN r"
        return self.kconn.execute(query)

    def create_rel_table(self, edge: Edge, drop: bool) -> QueryResult:
        creation_stmt = self.compose_create_statement(edge=edge)
        if drop:
            self.kconn.execute(f"DROP TABLE IF EXISTS {edge.table_name}")
        r = self.kconn.execute(creation_stmt)
        return r

    def copy_data_into_table(
        self,
        rel: FromToEdgeRelation,
        edge: Edge,
        fill_null: bool,
    ):
        # Get the edge data from DuckDB
        df = self.dconn.sql(rel.duckdb_query).pl()
        if fill_null:
            df.fill_null("")

        # Write the dataframe to a temporary parquet file
        tmp = Path("tmp.parquet")
        df.write_parquet(tmp)

        # Copy the dataframe to the relational table in Kuzu
        try:
            self.kconn.execute(
                f"""
    COPY {edge.table_name} FROM '{tmp}'
    (from='{rel.from_node}', to='{rel.to_node}')
    """
            )
        except Exception as e:
            print(edge.table_name)
            print(df)
            raise e

        # Delete the temporary parquet file
        tmp.unlink()
