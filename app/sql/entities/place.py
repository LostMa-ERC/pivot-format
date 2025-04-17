from app.sql.entities.core import Entity, Property

Place = Entity(
    alias="Place",
    properties=[
        Property(column="H-ID", alias="id"),
        Property(column="place_name", alias="name"),
        Property(column="administrative_region"),
        Property(column="country"),
        Property(column="place_type"),
        Property(column="location_mappable"),
        Property(column="location_certainty"),
        Property(column="geonames_id"),
    ],
)
