import unittest
from pprint import pprint

from app.tei.data.witness.msDesc_and_msParts import (
    yield_from_witness_parts_aggregated_by_doc,
)
from tests import GraphDepTest


class Test(GraphDepTest):
    def test(self):
        # Get a witness ID
        query = "MATCH (w:Witness)-[r:IS_OBSERVED_ON]->(p:Part) RETURN w.id"
        resp = self.conn.execute(query)
        while resp.has_next():
            wit_id = resp.get_next()[0]
            break

        # Test the parts
        for ms, parts in yield_from_witness_parts_aggregated_by_doc(
            conn=self.conn, witness_id=wit_id
        ):
            pprint(parts)


if __name__ == "__main__":
    unittest.main()
