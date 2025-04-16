from dataclasses import dataclass


@dataclass
class Selector:
    query: str
    from_node: str
    to_node: str
