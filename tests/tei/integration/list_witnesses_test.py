import unittest

from app.graph.edges import WitnessIsManifestationOf
from app.tei.data.text.witnesses import fetch_witnesess_of_a_text
from tests.tei.integration import TEIIntegrationTest


class ListWitnessesTest(TEIIntegrationTest):
    def test_text_with_multiple_witnesses(self):
        # Find texts with more than 1 witness
        iterate_texts = f"""
        MATCH (t:Text)<-[r:{WitnessIsManifestationOf.edge_label}]-(w:Witness)
        WITH t as text, count(w) as n_wits
        WHERE n_wits > 1
        RETURN text.id
        """
        for row in self.kconn.execute(iterate_texts).get_as_pl().iter_rows():
            text_id = row[0]
            break

        # Givne the target text's unique ID, get the IDs of its witnesses
        witness_ids = fetch_witnesess_of_a_text(conn=self.kconn, text_id=text_id)

        # Affirm that the function returned a list of valid identifiers (integers)
        [self.assertIsInstance(id, int) for id in witness_ids]

        # Affirm that the function returned a list of length greater than 1
        self.assertGreaterEqual(len(witness_ids), 2)

    def test_text_wihout_witnesses(self):
        # Find texts with more than no witnesses
        iterate_texts = f"""
        MATCH (t:Text)
        WHERE NOT (t:Text)<-[r:{WitnessIsManifestationOf.edge_label}]-(w:Witness)
        RETURN t.id
        """
        for row in self.kconn.execute(iterate_texts).get_as_pl().iter_rows():
            text_id = row[0]
            break

        # Givne the target text's unique ID, get the IDs of its witnesses
        witness_ids = fetch_witnesess_of_a_text(conn=self.kconn, text_id=text_id)

        # Affirm that the function returned an empty list
        self.assertListEqual(witness_ids, [])


if __name__ == "__main__":
    unittest.main()
