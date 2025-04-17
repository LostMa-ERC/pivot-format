from kuzu import Connection


def fetch_witness_refs(conn: Connection, id: int) -> str:
    query = f"MATCH (w:Witness) WHERE w.id = {id} RETURN w.urls"
    resp = conn.execute(query=query)
    while resp.has_next():
        refs = resp.get_next()[0]
        return refs or ""
