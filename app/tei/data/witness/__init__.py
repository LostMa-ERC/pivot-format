from pydantic import BaseModel, computed_field


def make_xml_id(id: int) -> str:
    return f"witness_{id}"


class WitnessModel(BaseModel):
    id: int

    @computed_field
    @property
    def xml_id(self) -> str:
        return make_xml_id(id=self.id)
