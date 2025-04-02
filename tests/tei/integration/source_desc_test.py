import unittest

from tests.tei.integration import TEIIntegrationTest
from app.tei.builders.text import build_sourceDesc
from app.tei.parsers.text_tree import TextXMLTree


class TitleStmtBuilderGMHTest(TEIIntegrationTest):
    maxDiff = None

    def test_alternative_title(self):
        # Get the default titleStmt tree branch
        root = TextXMLTree().sourceDesc

        # Build a TEI document for a text with an alternative title
        # Current working example in real data is ID 48337
        iterate_texts = """
        MATCH (t:Text) WHERE t.alternative_names <> []
        RETURN t.id
        """
        response = self.kconn.execute(iterate_texts)
        while response.has_next():
            text_id = response.get_next()[0]
            break
        build_sourceDesc(conn=self.kconn, text_id=text_id, root=root)

        # Read the created title nodes
        nodes = root.tree.xpath("//title")
        actual = len(nodes)
        # Affirm that there are at least 2 title nodes
        # (nested in the title with the TEI namespace)
        # 1 node as @type='main' + 1 or more nodes as @type='alt' = > 2
        self.assertGreaterEqual(actual, 2)


if __name__ == "__main__":
    unittest.main()
