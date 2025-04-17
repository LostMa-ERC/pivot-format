from typing import Generator, Optional

from kuzu import Connection
from pydantic import BaseModel, Field, computed_field

from app.graph.edges import IS_OBSERVED_ON


class PartModel(BaseModel):
    id: int
    div_order: int
    number_of_verses: Optional[int] = Field(default=None)
    part_of_text: Optional[str] = Field(default=None)
    volume_number: Optional[str] = Field(default=None)
    number_of_lines: Optional[int] = Field(default=None)
    verses_per_line: Optional[str] = Field(default=None)
    lines_are_incomplete: bool

    @computed_field
    @property
    def xml_id(self) -> str:
        return f"part_{self.id}"


def yield_witness_parts(
    conn: Connection, witness_id: int
) -> Generator[PartModel, None, None]:
    query = f"""
MATCH (a:Witness)-[r:{IS_OBSERVED_ON.label}]->(b:Part) WHERE a.id = {witness_id}
RETURN b
"""
    response = conn.execute(query)
    while response.has_next():
        data = response.get_next()[0]
        yield PartModel.model_validate(data)
        yield PartModel.model_validate(data)
