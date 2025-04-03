import unittest

from app.tei.builders.text import build_encondingDesc
from app.tei.parsers.text_tree import TextXMLTree
from tests.tei.integration import TEIIntegrationTest


class TextEncodingTest(TEIIntegrationTest):
    maxDiff = None

    def test_genre_parentage(self):
        # Get the default encodingDesc tree branch
        root = TextXMLTree().encodingDesc

        # Fetch and encode the text's nested genres
        build_encondingDesc(conn=self.kconn, root=root)

        from lxml import etree

        etree.indent(root.genre_taxonomy)
        print(etree.tostring(root.genre_taxonomy, encoding="utf-8").decode())


if __name__ == "__main__":
    unittest.main()
