import unittest
import kuzu

from app.graph import build_graph_from_defaults
from app.tei.text_builder import TextTEIBuilder


class TEIIntegrationTest(unittest.TestCase):
    def setUp(self):
        db = kuzu.Database()
        self.kconn = kuzu.Connection(db)
        build_graph_from_defaults(kconn=self.kconn)

        self.builder = TextTEIBuilder(conn=self.kconn)
        return super().setUp()
