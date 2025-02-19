from pydantic import Field

from typing import Optional, List
from .base import BaseDataModel
from app.database import DBConn

# Recusrive fields
MEMBER_OF_CYCLE = "member_of_cycle H-ID"

# Table name
TABLE_NAME = "Storyverse"


class StoryverseModel(BaseDataModel):
    id: int = Field(validation_alias="H-ID")
    preferred_name: str
    member_of_cycle: List[Optional["StoryverseModel"]] = Field(
        default=[],
        validation_alias="member_of_cycle H-ID",
        json_schema_extra={
            "model": None,
            "table": TABLE_NAME,
        },
    )
    alternative_names: Optional[str] = Field(default=None)
    described_at_URL: List[Optional[str]] = Field(default=[])

    @classmethod
    def build_nested_dict(cls, row_dict: dict, db: DBConn):
        array_of_nested_dicts = []
        for fk in row_dict[MEMBER_OF_CYCLE]:
            row = db.get_by_id(table=TABLE_NAME, hid=fk)
            nested_dict = cls.build_nested_dict(row_dict=row, db=db)
            array_of_nested_dicts.append(nested_dict)

        row_dict.update({MEMBER_OF_CYCLE: array_of_nested_dicts})

        return super().build_nested_dict(row_dict=row_dict, db=db)
