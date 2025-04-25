import json
import shutil
import unittest
from pathlib import Path

import duckdb
import kuzu

from app import HEURIST_DB
from app.sql_to_graph import (
    create_kuzu_database_from_config,
    create_neo4j_database_from_config,
    dump_relational_database_to_config,
    get_config,
)
from neo4j import GraphDatabase


class TestSQLtoGraph(unittest.TestCase):
    dir = Path(__file__).parent.joinpath("tmp")

    def setUp(self):
        self.dconn = duckdb.connect(HEURIST_DB, read_only=True)
        self.dir.mkdir(exist_ok=True)
        self.conf = dump_relational_database_to_config(output_dir=self.dir)
        return super().setUp()

    def tearDown(self):
        if self.dir.is_dir():
            shutil.rmtree(self.dir)
        return super().tearDown()

    def test_json_writing(self):
        config_file = get_config(dir=self.dir)
        with open(config_file) as f:
            conf = json.load(f)
        self.assertGreater(len(conf["nodes"]), 5)

    def test_kuzu_parsing(self):
        db = kuzu.Database()
        kconn = kuzu.Connection(db)
        create_kuzu_database_from_config(config=self.conf, conn=kconn)

    def test_neo4j_parsing(self):
        URI = "neo4j://localhost:7687"
        AUTH = ("neo4j", "password")
        with GraphDatabase.driver(uri=URI, auth=AUTH) as driver:
            if driver.verify_connectivity() is not None:
                unittest.skip("No Neo4j connection")
            create_neo4j_database_from_config(config=self.conf, driver=driver)


if __name__ == "__main__":
    unittest.main()
