import kuzu
import unittest

from app.graph import build_graph_from_defaults
from app.tei.text_builder import TextDocument


class TEITest(unittest.TestCase):
    def test(self):
        db = kuzu.Database()
        conn = kuzu.Connection(db)
        build_graph_from_defaults(kconn=conn)

        # Get a random text node
        # import random
        # offset = random.randint(1, 5)
        # query = f"""MATCH (t:Text)-[r:HAS_GENRE]-(g:Genre)
        # WHERE t.alternative_names <> []
        # AND g.name <> "Other"
        # RETURN t.id SKIP {offset} LIMIT 1"""

        # Get a text with 1 or more authors, who have a reference URL
        query = """
        MATCH (t:Text)-[r:IS_ATTRIBUTED_TO]->(p:Person)
        WHERE p.urls <> []
        RETURN t.id
        """
        response = conn.execute(query)
        while response.has_next():
            text_id = response.get_next()[0]
            break

        # Build a TEI document for the text
        doc = TextDocument(conn=conn, text_id=text_id)
        doc.write(outfile="example.xml")


if __name__ == "__main__":
    unittest.main()
