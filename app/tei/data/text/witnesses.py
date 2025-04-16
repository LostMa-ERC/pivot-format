from kuzu import Connection

from app.graph.edges import IS_MANIFESTATION_OF
from app.graph.nodes import Text, Witness


def fetch_witnesess_of_a_text(conn: Connection, text_id: int) -> list:
    query = f"""MATCH
        (t:{Text.label})
        <-[r:{IS_MANIFESTATION_OF.label}]
        -(w:{Witness.label})
        WHERE t.id = {text_id}
        RETURN w.id
        """
    rows = conn.execute(query).get_as_pl().rows()

    return [r[0] for r in rows]
