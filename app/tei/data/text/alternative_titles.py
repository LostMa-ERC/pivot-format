from typing import Optional

from kuzu import Connection

from app.graph.nodes import Text


def fetch_alternative_title(conn: Connection, id: int) -> list[Optional[str]]:
    """Methods to fetch and format metadata for the text's
    alternative titles."""

    query = f"""
MATCH (t:{Text.label}) WHERE t.id = {id} RETURN t.alternative_names
"""
    response = conn.execute(query)
    while response.has_next():
        return response.get_next()[0]
