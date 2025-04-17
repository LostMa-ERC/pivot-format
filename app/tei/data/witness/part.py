from dataclasses import dataclass, field
from typing import Annotated, Generator, Optional

from kuzu import Connection
from pydantic import BaseModel, BeforeValidator, Field, computed_field

from app.graph.edges import IS_INSCRIBED_ON, IS_OBSERVED_ON


@dataclass
class PageRange:
    text: str
    start: str
    end: str | None = field(default="")

    @classmethod
    def load_str(cls, text: str) -> "PageRange":
        start = text
        parts = text.split("-")
        if len(parts) == 2:
            end = parts[1]
            start = parts[0]
            return PageRange(text=text, start=start, end=end)
        return PageRange(text=text, start=start)


def parse_page_ranges(value: list) -> list[PageRange]:
    assert isinstance(value, list)
    return [PageRange.load_str(v) for v in value]


class PartModel(BaseModel):
    id: int
    div_order: int
    number_of_verses: Optional[int] = Field(default=None)
    part_of_text: Optional[str] = Field(default=None)
    volume_number: Optional[str] = Field(default=None)
    number_of_lines: Optional[int] = Field(default=None)
    verses_per_line: Optional[str] = Field(default=None)
    lines_are_incomplete: bool
    page_ranges: Annotated[list[PageRange], BeforeValidator(parse_page_ranges)]

    @computed_field
    @property
    def xml_id(self) -> str:
        return f"part_{self.id}"


def list_parts_aggregated_by_doc(
    conn: Connection, witness_id: int
) -> Generator[PartModel, None, None]:
    query = f"""
MATCH (w:Witness)-[:{IS_OBSERVED_ON.label}]-(p:Part)
    -[:{IS_INSCRIBED_ON.label}]-(d:Document)
WHERE w.id = {witness_id}
RETURN d, collect(p)
"""
    resp = conn.execute(query)
    while resp.has_next():
        row = resp.get_next()[1]
        yield [PartModel.model_validate(r) for r in row]
