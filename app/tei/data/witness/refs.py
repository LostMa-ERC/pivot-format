from kuzu import Connection


def fetch_witness_refs(conn: Connection, id: int) -> list:
    query = f"MATCH (w:Witness) WHERE w.id = {id} RETURN w.urls"
    resp = conn.execute(query=query)
    while resp.has_next():
        refs = resp.get_next()[0]
        return refs or []


def fetch_document_refs(conn: Connection, id: int) -> list:
    query = f"MATCH (d:Document) WHERE d.id = {id} RETURN d.urls"
    resp = conn.execute(query=query)
    while resp.has_next():
        refs = resp.get_next()[0]
        return refs or []
