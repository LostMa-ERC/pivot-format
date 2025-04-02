from datetime import datetime

from lxml import etree

from app.tei.xml.find_node import find_node


class PublicationStmtXML:
    """Branch of XML tree at teiHeader/fileDesc/publicationStmt."""

    def __init__(self, tree: etree.ElementTree):
        self.tree = tree
        self.date.text = datetime.now().strftime("%Y-%m-%d")

    @property
    def date(self) -> etree.Element:
        xpath = ".//tei:publicationStmt/tei:date"
        return find_node(tree=self.tree, xpath=xpath)
