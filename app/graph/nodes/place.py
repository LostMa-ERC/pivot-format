from app.graph import Property, Type

from .core import Node

PLACE_PROPS = [
    Property(name="id", type=Type.int),
    Property(name="name", type=Type.string),
    Property(name="administrative_region", type=Type.string),
    Property(name="country", type=Type.string),
    Property(name="place_type", type=Type.string),
    Property(name="location_mappable", type=Type.string),  # geo point
    Property(name="location_certainty", type=Type.string),
    Property(name="geonames_id", type=Type.int),
]

Place = Node(label="Place", pk="id", properties=PLACE_PROPS)
