import unittest

from app.tei.builders.text import build_encondingDesc
from app.tei.parsers.text_tree import TextXMLTree
from app.tei.text_builder import TextDocument
from tests.tei.integration import TEIIntegrationTest


class TextEncodingTest(TEIIntegrationTest):
    maxDiff = None

    def test_build_with_premade_encoding_desc(self):
        # Modify the default encodingDesc tree branch with the standard encodingDesc
        node = build_encondingDesc(conn=self.kconn, root=TextXMLTree().encodingDesc)

        # Instantiate the a text's TEI document with the encoding desc
        doc = TextDocument(conn=self.kconn, text_id=512, encodingDesc_node=node)

        # Assert that there are 4 category nodes in the tradition taxonomy
        tree = doc.parser.encodingDesc.tradition_status_taxonomy
        actual = len(tree.findall("category"))
        self.assertEqual(actual, 4)

    def test_build_without_encoding_desc(self):
        # Instantiate the a text's TEI document with the encoding desc
        doc = TextDocument(conn=self.kconn, text_id=512)
        doc.write("example.xml")

        # Assert that there are 4 category nodes in the tradition taxonomy
        tree = doc.parser.encodingDesc.tradition_status_taxonomy
        actual = len(tree.findall("category"))
        self.assertEqual(actual, 4)


if __name__ == "__main__":
    unittest.main()
