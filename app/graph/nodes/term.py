from app.graph.nodes.utils.node_class import Node
from app.graph.nodes.utils.property_metadata import PropertyMetadata

TERM_METADATA = [
    PropertyMetadata(
        label="id",
        type="INT",
    ),
    PropertyMetadata(
        label="name",
        type="STRING",
    ),
    PropertyMetadata(
        label="code",
        type="STRING",
    ),
    PropertyMetadata(
        label="description",
        type="STRING",
    ),
    PropertyMetadata(
        label="url",
        type="STRING",
    ),
]


# 9476 is the parent vocabulary ID for the Tradition Status vocabulary.
# If this changes, change the end of the DuckDB SQL query.
TraditionStatus = Node(
    table_name="TraditionStatus",
    pk="id",
    metadata=TERM_METADATA,
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
    table_name="Language",
    pk="id",
    metadata=TERM_METADATA,
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
