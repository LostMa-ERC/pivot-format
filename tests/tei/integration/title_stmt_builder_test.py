import unittest

from lxml import etree

from tests.tei.integration import TEIIntegrationTest
from app.tei.builders.text import build_titleStmt
from app.tei.parsers.text_tree import TextXMLTree


class TitleStmtBuilderGMHTest(TEIIntegrationTest):
    maxDiff = None

    def test_gmh_respStmt(self):
        # Get the default titleStmt tree branch
        root = TextXMLTree().titleStmt

        # Build a TEI document for a Middle High German text
        iterate_texts = """
        MATCH (t:Text)-[r:HAS_LANGAUGE]-(l:Language)
        WHERE l.code = 'gmh'
        RETURN t.id
        """
        response = self.kconn.execute(iterate_texts)
        while response.has_next():
            text_id = response.get_next()[0]
            break

        build_titleStmt(conn=self.kconn, text_id=text_id, root=root)

        # Read the created respStmt branch
        node = root.respStmt
        etree.indent(node)
        actual = etree.tostring(node, encoding="utf-8").decode().strip()

        # Affirm the created branch is what is expected
        expected = """\
<respStmt xmlns="http://www.tei-c.org/ns/1.0">
  <name>Mike Kestemont</name>
  <resp>data entry and proof correction</resp>
  <name>Kelly Christensen</name>
  <resp>conversion of metadata to TEI markup</resp>
  <name>Théo Moins</name>
  <resp>conversion of text to TEI markup</resp>
</respStmt>"""
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
