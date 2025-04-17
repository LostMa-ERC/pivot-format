from kuzu import Connection
from lxml import etree

# Builders
from app.tei.builders.witness.msPart import build_msPart
from app.tei.builders.witness.physDesc import build_physDesc

# Data models and fetchers
from app.tei.data.witness.origin import fetch_witness_origin_date
from app.tei.data.witness.part import PartModel
from app.tei.data.witness.status import fetch_witness_status, is_witness_hypothetical


def build_msDesc(
    conn: Connection,
    wit_id: int,
    parts: list[PartModel],
    siglum: str,
) -> etree.Element:
    # Make the msDesc root
    root = etree.Element("msDesc")
    if is_witness_hypothetical(conn=conn, id=wit_id):
        root.set("status", "hypothetical")
    else:
        status = fetch_witness_status(conn=conn, id=wit_id)
        root.set("status", status.status)
        if status.note:
            note = etree.SubElement(root, "note")
            note.text = status.note

    # Build the msIdentifier of the witness's theoretical document
    msIdentifier = etree.SubElement(root, "msIdentifier")
    msName = etree.SubElement(msIdentifier, "msName")
    msName.text = f"Historical document of witness {siglum}".strip()

    # Build each part
    for part in parts:
        msPart = build_msPart(conn=conn, part=part, wit_id=wit_id)
        root.append(msPart)

    # Make the history
    history = etree.SubElement(root, "history")
    origin = etree.SubElement(history, "origin")
    origDate_data = fetch_witness_origin_date(conn=conn, witness_id=wit_id)
    origDate = etree.SubElement(origin, "origDate", origDate_data.attribs)
    origDate.text = origDate_data.date_freetext

    # Make the physDesc
    physDesc = build_physDesc(conn=conn, parts=parts)
    root.append(physDesc)

    return root
