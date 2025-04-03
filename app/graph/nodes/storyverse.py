from app.graph.nodes.utils.node_class import Node
from app.graph.nodes.utils.property_metadata import PropertyMetadata


Storyverse = Node(
    table_name="Storyverse",
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
            label="described_at_URL",
            type="STRING[]",
        ),
    ],
    table="Storyverse",
)
