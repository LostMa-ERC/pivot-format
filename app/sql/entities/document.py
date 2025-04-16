from app.sql.entities.core import Entity, Property, SQLTransformer

Document = Entity(
    alias="Document",
    table_name="DocumentTable",
    properties=[
        Property(column="H-ID", alias="id"),
        Property(column="current_shelfmark", alias="shelfmark"),
        Property(column="collection"),
        Property(column="invented_label"),
        Property(column="is_hypothetical", method=SQLTransformer.boolean),
        Property(column="claim_freetext", alias="hypothesis"),
        Property(
            column="collection_of_fragments",
            alias="is_collection_of_fragments",
            method=SQLTransformer.boolean,
        ),
        Property(column="old_shelfmark"),
        Property(column="described_at_URL", alias="urls"),
        Property(column="online_catalogue_URL", alias="catalogue_record"),
        Property(column="ARK", alias="ark"),
    ],
)
