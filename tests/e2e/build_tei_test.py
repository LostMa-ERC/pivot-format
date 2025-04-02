import kuzu
import unittest
import random

from app.graph import build_graph_from_defaults
from app.tei.text_builder import TextTEIBuilder


class TEITest(unittest.TestCase):
    def test(self):
        db = kuzu.Database()
        conn = kuzu.Connection(db)
        build_graph_from_defaults(kconn=conn)
        builder = TextTEIBuilder(conn=conn)

        # Get a random text node
        offset = random.randint(1, 5)
        query = f"""MATCH (t:Text)-[r:HAS_GENRE]-(g:Genre)
        WHERE t.alternative_names <> []
        AND g.name <> "Other"
        RETURN t.id SKIP {offset} LIMIT 1"""
        response = conn.execute(query)
        while response.has_next():
            text_id = response.get_next()[0]

        # Build a TEI document for the text
        _ = builder(text_id=text_id)
        builder.write(outfile="example.xml")


if __name__ == "__main__":
    unittest.main()
