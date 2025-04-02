"""Class for navigating the base (empty) tree of the text's TEI document."""

from lxml import etree

from app import TEXT_TEI_MODEL
from app.tei.xml import fileDesc


class ParserTextTEI_XML:
    def __init__(self, base_file: str = TEXT_TEI_MODEL):
        self.tree = etree.parse(base_file)
        self.titleStmt = fileDesc.TitleStmtXML(tree=self.tree)
        self.publicationStmt = fileDesc.PublicationStmtXML(tree=self.tree)
        self.encodingDesc = fileDesc.EncodingDescXML(tree=self.tree)
        self.profileDesc = fileDesc.ProfileDescXML(tree=self.tree)
