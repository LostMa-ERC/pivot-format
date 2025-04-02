import unittest
import kuzu

from app.graph import build_graph_from_defaults
from app.tei.parsers.text_tree import TextXMLTree


class TEIIntegrationTest(unittest.TestCase):
    def setUp(self):
        db = kuzu.Database()
        self.kconn = kuzu.Connection(db)
        build_graph_from_defaults(kconn=self.kconn)
        self.tree = TextXMLTree
        return super().setUp()
