import unittest

from app.graph import Property, Type
from app.graph.nodes.core import Node
from neo4j import GraphDatabase

TestNode = Node(
    label="TestNode",
    pk="id",
    properties=[
        Property(name="id", type=Type.int),
        Property(name="title", type=Type.string),
    ],
)


class KuzuCypherTest(unittest.TestCase):
    def test_create_stmt(self):
        actual = TestNode.kuzu_create_table_stmt
        expected = "CREATE NODE TABLE TestNode (id INT, title STRING, PRIMARY KEY(id));"
        self.assertEqual(actual, expected)


class Neo4jCypherTest(unittest.TestCase):

    def test_create_multiple_nodes_stmt(self):
        actual = TestNode.neo4j_create_multiple_nodes_stmt
        expected = """\
UNWIND $data AS properties
CREATE (n:TestNode)
SET n = properties
RETURN n
"""
        self.assertEqual(actual, expected)

    def test_constraint_stmt(self):
        actual = TestNode.neo4j_node_constraint
        expected = """\
CREATE CONSTRAINT TestNode_primary_key IF NOT EXISTS FOR (n:TestNode) \
REQUIRE n.id IS UNIQUE"""
        self.assertEqual(actual, expected)


class Neo4jEfficacyTest(unittest.TestCase):
    def setUp(self):
        URI = "neo4j://localhost:7687"
        AUTH = ("neo4j", "password")
        self.driver = GraphDatabase.driver(uri=URI, auth=AUTH)
        if self.driver.verify_connectivity() is not None:
            unittest.skip("No Neo4j connection")
        # Reset the database, removing any nodes and the TestNode's constraint
        self.driver.execute_query("MATCH (n) DETACH DELETE n")
        self.driver.execute_query("DROP CONSTRAINT TestNode_primary_key IF EXISTS")
        return super().setUp()

    def tearDown(self):
        self.driver.close()
        return super().tearDown()

    def test_create_statement_with_multiple_nodes(self):
        self.driver.execute_query(TestNode.neo4j_node_constraint)

        stmt = TestNode.neo4j_create_multiple_nodes_stmt
        data = {
            "data": [
                {"id": 1, "title": "First node"},
                {"id": 2, "title": "Second node"},
            ]
        }
        records, summary, _ = self.driver.execute_query(stmt, parameters_=data)

        # Assert that 2 (and only 2) nodes are in the database
        self.assertEqual(len(records), 2)
        self.assertEqual(summary.counters.nodes_created, 2)

        # Assert that the created TestNodes have the expected metadata properties
        for result, expected in zip(records, data["data"]):
            actual = result.data()["n"]
            self.assertDictEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
