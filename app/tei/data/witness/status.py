from typing import Optional

from kuzu import Connection
from pydantic import BaseModel, Field


def is_witness_hypothetical(conn: Connection, id: int) -> str:
    query = f"MATCH (w:Witness) WHERE w.id = {id} RETURN w.is_unobserved"
    resp = conn.execute(query=query)
    while resp.has_next():
        refs = resp.get_next()[0]
        return refs or ""


class WitnessStatusModel(BaseModel):
    status: Optional[str] = Field(default="")
    note: Optional[str] = Field(default="")


def fetch_witness_status(conn: Connection, id: int) -> WitnessStatusModel:
    output = r"{status: w.status_witness, note: w.status_notes}"
    query = f"MATCH (w:Witness) WHERE w.id = {id} RETURN {output}"
    resp = conn.execute(query=query)
    while resp.has_next():
        data = resp.get_next()[0]
        return WitnessStatusModel.model_validate(data)
