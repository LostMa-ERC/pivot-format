from typing import Optional

from kuzu import Connection
from pydantic import BaseModel, Field, computed_field

from app.graph.edges import IS_INSCRIBED_ON


class DocumentModel(BaseModel):
    id: int
    shelfmark: Optional[str] = Field(default=None)
    collection: Optional[str] = Field(default=None)
    invented_label: Optional[str] = Field(default=None)
    is_hypothetical: bool
    old_shelfmark: list[Optional[str]] = Field(default=[])
    urls: list[Optional[str]] = Field(default=[])
    catalogue_record: Optional[str] = Field(default=None)
    ark: Optional[str] = Field(default=None)

    @computed_field
    @property
    def xml_id(self) -> str:
        return f"document_{self.id}"


def get_document_from_part(conn: Connection, part_id: int) -> DocumentModel:
    query = f"""MATCH (a:Part)-[:{IS_INSCRIBED_ON.label}]->(b:Document)
    WHERE a.id = {part_id}
    RETURN b"""
    resp = conn.execute(query)
    while resp.has_next():
        data = resp.get_next()[0]
        return DocumentModel.model_validate(data)
