from kuzu import Connection

from app.graph.nodes import Text
from app.tei.data.date import DateModel


def fetch_creation_date(conn: Connection, id: int) -> DateModel:
    # Get the rich date metadata
    query = f"MATCH (t:{Text.node_label}) WHERE t.id = {id} RETURN t"
    response = conn.execute(query)
    while response.has_next():
        text = response.get_next()[0]

    date_metadata = {}
    if text["creation_date"]:
        date_metadata.update(text["creation_date"])
    date_metadata.update({"date_freetext": text["creation_date_freetext"]})
    date_metadata.update({"cert_freetext": text["creation_date_certainty"]})

    return DateModel.model_validate(date_metadata)
