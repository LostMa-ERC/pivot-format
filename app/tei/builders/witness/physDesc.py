from kuzu import Connection
from lxml import etree


def build_physDesc(conn: Connection, witness_id: int) -> etree.Element:
    root = etree.Element("physDesc")
    return root
