from kuzu import Connection
from lxml import etree

# Data modelers
from app.tei.data.witness import PartModel

# Fetch data needed for the msPart


def build_msPart(conn: Connection, part: PartModel) -> etree.Element:
    # Make the msPart root
    root = etree.Element("msPart")

    # Make msIdentifier

    return root
