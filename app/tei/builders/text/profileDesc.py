from kuzu import Connection
from lxml import etree

from app.tei.constants import XML_ID

# Fetch data needed for the profileDesc
from app.tei.data.text import (
    fetch_all_genres_related_to_text,
    fetch_creation_date,
    fetch_direct_genre,
    fetch_language,
)

# XML parser for the profileDesc branch
from app.tei.parsers.profileDesc import ProfileDescXML


def build_profileDesc(conn: Connection, text_id: int, root: ProfileDescXML) -> None:
    # Add date to creation
    data = fetch_creation_date(conn=conn, id=text_id)
    attrs = {"notBefore": data.notBefore, "notAfter": data.notAfter, "cert": data.cert}
    node = etree.SubElement(root.creation, "date", attrib=attrs)
    node.text = data.date_freetext

    # Add language to langUsage
    data = fetch_language(conn=conn, id=text_id)
    attrs = {}
    if data:
        attrs = {"ident": data.code, "ref": data.url, XML_ID: data.xml_id}
    node = etree.SubElement(root.langUsage, "language", attrib=attrs)
    node.text = data.description

    # If the text has a genre, add a catRef node to textClass
    data = fetch_direct_genre(conn=conn, text_id=text_id)
    if data:
        ref = f"#{data.xml_id}"
        _ = etree.SubElement(root.textClass, "catRef", target=ref, scheme="#genre")

        # Create a list of the keywords of the genres associated with the text
        keywords = etree.SubElement(root.textClass, "keywords")

        # Get all the genres associated with this text
        genres_ordered_eldest_first = fetch_all_genres_related_to_text(
            conn=conn, text_id=text_id
        )

        for genre in reversed(genres_ordered_eldest_first):
            term = etree.SubElement(keywords, "term")
            term.text = genre.name
