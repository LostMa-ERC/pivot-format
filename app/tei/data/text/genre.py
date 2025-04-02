from kuzu import Connection
from typing import Optional

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


def fetch_genres(conn: Connection, id: int) -> list[GenreModel]:
    query = f"""
MATCH (a:Text)
-[r:{TextHasGenre.table_name}|{GenreHasParent.table_name} *1..]
->(b:Genre) WHERE a.id = {id} RETURN b
"""
    response = conn.execute(query)
    matches = []
    while response.has_next():
        result = response.get_next()[0]
        data = GenreModel.model_validate(result)
        matches.append(data)
    return matches
