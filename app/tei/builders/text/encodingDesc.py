from kuzu import Connection
from lxml import etree

from app.tei.constants import XML_ID

# Fetch data needed for the encodingDesc
from app.tei.data.text.genre import GenreModel, fetch_all_genre_roots
from app.tei.data.text.tradition_status import StatusModel, fetch_all_tradition_statuses

# XML parser for the encodingDesc branch
from app.tei.parsers.encodingDesc.parse_encodingDesc import EncodingDescXML
from app.tei.parsers.find_node import find_node


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
    return category


def make_status_category(parent: etree.Element, status: StatusModel) -> etree.Element:
    # Make a category for this status
    category = etree.SubElement(parent, "category")
    category.set(XML_ID, status.xml_id)

    # Add a catDesc into the category
    catDesc = etree.SubElement(category, "catDesc")
    catDesc.text = status.name

    # Add a desc into the category
    desc = etree.SubElement(category, "desc")
    desc.text = status.description

    if len(status.url) > 1:
        bibl = etree.SubElement(desc, "bibl")
        for url in status.url:
            _ = etree.SubElement(bibl, "ptr", target=url)


def build_encondingDesc(conn: Connection, root: EncodingDescXML) -> None:
    # Dynamically build the taxonomy for genre
    for family in fetch_all_genre_roots(conn=conn):
        node = make_genre_category(parent=root.genre_taxonomy, genre=family.root)
        if family.children:
            for i in family.children:
                make_genre_category(parent=node, genre=i)

    # Dynamically build the taxonomy for a text's tradition status
    for status in fetch_all_tradition_statuses(conn=conn):
        make_status_category(parent=root.tradition_status_taxonomy, status=status)

    # Return the created tree
    parent_node = find_node(tree=root.tree, xpath=".//tei:encodingDesc")
    return parent_node
