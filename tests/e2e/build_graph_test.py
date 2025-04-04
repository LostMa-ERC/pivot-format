import unittest

import kuzu

from app.cli.build_commands.build_graph import build_graph_from_defaults


class BuildGraphTest(unittest.TestCase):

    def test_command(self):
        db = kuzu.Database()
        conn = kuzu.Connection(db)
        with self.assertNoLogs():
            build_graph_from_defaults(kconn=conn)
