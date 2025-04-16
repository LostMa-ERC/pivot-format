import shutil
import unittest
from pathlib import Path

import kuzu

from app.sql_to_graph import (
    create_kuzu_database_from_config,
    dump_relational_database_to_config,
)
from app.tei.parsers.text_tree import TextXMLTree


class GraphDepTest(unittest.TestCase):
    tmp_dir = Path(__file__).parent.joinpath("tmp")

    def setUp(self):
        conf = dump_relational_database_to_config(output_dir=self.tmp_dir)

        db = kuzu.Database()
        self.conn = kuzu.Connection(db)
        create_kuzu_database_from_config(config=conf, conn=self.conn)

        self.tree = TextXMLTree
        return super().setUp()

    def tearDown(self):
        if self.tmp_dir.is_dir():
            shutil.rmtree(self.tmp_dir)
        return super().tearDown()
