from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, computed_field


class DateModel(BaseModel):
    start_earliest: Optional[date] = Field(default=None)
    start_latest: Optional[date] = Field(default=None)
    end_earliest: Optional[date] = Field(default=None)
    end_latest: Optional[date] = Field(default=None)
    timestamp_year: Optional[date] = Field(default=None)
    est_min: Optional[date] = Field(default=None)
    est_max: Optional[date] = Field(default=None)
    est_cert: Optional[str] = Field(default=None)
    date_freetext: Optional[str] = Field(default=None)
    cert_freetext: Optional[str] = Field(default=None)

    @computed_field
    def attribs(self) -> dict:
        if self.timestamp_year:
            return {
                "when": str(self.timestamp_year),
                "type": "circa",
                "cert": self.cert,
            }
        elif self.est_min and self.est_max:
            return {
                "notBefore": str(self.est_min),
                "notAfter": str(self.est_max),
                "cert": self.cert,
            }
        else:
            return {}

    @computed_field
    @property
    def cert(self) -> str:
        if self.est_cert:
            cert = self.est_cert
            # 0=>"Unknown",
            # 1=>"Attested",
            # 2=>"Conjecture",
            # 3=>"Measurement"
            if cert.lower() == "attested":
                return "low"
            elif cert.lower() == "conjecture":
                return "medium"
            elif cert.lower() == "measurement":
                return "high"
            else:
                return "unknown"

        elif self.cert_freetext and "probable" in self.cert_freetext.lower():
            return "medium"
        elif self.cert_freetext and "unlikely" in self.cert_freetext.lower():
            return "low"
        elif self.cert_freetext and "very likely" in self.cert_freetext.lower():
            return "high"
        elif self.cert_freetext and "certain" in self.cert_freetext.lower():
            return "high"
        else:
            return "unknown"

    @computed_field
    @property
    def notBefore(self) -> str:
        if self.est_min:
            return str(self.est_min)
        elif self.timestamp_year:
            return str(self.est_min)
        else:
            return ""

    @computed_field
    @property
    def notAfter(self) -> str:
        if self.est_max:
            return str(self.est_max)
        elif self.timestamp_year:
            return str(self.timestamp_year)
        else:
            return ""
