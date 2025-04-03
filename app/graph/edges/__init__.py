from duckdb import DuckDBPyConnection
from kuzu import Connection

from app.graph.edges.utils.builder import EdgeBuilder
from app.graph.edges.has_genre import TextHasGenre
from app.graph.edges.has_language import TextHasLanguage
from app.graph.edges.has_parent_genre import GenreHasParent
from app.graph.edges.is_attributed_to import IsAttributedTo
from app.graph.edges.is_expression_of import TextIsExpressionOf
from app.graph.edges.is_manifestation_of import WitnessIsManifestationOf
from app.graph.edges.is_modeled_on import IsModeledOn
from app.graph.edges.is_part_of_storyverse import IsPartOfStoryverse

ALL_EDGES = [
    IsModeledOn,
    IsPartOfStoryverse,
    TextHasLanguage,
    TextIsExpressionOf,
    GenreHasParent,
    TextHasGenre,
    WitnessIsManifestationOf,
    IsAttributedTo,
]


def create_all_edges(
    kconn: Connection, dconn: DuckDBPyConnection, edges=ALL_EDGES
) -> None:
    builder = EdgeBuilder(kconn=kconn, dconn=dconn)
    for edge in edges:
        try:
            builder(edge=edge)
        except RuntimeError as e:
            print(edge)
            raise e
