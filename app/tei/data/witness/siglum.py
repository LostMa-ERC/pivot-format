from kuzu import Connection


def fetch_witness_siglum(conn: Connection, id: int) -> str:
    query = f"MATCH (w:Witness) WHERE w.id = {id} RETURN w.siglum"
    resp = conn.execute(query=query)
    while resp.has_next():
        siglum = resp.get_next()[0]
        return siglum or ""
