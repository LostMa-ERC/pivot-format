from lxml import etree
from kuzu import Connection

# XML parser for the titleStmt branch
from app.tei.parsers.fileDesc import TitleStmtXML

# Fetch data needed for the titleStmt
from app.tei.data.contributors import list_resp_persons
from app.tei.data.text import fetch_language, fetch_title


def build_titleStmt(conn: Connection, text_id: int, root: TitleStmtXML):
    # Set the main title
    data = fetch_title(conn=conn, id=text_id)
    node = etree.SubElement(root.title, "title")
    node.text = f'Metadata encoding of "{data}"'

    # Set the titleStmt's <respStmt>
    language = fetch_language(conn=conn, id=text_id)
    people = list_resp_persons(lang=language)
    parent = root.respStmt
    for person in people:
        n = etree.SubElement(parent, "name")
        n.text = person.name
        n = etree.SubElement(parent, "resp")
        n.text = person.role
