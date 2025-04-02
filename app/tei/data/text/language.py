from kuzu import Connection
from typing import Optional

from pydantic import BaseModel, Field, computed_field


class LanguageModel(BaseModel):
    id: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default="")
    code: Optional[str] = Field(default="")
    description: Optional[str] = Field(default="")
    url: Optional[str] = Field(default="")

    @computed_field
    @property
    def xml_id(self) -> str:
        if self.id:
            return f"lang_{self.id}"
        else:
            return ""


def fetch_language(conn: Connection, id: int) -> LanguageModel:
    result = {}
    query = f"""
MATCH (t:Text)-[r:HAS_LANGAUGE]-(l:Language) WHERE t.id = {id} RETURN l
"""
    response = conn.execute(query)
    while response.has_next():
        result = response.get_next()[0]
        break
    return LanguageModel.model_validate(result)
