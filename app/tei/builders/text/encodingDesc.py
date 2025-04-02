from kuzu import Connection
from lxml import etree

from app.constants import XML_ID

# XML parser for the encodingDesc branch
from app.tei.parsers.encodingDesc.parse_encodingDesc import EncodingDescXML

# Fetch data needed for the encodingDesc
from app.tei.data.text.genre import GenreModel, fetch_genres


def make_genre_category(parent: etree.Element, genre: GenreModel) -> etree.Element:
    category = etree.SubElement(parent, "category")
    category.set(XML_ID, genre.xml_id)
    catDesc = etree.SubElement(category, "catDesc")
    catDesc.text = genre.name
    return category


def build_encondingDesc(conn: Connection, text_id: int, root: EncodingDescXML) -> None:
    parent = root.genre_taxonomy
    for genre in fetch_genres(conn=conn, id=text_id):
        parent = make_genre_category(parent=parent, genre=genre)
