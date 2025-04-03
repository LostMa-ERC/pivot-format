from duckdb import DuckDBPyConnection
from kuzu import Connection

from app.graph.edges.has_genre import TextHasGenre
from app.graph.edges.has_language import HasLangauge
from app.graph.edges.has_parent_genre import GenreHasParent
from app.graph.edges.has_status import HasStatus
from app.graph.edges.is_attributed_to import IsAttributedTo
from app.graph.edges.is_expression_of import TextIsExpressionOf
from app.graph.edges.is_manifestation_of import WitnessIsManifestationOf
from app.graph.edges.is_modeled_on import IsModeledOn
from app.graph.edges.is_part_of_storyverse import IsPartOfStoryverse
from app.graph.edges.utils.builder import EdgeBuilder

ALL_EDGES = [
    IsModeledOn,
    IsPartOfStoryverse,
    HasLangauge,
    TextHasGenre,
    HasStatus,
    TextIsExpressionOf,
    GenreHasParent,
    HasLangauge,
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
