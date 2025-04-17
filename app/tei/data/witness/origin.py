from kuzu import Connection

from app.tei.data.date import DateModel


def fetch_witness_origin_date(conn: Connection, witness_id: int) -> DateModel:
    query = f"MATCH (w:Witness) WHERE w.id = {witness_id} RETURN w"
    resp = conn.execute(query=query)
    while resp.has_next():
        data = resp.get_next()[0]

    date_metadata = {}
    if data["creation_date"]:
        date_metadata.update(data["creation_date"])
    date_metadata.update({"date_freetext": data["creation_date_freetext"]})
    date_metadata.update({"cert_freetext": data["creation_date_certainty"]})

    return DateModel.model_validate(date_metadata)
