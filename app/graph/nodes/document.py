from app.graph import Property, Type

from .core import Node

DOCUMENT_PROPS = [
    Property(name="id", type=Type.int),
    Property(name="shelfmark", type=Type.string),
    Property(name="collection", type=Type.string),
    Property(name="invented_label", type=Type.string),
    Property(name="is_hypothetical", type=Type.boolean),
    Property(name="hypothesis", type=Type.string),
    Property(name="is_collection_of_fragments", type=Type.boolean),
    Property(name="old_shelfmark", type=Type.string),
    Property(name="urls", type=Type.string_list),
    Property(name="catalogue_record", type=Type.string),
    Property(name="ark", type=Type.string),
]

Document = Node(label="Document", pk="id", properties=DOCUMENT_PROPS)
