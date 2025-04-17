from typing import Generator

from kuzu import Connection

from app.graph.edges import IS_INSCRIBED_ON, IS_OBSERVED_ON

from .document import DocumentModel
from .part import PartModel


def yield_from_witness_parts_aggregated_by_doc(
    conn: Connection,
    witness_id: int,
) -> Generator[tuple[DocumentModel, list[PartModel]], None, None]:
    query = f"""
MATCH (w:Witness)-[:{IS_OBSERVED_ON.label}]-(p:Part)
    -[:{IS_INSCRIBED_ON.label}]-(d:Document)
WHERE w.id = {witness_id}
RETURN d, collect(p)
"""
    resp = conn.execute(query)
    while resp.has_next():
        data = resp.get_next()
        ms = DocumentModel.model_validate(data[0])
        parts = [PartModel.model_validate(p) for p in data[1]]
        yield (ms, parts)
