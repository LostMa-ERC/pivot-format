from lxml import etree
from kuzu import Connection

from app.tei.constants import XML_ID

# XML parser for the sourceDesc branch
from app.tei.parsers.sourceDesc import SourceDescXML

# Fetch data needed for the sourceDesc
from app.tei.data.text import (
    fetch_title,
    fetch_alternative_title,
    fetch_authors,
)


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
