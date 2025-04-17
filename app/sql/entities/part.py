from .core import Entity, Property, SQLTransformer

Part = Entity(
    alias="Part",
    properties=[
        Property(column="H-ID", alias="id"),
        Property(column="div_order"),
        Property(column="number_of_verses"),
        Property(column="part_of_text"),
        Property(column="volume_number"),
        Property(column="number_of_lines"),
        Property(column="verses_per_line"),
        Property(column="lines_are_incomplete", method=SQLTransformer.boolean),
        Property(column="page_ranges"),
    ],
)
