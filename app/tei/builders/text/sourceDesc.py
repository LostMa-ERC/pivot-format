from kuzu import Connection
from lxml import etree

# Builder for the witnesses
from app.tei.builders.witness.msDesc import build_msDesc
from app.tei.constants import XML_ID

# Fetch data needed for the sourceDesc
from app.tei.data.text import (
    fetch_alternative_title,
    fetch_authors,
    fetch_title,
    fetch_witnesess_of_a_text,
)
from app.tei.data.witness import yield_from_witness_parts_aggregated_by_doc

# XML parser for the sourceDesc branch
from app.tei.parsers.fileDesc import SourceDescXML


def build_sourceDesc(conn: Connection, text_id: int, root: SourceDescXML) -> None:
    # Set the text's Heurist ID in the bibl node
    root.bibl.set(XML_ID, f"text_{text_id}")

    # Add the main title
    data = fetch_title(conn=conn, id=text_id)
    main = etree.SubElement(root.title, "title", type="main")
    main.text = data

    # Set alternative titles
    alt_titles = fetch_alternative_title(conn=conn, id=text_id)
    for alt_title in alt_titles:
        node = etree.SubElement(root.title, "title", type="alt")
        node.text = alt_title

    # Add the text's author or authors
    for author in fetch_authors(conn=conn, id=text_id):
        node = etree.Element("author")
        node.set(XML_ID, author.xml_id)
        if author.urls != []:
            urls = " ".join(author.urls)
            node.set("ref", urls)
        node.text = author.full_name
        root.title.addnext(node)

    # Create a witness node for each of the text's witnesses
    witness_ids = fetch_witnesess_of_a_text(conn=conn, text_id=text_id)
    for id in witness_ids:
        xml_id = f"witness_{id}"
        node = etree.SubElement(root.listWit, "witness")
        node.set(XML_ID, xml_id)
        for ms, parts in yield_from_witness_parts_aggregated_by_doc(
            conn=conn,
            witness_id=id,
        ):
            msDesc = build_msDesc(conn=conn, wit_id=id, ms=ms, parts=parts)
            node.append(msDesc)
