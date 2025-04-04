from dataclasses import dataclass, field
from typing import List

from .from_to_relation import FromToEdgeRelation


@dataclass
class Edge:
    edge_label: str
    relations: List[FromToEdgeRelation]
    properties: List = field(default_factory=list)
