from kuzu import Connection

from app.graph.nodes import Text


def fetch_title(conn: Connection, id: int) -> str:
    """Methods to fetch and format metadata for the text title."""

    query = f"""
MATCH (t:{Text.node_label}) WHERE t.id = {id} RETURN t.name
"""
    response = conn.execute(query)
    while response.has_next():
        return response.get_next()[0]
