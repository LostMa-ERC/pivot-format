from typing import Annotated, Optional

from kuzu import Connection
from pydantic import AfterValidator, BaseModel, Field, computed_field


def convert_illustration_quantitfication(value: str) -> str:
    if value == "none":
        return "0"
    elif value == "more than one":
        return ">1"
    elif value == "one":
        return "1"
    else:
        return ""


class PhysDescModel(BaseModel):
    id: int
    material: str
    form: str
    folio_size_width: Optional[str] = Field(default="")
    folio_size_height: Optional[str] = Field(default="")
    estimated_folio_size_height: Optional[str] = Field(default=None)
    estimated_folio_size_width: Optional[str] = Field(default=None)
    has_decorations: list[Optional[str]] = Field(default=[])
    amount_of_illustrations: Annotated[
        str, AfterValidator(convert_illustration_quantitfication)
    ]
    number_of_columns: Optional[str] = Field(default="")
    script_type: Optional[str] = Field(default="")
    subscript_type: Optional[str] = Field(default=None)
    number_of_lines_in_writing_area: Optional[str] = Field(default="")
    above_top_line: Optional[str] = Field(default="")

    @computed_field
    @property
    def xml_id(self) -> str:
        return f"physDesc_{self.id}"


def fetch_physDesc(conn: Connection, part_id: int) -> PhysDescModel | None:
    query = f"""
MATCH (p:Part)-[:HAS_DESCRIPTION]->(d:PhysDesc)
WHERE p.id = {part_id}
RETURN d
"""
    resp = conn.execute(query)
    while resp.has_next():
        data = resp.get_next()[0]
        return PhysDescModel.model_validate(data)
