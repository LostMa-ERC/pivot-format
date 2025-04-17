from typing import Optional

from kuzu import Connection
from pydantic import BaseModel, Field, computed_field


class ScriptaModel(BaseModel):
    id: int
    code: str = Field(validation_alias="name")
    description: str
    urls: list[Optional[str]] = Field(default=[])

    @computed_field
    @property
    def xml_id(self) -> str:
        return f"scripta_{self.id}"


def fetch_witness_scripta(conn: Connection, id: int) -> ScriptaModel | None:
    query = f"MATCH (w:Witness)-[:HAS_SCRIPT]->(s:Scripta) WHERE w.id = {id} RETURN s"
    resp = conn.execute(query=query)
    while resp.has_next():
        data = resp.get_next()[0]
        return ScriptaModel.model_validate(data)


def fetch_text_scripta(conn: Connection, id: int) -> ScriptaModel | None:
    query = f"MATCH (t:Text)-[:HAS_SCRIPT]->(s:Scripta) WHERE t.id = {id} RETURN s"
    resp = conn.execute(query=query)
    while resp.has_next():
        data = resp.get_next()[0]
        return ScriptaModel.model_validate(data)
