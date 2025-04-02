import unittest

from app.graph.edges.has_genre import TextHasGenre
from app.graph.edges.has_parent_genre import GenreHasParent

from tests.tei.integration import TEIIntegrationTest
from app.tei.parsers.text_tree import TextXMLTree
from app.tei.builders.text import build_encondingDesc


class TextEncodingTest(TEIIntegrationTest):
    maxDiff = None

    def test_genre_parentage(self):
        # Get the default encodingDesc tree branch
        root = TextXMLTree().encodingDesc

        # Get a text with nested genres
        iterate_texts = f"""
        MATCH path=(g:Genre)
    <-[r:{TextHasGenre.table_name}|{GenreHasParent.table_name} *1..]
    -(t:Text)
        WHERE LENGTH(r) > 1
        RETURN t.id
        """
        response = self.kconn.execute(iterate_texts)
        while response.has_next():
            text_id = response.get_next()[0]
            break

        # Fetch and encode the text's nested genres
        build_encondingDesc(conn=self.kconn, text_id=text_id, root=root)

        # Count the created nodes, nested under <category xml:id="genre">
        nodes = root.genre_taxonomy.findall(".//category")
        self.assertGreaterEqual(len(nodes), 2)


if __name__ == "__main__":
    unittest.main()
