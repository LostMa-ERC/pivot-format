from lxml import etree

from app.tei.parsers.find_node import find_node


class SourceDescXML:
    """Branch of XML tree at teiHeader/sourceDesc."""

    def __init__(self, tree):
        self.tree = tree

    @property
    def title(self) -> etree.Element:
        xpath = ".//tei:sourceDesc/tei:title[@type='full']"
        return find_node(tree=self.tree, xpath=xpath)
