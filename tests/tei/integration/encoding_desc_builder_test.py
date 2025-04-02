import unittest

from app.graph.edges.has_genre import TextHasGenre
from app.graph.edges.has_parent_genre import GenreHasParent


from tests.tei.integration import TEIIntegrationTest


class TextBuilderGMHTest(TEIIntegrationTest):
    maxDiff = None

    def test_genre_parentage(self):
        # Build a TEI document for a text with a nested genre
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
        self.builder(text_id=text_id)
        # Read the created genre nodes


if __name__ == "__main__":
    unittest.main()
