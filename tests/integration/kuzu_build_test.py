import unittest

from tests.integration import IntegrationTest

from app.builder.edges import build_all_edges
from app.builder.nodes import build_all_nodes, ALL_NODES

from app.models.nodes import Builder as NodeBuilder
from app.models.nodes.story import Story
from app.models.nodes.storyverse import Storyverse

from app.models.edges import Builder as EdgeBuilder
from app.models.edges.is_part_of_storyverse import (
    StoryIsPartOfStoryverse,
    StoryverseIsPartOfStoryverse,
)


class BuildTest(IntegrationTest):
    """Test the builder functions and methods for the Kuzu nodes and edges."""

    def test_edge_integration_builder(self):
        """Test that the integrated build-all methods work."""
        build_all_nodes(kconn=self.kconn, dconn=self.dconn)
        build_all_edges(kconn=self.kconn, dconn=self.dconn)

        for node in ALL_NODES:
            # Count the number of rows selected from the DuckDB database.
            expected = self.dconn.sql(node.duckdb_query).count("*").fetchone()[0]
            # Count the number of nodes created in the Kuzu database.
            query = f"MATCH (n:{node.name}) RETURN n"
            actual = self.kconn.execute(query).get_as_df().shape[0]
            # Assert that all the rows from the DuckDB database were inserted as
            # nodes in the Kuzu database.
            self.assertEqual(expected, actual)

    def test_edges(self):
        """Test that the edge builder works."""

        # Build the nodes for the testd edge
        node_builder = NodeBuilder(kconn=self.kconn, dconn=self.dconn)
        node_builder(node=Story)
        node_builder(node=Storyverse)

        # Build the edges
        edge_builder = EdgeBuilder(kconn=self.kconn, dconn=self.dconn)

        # Story -> Storyverse edge type
        res1 = edge_builder(edge=StoryIsPartOfStoryverse)
        edges1 = res1.get_as_df().shape[0]

        # Storyverse -> Storyverse edge type
        res2 = edge_builder(edge=StoryverseIsPartOfStoryverse)
        edges2 = res2.get_as_df().shape[0]

        # Sum of both created edges types
        expected = edges1 + edges2

        # Sum of all edges in the graph
        query = "MATCH ()-[r]->() RETURN r"
        actual = self.kconn.execute(query).get_as_df().shape[0]

        # Assert that the sum of the created edges equals the
        # sum of all edges found in the graph
        self.assertEqual(expected, actual)

    def test_nodes(self):
        """Test that the node builder works."""

        builder = NodeBuilder(kconn=self.kconn, dconn=self.dconn)

        # Story node
        res1 = builder(node=Story)
        count1 = res1.get_as_df().shape[0]

        # Storyverse node
        res2 = builder(node=Storyverse)
        count2 = res2.get_as_df().shape[0]

        # Sum of the created nodes
        expected = count1 + count2

        # Sum of all nodes in the graph
        res = self.kconn.execute("MATCH (n) RETURN n")
        actual = res.get_as_df().shape[0]

        # Assert that the sum of the created nodes equals the
        # sum of all nodes found in the graph
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
