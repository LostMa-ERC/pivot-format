from app.graph.nodes.utils.node_class import Node
from app.graph.nodes.utils.property_metadata import PropertyMetadata

Person = Node(
    node_label="Person",
    pk="id",
    node_properties=[
        PropertyMetadata(
            property_label="id",
            duckdb_col="H-ID",
            property_type="INT",
        ),
        PropertyMetadata(
            property_label="family_name",
            duckdb_col="family_name",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="given_name",
            duckdb_col="given_names",
            property_type="STRING",
        ),
        PropertyMetadata(
            property_label="alternative_names",
            duckdb_col="alternative_names",
            property_type="STRING[]",
        ),
        PropertyMetadata(
            property_label="urls",
            duckdb_col="described_at_URL",
            property_type="STRING[]",
        ),
    ],
    duckdb_table="Person",
)
