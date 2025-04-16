from app.sql.entities.core import Entity

Language = Entity(
    alias="Language",
    query="""
SELECT
    trm_ID AS id,
    trm_Label AS name,
    trm_Code AS code,
    trm_Description AS description,
    trm_SemanticReferenceURL AS url
FROM trm
WHERE trm_ParentTermID = 9469
""",
)
