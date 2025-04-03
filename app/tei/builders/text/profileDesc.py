from lxml import etree
from kuzu import Connection

from app.tei.constants import XML_ID

# XML parser for the profileDesc branch
from app.tei.parsers.profileDesc import ProfileDescXML

# Fetch data needed for the profileDesc
from app.tei.data.text import fetch_creation_date, fetch_language


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
