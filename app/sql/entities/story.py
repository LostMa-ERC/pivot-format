from app.sql.entities.core import Entity, Property, SQLTransformer

Story = Entity(
    alias="Story",
    properties=[
        Property(column="H-ID", alias="id"),
        Property(column="preferred_name", alias="name"),
        Property(column="alternative_names"),
        Property(column="matter"),
        Property(column="peripheral", method=SQLTransformer.boolean),
        Property(column="described_at_URL", alias="urls"),
    ],
)
