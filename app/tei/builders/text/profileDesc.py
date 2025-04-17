from kuzu import Connection
from lxml import etree

from app.tei.constants import XML_ID

# Fetch data needed for the profileDesc
from app.tei.data.text import (
    fetch_all_genres_related_to_text,
    fetch_creation_date,
    fetch_direct_genre,
    fetch_language,
    fetch_literary_form_of_a_text,
)
from app.tei.data.text.tradition_status import fetch_text_tradition_status

# XML parser for the profileDesc branch
from app.tei.parsers.profileDesc import ProfileDescXML


def build_profileDesc(conn: Connection, text_id: int, root: ProfileDescXML) -> None:
    # --- CREATION ---
    # Add date to creation
    data = fetch_creation_date(conn=conn, id=text_id)
    attrs = {"notBefore": data.notBefore, "notAfter": data.notAfter, "cert": data.cert}
    node = etree.SubElement(root.creation, "date", attrib=attrs)
    node.text = data.date_freetext

    # --- LANGUSAGE ---
    # Add language to langUsage
    data = fetch_language(conn=conn, id=text_id)
    attrs = {}
    if data:
        attrs = {"ident": data.code, "corresp": data.url or "", XML_ID: data.xml_id}
    node = etree.SubElement(root.langUsage, "language", attrib=attrs)
    node.text = data.description

    # --- TEXTCLASS ---
    # Create a catRef for the text's literary form
    label = fetch_literary_form_of_a_text(conn=conn, text_id=text_id)
    ref = f"#{label}Form"
    _ = etree.SubElement(root.textClass, "catRef", scheme="#form", target=ref)

    # Create a catRef for the text's tradition status
    data = fetch_text_tradition_status(conn=conn, text_id=text_id)
    if data:
        ref = f"#{data.xml_id}"
        _ = etree.SubElement(
            root.textClass, "catRef", scheme="#traditionStatus", target=ref
        )

    # If the text has a genre, create a catRef for the genre
    # List the names of the genre and its parents as keyword terms
    data = fetch_direct_genre(conn=conn, text_id=text_id)
    if data:
        ref = f"#{data.xml_id}"
        _ = etree.SubElement(root.textClass, "catRef", scheme="#genre", target=ref)

        # Create a list of the keywords of the genres associated with the text
        keywords = etree.SubElement(root.textClass, "keywords")

        # Get all the genres associated with this text
        genres_ordered_eldest_first = fetch_all_genres_related_to_text(
            conn=conn, text_id=text_id
        )

        for genre in reversed(genres_ordered_eldest_first):
            term = etree.SubElement(keywords, "term")
            term.text = genre.name
