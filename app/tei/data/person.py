from typing import Optional
from pydantic import BaseModel, Field, computed_field


class PersonModel(BaseModel):
    id: int
    family_name: Optional[str] = Field(default=None)
    given_name: Optional[str] = Field(default=None)
    alternative_names: list[Optional[str]] = Field(default=[])
    urls: list[Optional[str]] = Field(default=[])

    @computed_field
    @property
    def xml_id(self) -> str:
        return f"person_{self.id}"

    @computed_field
    @property
    def full_name(self) -> str:
        if self.given_name and self.family_name:
            return f"{self.given_name} {self.family_name}"
        elif self.given_name:
            return self.given_name
        elif self.family_name:
            return self.family_name
        return ""
