from app.sql.entities.core import Entity

TraditionStatus = Entity(
    alias="TraditionStatus",
    query="""
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
