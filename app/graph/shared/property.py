from dataclasses import dataclass

from .types import Type


@dataclass
class Property:
    name: str
    type: Type
