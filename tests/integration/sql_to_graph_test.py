import json
import shutil
import unittest
from pathlib import Path

import duckdb
import kuzu

from app import HEURIST_DB
from app.sql_to_graph import (
    create_kuzu_database_from_config,
    dump_relational_database_to_config,
    get_config,
)


class TestSQLtoGraph(unittest.TestCase):
    dir = Path(__file__).parent.joinpath("tmp")

    def setUp(self):
        self.dconn = duckdb.connect(HEURIST_DB, read_only=True)
        db = kuzu.Database()
        self.kconn = kuzu.Connection(db)
        self.dir.mkdir(exist_ok=True)
        return super().setUp()

    def tearDown(self):
        if self.dir.is_dir():
            shutil.rmtree(self.dir)
        return super().tearDown()

    def test(self):
        _ = dump_relational_database_to_config(output_dir=self.dir)

        config_file = get_config(dir=self.dir)
        with open(config_file) as f:
            conf = json.load(f)

        create_kuzu_database_from_config(config=conf, conn=self.kconn)


if __name__ == "__main__":
    unittest.main()
