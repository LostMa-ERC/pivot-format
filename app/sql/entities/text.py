from app.sql.entities.core import Entity, Property, SQLTransformer

Text = Entity(
    alias="Text",
    table_name="TextTable",
    properties=[
        Property(column="H-ID", alias="id"),
        Property(column="preferred_name", alias="name"),
        Property(column="language_COLUMN", alias="language"),
        Property(column="literary_form", alias="form"),
        Property(column="is_hypothetical", method=SQLTransformer.boolean),
        Property(column="claim_freetext", alias="hypothesis"),
        Property(column="alternative_names"),
        Property(
            column="peripheral", alias="is_peripheral", method=SQLTransformer.boolean
        ),
        Property(column="length"),
        Property(column="length_freetext"),
        Property(column="verse_type"),
        Property(column="rhyme_type"),
        Property(column="Stanza_type", alias="stanza_type"),
        Property(column="tradition_status"),
        Property(column="has_lost_older_version", method=SQLTransformer.boolean),
        Property(
            column="ancient_translations_freetext", alias="lost_older_version_freetext"
        ),
        Property(column="rewritings_freetext"),
        Property(column="note"),
        Property(
            column="date_of_creation",
            alias="creation_date",
            method=SQLTransformer.temporal,
        ),
        Property(column="date_of_creation_certainty", alias="creation_date_certainty"),
        Property(column="date_freetext", alias="creation_date_freetext"),
        Property(column="described_at_URL", alias="urls"),
    ],
)
