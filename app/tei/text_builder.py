from datetime import datetime

from lxml import etree

from app.tei.builders.text import (
    build_titleStmt,
    build_encondingDesc,
    build_profileDesc,
    build_sourceDesc,
)
from app.tei.parsers.text_tree import TextXMLTree
from app.tei.data.text.language import fetch_language
from kuzu import Connection


class TextDocument:

    def __init__(self, conn: Connection, text_id: int) -> None:
        self.conn = conn
        self.id = text_id
        self.lang = fetch_language(conn=conn, id=text_id)
        self.parser = TextXMLTree()

        # Build the titleStmt
        build_titleStmt(
            conn=self.conn,
            text_id=text_id,
            root=self.parser.titleStmt,
        )
        # Build the publicationStmt
        node = self.parser.publicationStmt.date
        node.text = datetime.today().strftime("%Y-%m-%d")
        # Build the encodingDesc
        build_encondingDesc(
            conn=self.conn,
            text_id=text_id,
            root=self.parser.encodingDesc,
        )
        # Build the sourceDesc
        build_sourceDesc(
            conn=self.conn,
            text_id=text_id,
            root=self.parser.sourceDesc,
        )
        # Build the profileDesc
        build_profileDesc(
            conn=self.conn,
            text_id=text_id,
            root=self.parser.profileDesc,
        )

    def write(self, outfile: str) -> None:
        etree.indent(self.parser.tree)
        s = etree.tostring(
            self.parser.tree,
            encoding="utf-8",
            xml_declaration=True,
            pretty_print=True,
        )
        with open(outfile, "wb") as f:
            f.write(s)
