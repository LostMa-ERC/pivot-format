import unittest
from app.graph.nodes import create_all_nodes
from app import HEURIST_DB
import duckdb
import kuzu
from datetime import date


class Test(unittest.TestCase):
    def test(self):
        db = kuzu.Database()
        kconn = kuzu.Connection(db)
        dconn = duckdb.connect(HEURIST_DB)
        create_all_nodes(kconn=kconn, dconn=dconn)
        query = (
            "MATCH (n:Text) WHERE n.creation_date.start_earliest IS NOT NULL "
            "RETURN n.creation_date.start_earliest"
        )
        response = kconn.execute(query)
        # Make sure the query returned results
        self.assertGreater(response.get_num_tuples(), 1)
        # Make sure every result is a date
        while response.has_next():
            result = response.get_next()[0]
            self.assertIsInstance(result, date)


if __name__ == "__main__":
    unittest.main()
