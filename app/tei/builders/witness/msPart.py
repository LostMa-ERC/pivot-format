from kuzu import Connection
from lxml import etree

from app.tei.constants import XML_ID
from app.tei.data.scripta import fetch_witness_scripta

# Data modelers
from app.tei.data.witness import PartModel

# Fetch data needed for the msPart
from app.tei.data.witness.document import get_document_from_part

# Builders
from .msIdentifier import make_msDesc_msIdentifier


def build_msPart(conn: Connection, part: PartModel, wit_id: int) -> etree.Element:
    # Make the msPart root
    root = etree.Element("msPart")

    # Fetch data and make msIdentifier
    document_data = get_document_from_part(conn=conn, part_id=part.id)
    msIdentifier = make_msDesc_msIdentifier(document_data=document_data)
    root.append(msIdentifier)

    # Make msContents
    msContents = etree.SubElement(root, "msContents")

    # Make 1 msItem for this part
    msItem = etree.SubElement(msContents, "msItem")
    msItem.set(XML_ID, part.xml_id)
    locusGrp = etree.SubElement(msItem, "locusGrp")
    textLang = etree.SubElement(msItem, "textLang")

    # List the locus
    for range in part.page_ranges:
        attrib = {"from": range.start, "to": range.end}
        locus = etree.SubElement(locusGrp, "locus", attrib=attrib)
        locus.text = range.text
    # If the witness has a scripta, add it to the msItem
    scripta = fetch_witness_scripta(conn=conn, id=wit_id)
    if scripta:
        textLang.set("mainLang", scripta.code)
        textLang.set("ref", f"#{scripta.xml_id}")
        textLang.text = scripta.description

    return root
