from lxml import etree

from app.tei.parsers.find_node import find_node


class TitleStmtXML:
    """Branch of XML tree at teiHeader/fileDesc/titleStmt."""

    def __init__(self, tree: etree.ElementTree):
        self.tree = tree

    @property
    def root(self) -> etree.Element:
        xpath = ".//tei:titleStmt"
        return find_node(tree=self.tree, xpath=xpath)

    @property
    def title(self) -> etree.Element:
        xpath = ".//tei:titleStmt/tei:title"
        return find_node(tree=self.tree, xpath=xpath)
