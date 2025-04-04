from app.graph.nodes.utils.node_class import Node
from app.graph.nodes.utils.property_metadata import PropertyMetadata

Story = Node(
    node_label="Story",
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
            property_label="alternative_names",
            property_type="STRING[]",
        ),
        PropertyMetadata(
            property_label="matter",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="peripheral",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="described_at_URL",
            property_type="STRING[]",
        ),
    ],
    duckdb_table="Story",
)
