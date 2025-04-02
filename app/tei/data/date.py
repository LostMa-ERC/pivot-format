from typing import Optional
from datetime import date
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
    @property
    def cert(self) -> str:
        if self.est_cert:
            return self.est_cert
        elif self.cert_freetext and "probable" in self.cert_freetext.lower():
            return "probable"
        elif self.cert_freetext and "unlikely" in self.cert_freetext.lower():
            return "unlikely"
        elif self.cert_freetext and "very likely" in self.cert_freetext.lower():
            return "veryLikely"
        elif self.cert_freetext and "certain" in self.cert_freetext.lower():
            return "certain"
        else:
            return ""

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
