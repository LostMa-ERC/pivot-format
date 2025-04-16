import unittest

from app.graph.edges import IS_MANIFESTATION_OF
from app.tei.text_builder import TextDocument
from tests import GraphDepTest


class TEITest(GraphDepTest):

    def test_text_with_author(self):
        # Get a text with 1 or more authors, who have a reference URL
        query = """
        MATCH (t:Text)-[r:IS_ATTRIBUTED_TO]->(p:Person)
        WHERE p.urls <> []
        RETURN t.id
        """
        response = self.conn.execute(query)
        while response.has_next():
            text_id = response.get_next()[0]
            break

        # Build a TEI document for the text
        doc = TextDocument(conn=self.conn, text_id=text_id)
        doc.write(outfile="tests/authors.xml")

    def test_text_with_nested_genres(self):
        # Get a text with 2 or more genres
        query = """
        MATCH (t:Text)-[r:HAS_GENRE|HAS_PARENT *2..]->(g:Genre)
        RETURN t.id
        """
        response = self.conn.execute(query)
        while response.has_next():
            text_id = response.get_next()[0]
            break

        # Build a TEI document for the text
        doc = TextDocument(conn=self.conn, text_id=text_id)
        doc.write(outfile="tests/nested_genre.xml")

    def test_text_with_multiple_witnesses(self):
        # Get a text with 2 or more witnesses
        query = f"""
        MATCH (t:Text)<-[r:{IS_MANIFESTATION_OF.label}]-(w:Witness)
        WITH t as text, count(w) as n_wits
        WHERE n_wits > 3
        RETURN text.id
        """
        response = self.conn.execute(query)
        while response.has_next():
            text_id = response.get_next()[0]
            break

        # Build a TEI document for the text
        doc = TextDocument(conn=self.conn, text_id=text_id)
        doc.write(outfile="tests/multiple_witnesses.xml")


if __name__ == "__main__":
    unittest.main()
