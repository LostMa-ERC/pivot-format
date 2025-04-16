from app.sql.entities.core import Entity, Property

Storyverse = Entity(
    alias="Storyverse",
    properties=[
        Property(column="H-ID", alias="id"),
        Property(column="preferred_name", alias="name"),
        Property(column="alternative_names"),
        Property(column="described_at_URL", alias="urls"),
    ],
)
