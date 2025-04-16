from kuzu import Connection

from app.graph.nodes import Text


def fetch_literary_form_of_a_text(conn: Connection, text_id: int) -> str:
    query = f"""
MATCH (t:{Text.label}) WHERE t.id = {text_id} RETURN t.form
"""
    response = conn.execute(query)
    while response.has_next():
        data = response.get_next()[0]
        if not data or data == "":
            return "unknown"
        else:
            return data
