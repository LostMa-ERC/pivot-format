from lxml import etree

from app.tei.parsers.find_node import find_node


class ProfileDescXML:
    """Branch of XML tree at teiHeader/profileDesc."""

    def __init__(self, tree):
        self.tree = tree

    @property
    def creation(self) -> etree.Element:
        xpath = ".//tei:profileDesc/tei:creation"
        return find_node(tree=self.tree, xpath=xpath)

    @property
    def langUsage(self) -> etree.Element:
        xpath = ".//tei:profileDesc/tei:langUsage"
        return find_node(tree=self.tree, xpath=xpath)

    @property
    def textClass(self) -> etree.Element:
        xpath = ".//tei:profileDesc/tei:textClass"
        return find_node(tree=self.tree, xpath=xpath)
