from app.sql.entities.core import Entity, Property, SQLTransformer

Witness = Entity(
    alias="Witness",
    properties=[
        Property(column="H-ID", alias="id"),
        Property(column="is_unobserved", method=SQLTransformer.boolean),
        Property(column="claim_freetext", alias="hypothesis"),
        Property(column="preferred_siglum", alias="siglum"),
        Property(column="alternative_sigla"),
        Property(column="status_witness"),
        Property(column="status_notes"),
        Property(column="is_excerpt", method=SQLTransformer.boolean),
        Property(
            column="date_of_creation",
            alias="creation_date",
            method=SQLTransformer.temporal,
        ),
        Property(column="date_of_creation_certainty", alias="creation_date_certainty"),
        Property(column="date_freetext", alias="creation_date_freetext"),
        Property(column="described_at_URL", alias="urls"),
    ],
)
