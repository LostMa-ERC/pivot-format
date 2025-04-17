from typing import Optional

from kuzu import Connection
from pydantic import BaseModel, Field, computed_field

from app.graph.edges import IS_INSCRIBED_ON, LOCATION


class RepositoryModel(BaseModel):
    id: int
    name: str
    alternative_names: list[Optional[str]] = Field(default=[])
    viaf: Optional[str] = Field(default=None)
    isni: Optional[str] = Field(default=None)
    biblissima_identifier: Optional[str] = Field(default=None)
    website: Optional[str] = Field(default=None)

    @computed_field
    @property
    def xml_id(self) -> str:
        return f"respository_{self.id}"


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


class CountryModel(BaseModel):
    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    code: str | None = Field(default="")


class PlaceModel(BaseModel):
    id: int
    name: str
    region: str | None = Field(default=None)
    country: CountryModel | None = Field(default=None)

    @computed_field
    @property
    def xml_id(self) -> str:
        return f"place_{self.id}"


class CompiledDocumentModel(BaseModel):
    document: DocumentModel
    repository: RepositoryModel | None = Field(default=None)
    place: PlaceModel | None = Field(default=None)


def get_document_from_part(conn: Connection, part_id: int) -> CompiledDocumentModel:
    # Query for when the part is in a real document, with a location
    query = f"""MATCH (pt:Part)-[:{IS_INSCRIBED_ON.label}]->(d:Document)
    -[:{LOCATION.label}]->(r:Repository)-[:{LOCATION.label}]->(pl:Place)
    -[:{LOCATION.label}]->(c:Country)
    WHERE pt.id = {part_id}
    RETURN d, r, pl, c"""
    resp = conn.execute(query)
    while resp.has_next():
        row = resp.get_next()
        d, r, pl, c = row
        pl.update({"country": c})

        repo = RepositoryModel.model_validate(r)
        doc = DocumentModel.model_validate(d)
        place = PlaceModel.model_validate(pl)

        return CompiledDocumentModel(document=doc, repository=repo, place=place)

    # Query for when the part is in a document without a location registered
    if not resp.has_next():
        query = f"""MATCH (pt:Part)-[:{IS_INSCRIBED_ON.label}]->(d:Document)
        WHERE pt.id = {part_id}
        RETURN d
        """
        resp = conn.execute(query)
        while resp.has_next():
            d = resp.get_next()[0]

        doc = DocumentModel.model_validate(d)

        return CompiledDocumentModel(document=doc)
