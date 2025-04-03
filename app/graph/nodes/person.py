from app.graph.nodes.utils.node_class import Node
from app.graph.nodes.utils.property_metadata import PropertyMetadata


Person = Node(
    table_name="Person",
    pk="id",
    metadata=[
        PropertyMetadata(
            label="id",
            col="H-ID",
            type="INT",
        ),
        PropertyMetadata(
            label="family_name",
            col="family_name",
            type="STRING",
        ),
        PropertyMetadata(
            label="given_name",
            col="given_names",
            type="STRING",
        ),
        PropertyMetadata(
            label="alternative_names",
            col="alternative_names",
            type="STRING[]",
        ),
        PropertyMetadata(
            label="urls",
            col="described_at_URL",
            type="STRING[]",
        ),
    ],
    table="Person",
)
