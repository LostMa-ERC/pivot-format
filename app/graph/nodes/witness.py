from app.graph import Property, Type

from .core import Node

WITNESS_PROPS = [
    Property(name="id", type=Type.int),
    Property(name="is_unobserved", type=Type.boolean),
    Property(name="hypothesis", type=Type.string),
    Property(name="siglum", type=Type.string),
    Property(name="alternative_sigla", type=Type.string_list),
    Property(name="status_witness", type=Type.string),
    Property(name="status_notes", type=Type.string),
    Property(name="is_excerpt", type=Type.boolean),
    Property(name="creation_date", type=Type.temporal),
    Property(name="creation_date_certainty", type=Type.string),
    Property(name="creation_date_freetext", type=Type.string),
    Property(name="urls", type=Type.string_list),
]

Witness = Node(label="Witness", pk="id", properties=WITNESS_PROPS)
