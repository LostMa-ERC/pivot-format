from app.sql.entities.core import Entity, Property

Genre = Entity(
    alias="Genre",
    properties=[
        Property(column="H-ID", alias="id"),
        Property(column="preferred_name", alias="name"),
        Property(column="alternative_names"),
        Property(column="description"),
        Property(column="described_at_URL", alias="urls"),
    ],
)
