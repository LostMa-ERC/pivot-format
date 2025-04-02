import kuzu
import duckdb

from app.graph.edges import EdgeBuilder
from app.graph.nodes import NodeBuilder
from app import KUZU_DB, HEURIST_DB
from app.graph.builders import create_all_edges, create_all_nodes

EdgeBuilder
NodeBuilder


def build_graph_from_defaults(kconn: kuzu.Connection | None = None):
    dconn = duckdb.connect(HEURIST_DB)
    if not kconn:
        db = kuzu.Database(KUZU_DB)
        kconn = kuzu.Connection(db)
    create_all_nodes(kconn=kconn, dconn=dconn)
    create_all_edges(kconn=kconn, dconn=dconn)
