from kuzu import Connection
from lxml import etree

from app.tei.constants import XML_ID

# Fetch data needed for the encodingDesc
from app.tei.data.text.genre import GenreModel, fetch_all_genre_roots

# XML parser for the encodingDesc branch
from app.tei.parsers.encodingDesc.parse_encodingDesc import EncodingDescXML


def make_genre_category(parent: etree.Element, genre: GenreModel) -> etree.Element:
    category = etree.SubElement(parent, "category")
    category.set(XML_ID, genre.xml_id)
    catDesc = etree.SubElement(category, "catDesc")
    catDesc.text = genre.name
    return category


def build_encondingDesc(conn: Connection, root: EncodingDescXML) -> None:
    parent_category = root.genre_taxonomy
    for family in fetch_all_genre_roots(conn=conn):
        node = make_genre_category(parent=parent_category, genre=family.root)
        if family.children:
            for i in family.children:
                make_genre_category(parent=node, genre=i)

        # parent = make_genre_category(parent=parent, genre=genre)
