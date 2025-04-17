from datetime import date

from kuzu import Connection
from pydantic import BaseModel, Field, computed_field


class WitnessOrigin(BaseModel):
    freetext: str | None = Field(default="")
    cert_heurist: str | None = Field(default=None)
    cert_lostma: str | None = Field(default=None)
    estMinDate: date | None = Field(default=None)
    estMaxDate: date | None = Field(default=None)
    timestamp_year: date | None = Field(default=None)
    timestamp_circa: bool | None = Field(default=None)

    @computed_field
    def attribs(self) -> dict:
        if self.cert_heurist:
            cert = self.cert_heurist
        else:
            cert = self.cert_lostma or ""
        if self.timestamp_year:
            return {"when": str(self.timestamp_year), "type": "circa", "cert": cert}
        elif self.estMinDate and self.estMaxDate:
            return {
                "notBefore": str(self.estMinDate),
                "notAfter": str(self.estMaxDate),
                "cert": cert,
            }
        else:
            return {}


def fetch_witness_origin_date(conn: Connection, witness_id: int):
    output = r"""{
    freetext: w.creation_date_freetext,
    cert_heurist: w.creation_date.est_cert,
    cert_lostma: w.creation_date_certainty,
    estMinDate: w.creation_date.est_min,
    estMaxDate: w.creation_date.est_max,
    timestamp_year: w.creation_date.timestamp_year,
    timestamp_type: w.creation_date.timestamp_type
}"""
    query = f"MATCH (w:Witness) WHERE w.id = {witness_id} RETURN {output}"
    resp = conn.execute(query=query)
    while resp.has_next():
        data = resp.get_next()[0]
        return WitnessOrigin.model_validate(data)
