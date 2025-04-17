from kuzu import Connection
from lxml import etree

# Builder for nested entity
from app.tei.builders.witness.msPart import build_msPart
from app.tei.builders.witness.physDesc import build_physDesc

# Data modelers
from app.tei.data.witness.origin import fetch_witness_origin_date
from app.tei.data.witness.part import PartModel

# Fetch data needed for the msDesc
from app.tei.data.witness.siglum import fetch_witness_siglum


def build_msDesc(
    conn: Connection, wit_id: int, parts: list[PartModel]
) -> etree.Element:
    # Make the msDesc root
    root = etree.Element("msDesc")

    # Build the msIdentifier of the witness's theoretical document
    msIdentifier = etree.SubElement(root, "msIdentifier")
    siglum = fetch_witness_siglum(conn=conn, id=wit_id)
    msName = etree.SubElement(msIdentifier, "msName")
    msName.text = f"Historical document of witness {siglum}".strip()
    abbr = etree.SubElement(msIdentifier, "abbr", type="siglum")
    abbr.text = siglum

    # Build each part
    for part in parts:
        msPart = build_msPart(conn=conn, part=part, wit_id=wit_id)
        root.append(msPart)

    # Make the history
    history = etree.SubElement(root, "history")
    origin = etree.SubElement(history, "origin")
    origDate_data = fetch_witness_origin_date(conn=conn, witness_id=wit_id)
    origDate = etree.SubElement(origin, "origDate", origDate_data.attribs)
    origDate.text = origDate_data.freetext

    # Make the physDesc
    physDesc = build_physDesc(conn=conn, parts=parts)
    root.append(physDesc)

    return root
