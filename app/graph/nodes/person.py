from app.graph.nodes import Metadata, Node


Person = Node(
    table_name="Person",
    pk="id",
    metadata=[
        Metadata(
            label="id",
            col="H-ID",
            type="INT",
        ),
        Metadata(
            label="family_name",
            col="family_name",
            type="STRING",
        ),
        Metadata(
            label="given_name",
            col="given_names",
            type="STRING",
        ),
        Metadata(
            label="alternative_names",
            col="alternative_names",
            type="STRING[]",
        ),
        Metadata(
            label="urls",
            col="described_at_URL",
            type="STRING[]",
        ),
    ],
    table="Person",
)
