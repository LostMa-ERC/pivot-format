from dataclasses import dataclass, field

from .selector import Selector


@dataclass
class Relation:
    alias: str
    selectors: list[Selector]
    property_names: list[str] = field(default_factory=list)
