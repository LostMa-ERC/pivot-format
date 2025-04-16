from app.sql.entities.core import Entity, Property

Scripta = Entity(
    alias="Scripta",
    properties=[
        Property(column="H-ID", alias="id"),
        Property(column="preferred_name", alias="name"),
        Property(column="description"),
        Property(column="region_note"),
        Property(column="described_at_URL", alias="urls"),
    ],
)
