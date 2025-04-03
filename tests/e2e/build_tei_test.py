import unittest

import kuzu

from app.graph import build_graph_from_defaults
from app.tei.text_builder import TextDocument


class TEITest(unittest.TestCase):

    def test_text_with_author(self):
        db = kuzu.Database()
        conn = kuzu.Connection(db)
        build_graph_from_defaults(kconn=conn)

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
        doc.write(outfile="tests/authors.xml")

    def test_text_with_nested_genres(self):
        db = kuzu.Database()
        conn = kuzu.Connection(db)
        build_graph_from_defaults(kconn=conn)

        # Get a text with 2 or more genres
        query = """
        MATCH (t:Text)-[r:HAS_GENRE|HAS_PARENT *2..]->(g:Genre)
        RETURN t.id
        """
        response = conn.execute(query)
        while response.has_next():
            text_id = response.get_next()[0]
            break

        # Build a TEI document for the text
        doc = TextDocument(conn=conn, text_id=text_id)
        doc.write(outfile="tests/nested_genre.xml")


if __name__ == "__main__":
    unittest.main()
