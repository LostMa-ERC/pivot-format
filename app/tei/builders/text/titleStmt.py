from lxml import etree
from kuzu import Connection

# XML parser for the titleStmt branch
from app.tei.xml.fileDesc import TitleStmtXML

# Fetch data needed for the titleStmt
from app.tei.data.contributors import list_resp_persons
from app.tei.data.text.language import fetch_language
from app.tei.data.text.alternative_titles import fetch_alternative_title
from app.tei.data.text.title import fetch_title


def build_titleStmt(conn: Connection, text_id: int, root: TitleStmtXML):
    # Set the main title
    data = fetch_title(conn=conn, id=text_id)
    main = etree.SubElement(root.title, "title", type="main")
    main.text = data
    sub = etree.SubElement(root.title, "title", type="sub")
    sub.text = "Encoding of Metadata"

    # Set alternative titles
    parent = root.title
    alt_titles = fetch_alternative_title(conn=conn, id=text_id)
    for alt_title in alt_titles:
        node = etree.Element("title", type="alt")
        node.text = alt_title
        parent.addnext(node)

    # Set the titleStmt's <respStmt>
    language = fetch_language(conn=conn, id=text_id)
    people = list_resp_persons(lang=language)
    parent = root.respStmt
    for person in people:
        n = etree.SubElement(parent, "name")
        n.text = person.name
        n = etree.SubElement(parent, "resp")
        n.text = person.role
