from typing import List
from dataclasses import dataclass, field

from .from_to_relation import FromToEdgeRelation


@dataclass
class Edge:
    table_name: str
    relations: List[FromToEdgeRelation]
    properties: List = field(default_factory=list)
