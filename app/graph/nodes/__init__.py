from duckdb import DuckDBPyConnection
from kuzu import Connection

from app.graph.nodes.utils.builder import NodeBuilder
from app.graph.nodes.genre import Genre
from app.graph.nodes.story import Story
from app.graph.nodes.storyverse import Storyverse
from app.graph.nodes.term import Language
from app.graph.nodes.text import Text
from app.graph.nodes.witness import Witness
from app.graph.nodes.person import Person


ALL_NODES = [
    Story,
    Storyverse,
    Text,
    Language,
    Genre,
    Witness,
    Person,
]


def create_all_nodes(
    kconn: Connection, dconn: DuckDBPyConnection, nodes=ALL_NODES
) -> None:
    builder = NodeBuilder(kconn=kconn, dconn=dconn)
    for node in nodes:
        try:
            builder(node=node)
        except RuntimeError as e:
            print(node)
            raise e
