from kuzu import Connection

from app.tei.data.person import PersonModel
from app.graph.edges.is_attributed_to import IsAttributedTo


def fetch_authors(conn: Connection, id: int) -> list[PersonModel]:
    query = f"""
MATCH (a:Text)
-[r:{IsAttributedTo.table_name}]
->(p:Person) WHERE a.id = {id} RETURN p
"""
    response = conn.execute(query)
    matches = []
    while response.has_next():
        result = response.get_next()[0]
        data = PersonModel.model_validate(result)
        matches.append(data)
    return matches
