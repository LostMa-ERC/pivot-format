from datetime import datetime

from kuzu import Connection
from lxml import etree

from app.tei.builders.text import (
    build_encondingDesc,
    build_profileDesc,
    build_sourceDesc,
    build_titleStmt,
)
from app.tei.data.text.language import fetch_language
from app.tei.parsers.find_node import find_node
from app.tei.parsers.text_tree import TextXMLTree


class TextDocument:

    def __init__(
        self,
        conn: Connection,
        text_id: int,
        encodingDesc_node: etree.Element = None,
    ) -> None:
        self.conn = conn
        self.id = text_id
        self.lang = fetch_language(conn=conn, id=text_id)
        self.parser = TextXMLTree()

        # Replace the encodingDesc with the standard taxonomies
        if encodingDesc_node is not None:
            new_node = encodingDesc_node
        else:
            new_node = build_encondingDesc(
                conn=self.conn, root=self.parser.encodingDesc
            )
        old_node = find_node(tree=self.parser.tree, xpath=".//tei:encodingDesc")
        old_node.getparent().replace(old_node, new_node)

        # --- fileDesc ---
        # --- --- titlestmt --- ---
        build_titleStmt(
            conn=self.conn,
            text_id=text_id,
            root=self.parser.titleStmt,
        )
        # --- --- publicationStmt --- ---
        node = self.parser.publicationStmt.date
        node.text = datetime.today().strftime("%Y-%m-%d")

        # --- sourceDesc ---
        build_sourceDesc(
            conn=self.conn,
            text_id=text_id,
            root=self.parser.sourceDesc,
        )
        # --- profileDesc ---
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
