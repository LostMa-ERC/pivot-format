from app.sql.entities.core import Entity, Property

PhysDesc = Entity(
    alias="PhysDesc",
    properties=[
        Property(column="H-ID", alias="id"),
        Property(column="material"),
        Property(column="form"),
        Property(column="folio_size_width"),
        Property(column="folio_size_height"),
        Property(column="estimated_folio_size_height"),
        Property(column="estimated_folio_size_width"),
        Property(column="has_decorations"),
        Property(column="amount_of_illustrations"),
        Property(column="writing_surface_area_height"),
        Property(column="writing_surface_area_width"),
        Property(column="number_of_columns"),
        Property(column="number_of_lines_in_writing_area"),
        Property(column="above_top_line"),
        Property(column="script_type"),
        Property(column="subscript_type"),
    ],
)
