import unittest
import shutil

from pathlib import Path

from app.cli.build_commands.build_graph import build_graph
from app import KUZU_DB


class BuildGraphTest(unittest.TestCase):
    def setUp(self):
        if Path(KUZU_DB).is_dir():
            shutil.rmtree(KUZU_DB)
        return super().setUp()

    def test_command(self):
        with self.assertNoLogs():
            build_graph()

    def tearDown(self):
        shutil.rmtree(KUZU_DB)
        return super().tearDown()
