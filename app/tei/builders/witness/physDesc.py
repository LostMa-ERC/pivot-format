from kuzu import Connection
from lxml import etree

from app.tei.constants import XML_ID
from app.tei.data.witness.part import PartModel
from app.tei.data.witness.physDesc import PhysDescModel, fetch_physDesc


def build_physDesc(conn: Connection, parts: list[PartModel]) -> etree.Element:
    root = etree.Element("physDesc")

    # Get the relevant physdesc
    descriptions = [fetch_physDesc(conn=conn, part_id=p.id) for p in parts]
    if descriptions == [None]:
        return root
    unique_data = {d.id: d for d in descriptions}
    assert len(unique_data.keys()) == 1
    data = list(unique_data.values())[0]
    assert isinstance(data, PhysDescModel)

    try:
        # Add metadata to the physDesc element
        root.set(XML_ID, data.xml_id)
        objectDesc = etree.SubElement(root, "objectDesc", form=data.form)
        supportDesc = etree.SubElement(
            objectDesc, "supportDesc", material=data.material
        )

        # Extent
        extent = etree.SubElement(supportDesc, "extent")
        dimensions = etree.SubElement(
            extent,
            "dimensions",
            unit="millimeters",
            type="written",
        )
        height = etree.SubElement(
            dimensions,
            "height",
            quantity=data.folio_size_height or "",
        )
        height.text = data.folio_size_height
        width = etree.SubElement(
            dimensions,
            "width",
            quantity=data.folio_size_width or "",
        )
        width.text = data.folio_size_width

        # Layout
        layoutDesc = etree.SubElement(root, "layoutDesc")
        layout = etree.SubElement(
            layoutDesc,
            "layout",
            columns=data.number_of_columns or "",
            writtenLines=data.number_of_lines_in_writing_area or "",
        )
        if data.above_top_line and data.above_top_line != "unknown":
            layout.set("topLine", data.above_top_line)

        # Hands
        handDesc = etree.SubElement(root, "handDesc")
        handNote = etree.SubElement(handDesc, "handNote")
        handNote.set("script", data.script_type)
        if data.subscript_type:
            handNote.set("subtype", data.subscript_type)

        # Illustrations
        decoDesc = etree.SubElement(root, "decoDesc")
        note = etree.SubElement(decoDesc, "decNote", type="illustration")
        etree.SubElement(note, "measure", quantity=data.amount_of_illustrations)
        # Decorations
        for dec in data.has_decorations:
            etree.SubElement(decoDesc, "decoNote", type=dec)
    except Exception as e:
        print(data)
        raise e

    return root
