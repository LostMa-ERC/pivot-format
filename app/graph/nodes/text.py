from app.graph import Property, Type

from .core import Node

TEXT_PROPS = [
    Property(name="id", type=Type.int),
    Property(name="name", type=Type.string),
    Property(name="language", type=Type.string),
    Property(name="form", type=Type.string),
    Property(name="is_hypothetical", type=Type.boolean),
    Property(name="hypothesis", type=Type.string),
    Property(name="alternative_names", type=Type.string_list),
    Property(name="is_peripheral", type=Type.boolean),
    Property(name="length", type=Type.float),
    Property(name="length_freetext", type=Type.string),
    Property(name="verse_type", type=Type.string),
    Property(name="rhyme_type", type=Type.string),
    Property(name="stanza_type", type=Type.string),
    Property(name="tradition_status", type=Type.string),
    Property(name="has_lost_older_version", type=Type.boolean),
    Property(name="lost_older_version_freetext", type=Type.string),
    Property(name="rewritings_freetext", type=Type.string),
    Property(name="note", type=Type.string),
    Property(name="creation_date", type=Type.temporal),
    Property(name="creation_date_certainty", type=Type.string),
    Property(name="creation_date_freetext", type=Type.string),
    Property(name="urls", type=Type.string_list),
]

Text = Node(label="Text", pk="id", properties=TEXT_PROPS)
