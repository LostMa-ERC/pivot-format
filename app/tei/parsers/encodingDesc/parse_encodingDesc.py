from lxml import etree

from app.tei.parsers.find_node import find_node


class EncodingDescXML:
    """Branch of XML tree at teiHeader/encodingDesc."""

    def __init__(self, tree: etree.ElementTree):
        self.tree = tree

    @property
    def genre_taxonomy(self) -> etree.Element:
        xpath = ".//tei:encodingDesc//tei:category[@xml:id='genre']"
        return find_node(tree=self.tree, xpath=xpath)
