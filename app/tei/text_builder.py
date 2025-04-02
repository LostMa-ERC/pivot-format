from datetime import datetime

from lxml import etree

from app.tei.builders.text import build_titleStmt, build_encondingDesc
from app.tei.xml.text_tree import TextXMLTree
from kuzu import Connection


class TextTEIBuilder:
    def __init__(self, conn: Connection):
        self.conn = conn

    def __call__(self, text_id: int) -> etree.ElementTree:
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
        return self.parser.tree

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
