import unittest

import duckdb

from app import HEURIST_DB
from app.sql_to_graph.dump_db import NODES


class Test(unittest.TestCase):
    def setUp(self):
        self.conn = duckdb.connect(HEURIST_DB)
        return super().setUp()

    def test_sql_query(self):
        valid_tables = 0
        for sql_entity, _ in NODES:
            try:
                original = self.conn.table(sql_entity.table_name)
            except duckdb.CatalogException:
                # Table is an inenvted edge table, not in original DB
                continue
            valid_tables += 1

            original_count = original.count("*").fetchone()[0]
            result = self.conn.sql(query=sql_entity.query)
            result_count = result.count("*").fetchone()[0]
            self.assertEqual(original_count, result_count)

        # Make sure not all the tables were skipped
        self.assertGreaterEqual(valid_tables, 5)


if __name__ == "__main__":
    unittest.main()
