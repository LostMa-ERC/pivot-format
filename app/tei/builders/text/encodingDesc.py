from kuzu import Connection
from lxml import etree

from app.tei.constants import XML_ID

# Fetch data needed for the encodingDesc
from app.tei.data.text.genre import GenreModel, fetch_all_genre_roots

# XML parser for the encodingDesc branch
from app.tei.parsers.encodingDesc.parse_encodingDesc import EncodingDescXML


def make_genre_category(parent: etree.Element, genre: GenreModel) -> etree.Element:
    # Make a category for this genre
    category = etree.SubElement(parent, "category")
    category.set(XML_ID, genre.xml_id)

    # Add a catDesc into the category
    catDesc = etree.SubElement(category, "catDesc")
    catDesc.text = genre.name

    # Add a desc into the category
    desc = etree.SubElement(category, "desc")
    desc.text = genre.description

    # If the genre has alternative names, add them into the desc
    for name in genre.alternative_names:
        n = etree.SubElement(desc, "name", type="alt")
        n.text = name

    # If the genre has URL references, create a bibl and add them as ptr nodes
    if len(genre.described_at_URL) > 1:
        bibl = etree.SubElement(desc, "bibl")
        for url in genre.described_at_URL:
            _ = etree.SubElement(bibl, "ptr", target=url)

    # Return the category node created for the genre
    # (not always necessary, since subElement was used to modify the parent category)
    return category


def build_encondingDesc(conn: Connection, root: EncodingDescXML) -> None:
    parent_category = root.genre_taxonomy
    for family in fetch_all_genre_roots(conn=conn):
        node = make_genre_category(parent=parent_category, genre=family.root)
        if family.children:
            for i in family.children:
                make_genre_category(parent=node, genre=i)
