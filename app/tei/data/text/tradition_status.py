from typing import Optional

from kuzu import Connection
from pydantic import BaseModel, Field, computed_field

from app.graph.edges import HAS_STATUS
from app.graph.nodes import Text, TraditionStatus


class StatusModel(BaseModel):
    id: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default="")
    code: Optional[str] = Field(default="")
    description: Optional[str] = Field(default="")
    url: Optional[str] = Field(default="")

    @computed_field
    @property
    def xml_id(self) -> str:
        if self.id:
            return f"tradition{self.name.capitalize()}"
        else:
            return ""


def fetch_text_tradition_status(conn: Connection, text_id: int) -> StatusModel | None:
    query = f"""
    MATCH (t:{Text.label})-[r:{HAS_STATUS.label}]
        ->(s:{TraditionStatus.label})
    WHERE t.id = {text_id} RETURN s
    """
    response = conn.execute(query)
    while response.has_next():
        row = response.get_next()[0]
        return StatusModel.model_validate(row)


def fetch_all_tradition_statuses(conn: Connection) -> list[StatusModel]:
    query = f"MATCH (ts:{TraditionStatus.label}) RETURN ts"
    response = conn.execute(query)
    statuses = []
    while response.has_next():
        row = response.get_next()[0]
        data = StatusModel.model_validate(row)
        statuses.append(data)
    return statuses
