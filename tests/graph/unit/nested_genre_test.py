import unittest

import kuzu

CREATE_GENRE_TABLE = """
CREATE NODE TABLE Genre (id INT, name STRING, PRIMARY KEY(id));
"""

CREATE_TEXT_TABLE = """
CREATE NODE TABLE Text (id INT, name STRING, PRIMARY KEY (id));
"""

CREATE_EDGE_TABLES = """
CREATE REL TABLE HAS_GENRE (FROM Text TO Genre);
CREATE REL TABLE HAS_PARENT (FROM Genre TO Genre);
"""

INSERT_NODES = """
CREATE
(:Text {id: 1, name: 'example text'}),
(:Genre {id: 1, name: 'grandparent'}),
(:Genre {id: 2, name: 'parent'}),
(:Genre {id: 3, name: 'child1'}),
(:Genre {id: 4, name: 'child2'}),
(:Genre {id: 5, name: 'grandchild'}),
(:Genre {id: 6, name: 'orphan'})
"""

INSERT_EDGES = """
MATCH (t:Text {id:1})
MATCH (g1:Genre {id:1})
MATCH (g2:Genre {id:2})
MATCH (g3:Genre {id:3})
MATCH (g4:Genre {id:4})
MATCH (g5:Genre {id:5})
CREATE (t)-[:HAS_GENRE]->(g5)
CREATE (g5)-[:HAS_PARENT]->(g4)
CREATE (g4)-[:HAS_PARENT]->(g2)
CREATE (g3)-[:HAS_PARENT]->(g2)
CREATE (g2)-[:HAS_PARENT]->(g1)
"""


class TestKuzuCypherQuery(unittest.TestCase):

    def setUp(self):
        # Connect to an in-memory Kuzu database
        db = kuzu.Database()
        self.conn = kuzu.Connection(db)

    def test_family_group_collection(self):
        self.conn.execute(CREATE_GENRE_TABLE)
        self.conn.execute(CREATE_TEXT_TABLE)
        self.conn.execute(CREATE_EDGE_TABLES)
        self.conn.execute(INSERT_NODES)
        self.conn.execute(INSERT_EDGES)

        # Find the root of all family trees and list its family members
        # Return the family groups with the largest being the first result row
        query = """
        MATCH path=(child:Genre)-[r:HAS_PARENT *0..]->(parent:Genre)
        WHERE NOT (parent)-[:HAS_PARENT]->()
        WITH parent as parent, collect(child) as family, count(child) as size
        RETURN parent, family
        ORDER BY size DESC
        """
        rows = self.conn.execute(query).get_as_pl().rows()
        largest_family, smallest_family = rows[0], rows[1]
        largest_family_eldest, largest_family_members = (
            largest_family[0],
            largest_family[1],
        )
        smallest_family_eldest, smallest_family_members = (
            smallest_family[0],
            smallest_family[1],
        )

        # Affirm that the largest family's parent is 'grandparent'
        self.assertEqual(largest_family_eldest["name"], "grandparent")
        # Affirm that the largest family's list of members has 5 nodes
        self.assertEqual(len(largest_family_members), 5)
        # Affirm that all the family members' names are what is expected
        member_names = [i["name"] for i in largest_family_members]
        self.assertCountEqual(
            member_names, ["grandparent", "parent", "child1", "child2", "grandchild"]
        )

        # Affirm that the smallest family's parent is 'orphan'
        self.assertEqual(smallest_family_eldest["name"], "orphan")
        # Affirm that the smallest family's list of members has 1 node
        self.assertEqual(len(smallest_family_members), 1)
        # Affirm that the family's members names are what is expected
        member_names = [i["name"] for i in smallest_family_members]
        self.assertCountEqual(member_names, ["orphan"])


if __name__ == "__main__":
    unittest.main()
