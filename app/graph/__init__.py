import kuzu
import duckdb

from app.graph.edges import create_all_edges
from app.graph.nodes import create_all_nodes
from app import KUZU_DB, HEURIST_DB


def build_graph_from_defaults(kconn: kuzu.Connection | None = None) -> kuzu.Connection:
    """Transform the Heurist data into a Kùzu graph database.

    Args:
        kconn (kuzu.Connection | None, optional): Connection to Kùzu database. \
            Defaults to None.

    Returns:
        kuzu.Connection: Kùzu database connection in which nodes and edges were created.
    """

    dconn = duckdb.connect(HEURIST_DB)
    if not kconn:
        db = kuzu.Database(KUZU_DB)
        kconn = kuzu.Connection(db)
    create_all_nodes(kconn=kconn, dconn=dconn)
    create_all_edges(kconn=kconn, dconn=dconn)
    return kconn
