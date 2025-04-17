from app.sql.entities.core import Entity, Property

Repository = Entity(
    alias="Repository",
    properties=[
        Property(column="H-ID", alias="id"),
        Property(column="preferred_name", alias="name"),
        Property(column="alternative_names"),
        Property(column="VIAF", alias="viaf"),
        Property(column="ISNI", alias="isni"),
        Property(column="biblissima_identifier"),
        Property(column="website"),
    ],
)
