from dataclasses import dataclass, field
from typing import Generator, Optional

from kuzu import Connection
from pydantic import BaseModel, Field, computed_field

from app.graph.edges.has_genre import TextHasGenre
from app.graph.edges.has_parent_genre import GenreHasParent


class GenreModel(BaseModel):
    id: int
    name: str
    alternative_names: list[Optional[str]] = Field(default=[])
    description: str
    described_at_URL: list[Optional[str]] = Field(default=[])

    @computed_field
    @property
    def xml_id(self) -> str:
        return f"genre_{self.id}"


def fetch_direct_genre(conn: Connection, text_id: int) -> GenreModel | None:
    """Given a text's unique ID, get the most direct genre associated with the text.

    Args:
        conn (Connection): Connection to a Kùzu database with the text and genre nodes.
        text_id (int): Unique ID of the text.

    Returns:
        GenreModel | None: If the text has a genre, the genre's metadata.
    """

    query = f"""
MATCH (a:Text)-[r:{TextHasGenre.table_name}]->(b:Genre) WHERE a.id = {text_id} RETURN b
    """
    response = conn.execute(query)
    while response.has_next():
        data = response.get_next()[0]
        return GenreModel.model_validate(data)


def fetch_all_genres_related_to_text(
    conn: Connection, text_id: int
) -> list[GenreModel]:
    """Given a text's unique ID, get the metadata of all the parent genres related to \
    the text's specific genre.

    Args:
        conn (Connection): Connection to the Kùzu database with the text and genres.
        text_id (int): Unique ID of the text node.

    Returns:
        list[GenreModel]: List of the parent genres of the text's genre.
    """

    query = f"""
MATCH (a:Text)
-[r:{TextHasGenre.table_name}|{GenreHasParent.table_name} *1..]
->(b:Genre) WHERE a.id = {text_id} RETURN b
"""
    response = conn.execute(query)
    matches = []
    while response.has_next():
        result = response.get_next()[0]
        data = GenreModel.model_validate(result)
        matches.append(data)
    return matches


def sort_nested_genres(id: int, conn: Connection) -> list[dict]:
    """Given the unique ID of a root genre, find all the children genres
    that descend from it.

    Args:
        id (int): Unique ID of the root genre, aka eldest parent.
        conn (Connection): Connection to the Kùzu database with genre nodes.

    Returns:
        list[dict]: List of children genres, ordered eldest first.
    """

    ordered_genres = []
    query = f"""
MATCH (g:Genre)
<-[r:HAS_PARENT *1..]-(b:Genre)
WHERE g.id = {id}
RETURN b """
    result = conn.execute(query)
    while result.has_next():
        ordered_genres.append(result.get_next()[0])
    return ordered_genres


@dataclass
class GenreFamily:
    """Dataclass for storing the sorted results of a genre's family tree."""

    root: GenreModel
    children: list[Optional[GenreModel]] = field(default_factory=list)


def fetch_all_genre_roots(conn: Connection) -> Generator[GenreFamily, None, None]:
    """Yield families of genres from the database.

    Currently, this function simplifies family relations to two categories: \
        eldest parent, all descendants.

        In future development, it might be good to fix this setback and retain a \
        tree's complexity. For now, this simpler solution is good enough because our \
        data does not have more complex genre relations.

    Args:
        conn (Connection): Connection to Kùzu database with the genre nodes.

    Yields:
        Generator[GenreFamily, None, None]: Dataclass for 1 genre family.
    """

    root_genres = """
MATCH (g:Genre)<-[r:HAS_PARENT]-(:Genre)
RETURN DISTINCT g.id AS genre, false AS isChildless
UNION ALL
MATCH (g:Genre) WHERE not ((g)-[:HAS_PARENT]-(:Genre))
RETURN g.id, true
"""
    response = conn.execute(root_genres)
    for root_id, childless in response.get_as_pl().iter_rows():
        response = conn.execute(f"MATCH (g:Genre) WHERE g.id = {root_id} RETURN g")
        df = response.get_as_pl()
        root_node = GenreModel.model_validate(df.row(0)[0])
        if childless:
            yield GenreFamily(root_node)
        else:
            sorted_genre_family = sort_nested_genres(id=root_id, conn=conn)
            children = [GenreModel.model_validate(d) for d in sorted_genre_family]
            yield GenreFamily(root_node, children)
