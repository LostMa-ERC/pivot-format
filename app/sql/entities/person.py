from app.sql.entities.core import Entity, Property

Person = Entity(
    alias="Person",
    properties=[
        Property(column="H-ID", alias="id"),
        Property(column="family_name"),
        Property(column="given_names"),
        Property(column="alternative_names"),
        Property(column="described_at_URL", alias="urls"),
    ],
)
