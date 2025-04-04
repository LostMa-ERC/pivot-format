from app.graph.nodes.utils.node_class import Node
from app.graph.nodes.utils.property_metadata import PropertyMetadata

Text = Node(
    node_label="Text",
    pk="id",
    node_properties=[
        PropertyMetadata(
            property_label="id",
            duckdb_col="H-ID",
            property_type="INT",
        ),
        PropertyMetadata(
            property_label="name",
            duckdb_col="preferred_name",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="language",
            duckdb_col="language_COLUMN",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="form",
            duckdb_col="literary_form",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="is_hypothetical",
            property_type="BOOLEAN",
        ),
        PropertyMetadata(
            property_label="hypothesis",
            duckdb_col="claim_freetext",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="alternative_names",
            property_type="STRING[]",
        ),
        PropertyMetadata(
            property_label="is_peripheral",
            duckdb_col="peripheral",
            property_type="BOOLEAN",
        ),
        PropertyMetadata(
            property_label="length",
            property_type="FLOAT",
        ),
        PropertyMetadata(
            property_label="length_freetext",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="verse_type",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="rhyme_type",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="stanza_type",
            duckdb_col="Stanza_type",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="tradition_status",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="has_lost_older_version",
            property_type="BOOLEAN",
        ),
        PropertyMetadata(
            property_label="lost_older_version_freetext",
            duckdb_col="ancient_translations_freetext",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="rewritings_freetext",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="note",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="creation_date",
            duckdb_col="date_of_creation",
            is_temporal=True,
        ),
        PropertyMetadata(
            property_label="creation_date_certainty",
            duckdb_col="date_of_creation_certainty",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="creation_date_freetext",
            duckdb_col="date_freetext",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="described_at_URL",
            property_type="STRING[]",
        ),
    ],
    duckdb_table="TextTable",
)
