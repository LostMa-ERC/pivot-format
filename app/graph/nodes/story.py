from app.graph.nodes.utils.node_class import Node
from app.graph.nodes.utils.property_metadata import PropertyMetadata

Story = Node(
    table_name="Story",
    pk="id",
    metadata=[
        PropertyMetadata(
            label="id",
            col="H-ID",
            type="INT",
        ),
        PropertyMetadata(
            label="name",
            col="preferred_name",
            type="STRING",
        ),
        PropertyMetadata(
            label="alternative_names",
            type="STRING[]",
        ),
        PropertyMetadata(
            label="matter",
            type="STRING",
        ),
        PropertyMetadata(
            label="peripheral",
            type="STRING",
        ),
        PropertyMetadata(
            label="described_at_URL",
            type="STRING[]",
        ),
    ],
    table="Story",
)
