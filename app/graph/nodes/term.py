from app.graph.nodes.utils.node_class import Node
from app.graph.nodes.utils.property_metadata import PropertyMetadata

TERM_METADATA = [
    PropertyMetadata(
        property_label="id",
        property_type="INT",
    ),
    PropertyMetadata(
        property_label="name",
        property_type="STRING",
    ),
    PropertyMetadata(
        property_label="code",
        property_type="STRING",
    ),
    PropertyMetadata(
        property_label="description",
        property_type="STRING",
    ),
    PropertyMetadata(
        property_label="url",
        property_type="STRING",
    ),
]


# 9476 is the parent vocabulary ID for the Tradition Status vocabulary.
# If this changes, change the end of the DuckDB SQL query.
TraditionStatus = Node(
    node_label="TraditionStatus",
    pk="id",
    node_properties=TERM_METADATA,
    duckdb_query="""
    SELECT
        trm_ID as id,
        trm_Label as name,
        trm_Code as code,
        trm_Description as description,
        trm_SemanticReferenceURL as url
    FROM trm
    WHERE trm_ParentTermID = 9476
""",
)


Language = Node(
    node_label="Language",
    pk="id",
    node_properties=TERM_METADATA,
    duckdb_query="""
    SELECT
        trm_ID as id,
        ANY_VALUE(trm_Label) as name,
        ANY_VALUE(trm_Code) as code,
        ANY_VALUE(trm_Description) as description,
        ANY_VALUE(trm_SemanticReferenceURL) as url
    FROM trm
    JOIN TextTable tt ON trm.trm_ID = tt."language_COLUMN TRM-ID"
    GROUP BY trm_ID
""",
)
