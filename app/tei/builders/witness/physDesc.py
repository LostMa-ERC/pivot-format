from kuzu import Connection
from lxml import etree

from app.tei.data.witness.part import PartModel
from app.tei.data.witness.physDesc import PhysDescModel, fetch_physDesc


def build_physDesc(conn: Connection, parts: list[PartModel]) -> etree.Element:
    root = etree.Element("physDesc")

    # Get the relevant physdesc
    descriptions = [
        d
        for d in [
            fetch_physDesc(
                conn=conn,
                part_id=p.id,
            )
            for p in parts
        ]
        if d
    ]
    if len(descriptions) == 0:
        return root
    unique_data = {d.id: d for d in descriptions}
    assert len(unique_data.keys()) == 1
    data = list(unique_data.values())[0]
    assert isinstance(data, PhysDescModel)

    try:
        # Add metadata to the physDesc element
        root.set("corresp", f"#{data.xml_id}")
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

        # Dimensions -- height
        height = etree.SubElement(dimensions, "height")
        try:
            int(data.folio_size_height)
            height.set("quantity", data.folio_size_height)
        except Exception:
            pass
        height.text = data.folio_size_height

        # Dimensions -- width
        width = etree.SubElement(dimensions, "width")
        try:
            int(data.folio_size_width)
            width.set("quantity", data.folio_size_width)
        except Exception:
            pass
        width.text = data.folio_size_width

        # Layout
        layoutDesc = etree.SubElement(objectDesc, "layoutDesc")
        layout = etree.SubElement(layoutDesc, "layout")
        try:
            int(data.number_of_columns)
            layout.set("columns", data.number_of_columns)
        except Exception:
            pass
        try:
            int(data.number_of_lines_in_writing_area)
            layout.set("writtenLines", data.number_of_lines_in_writing_area)
        except Exception:
            pass
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
        note = etree.SubElement(decoDesc, "decoNote", type="illustration")
        etree.SubElement(
            note,
            "measure",
            quantity=data.amount_of_illustrations,
        )
        # Decorations
        for dec in data.has_decorations:
            etree.SubElement(decoDesc, "decoNote", type=dec)
    except Exception as e:
        print(data)
        raise e

    return root
