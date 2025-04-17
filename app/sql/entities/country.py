from app.sql.entities.core import Entity

Country = Entity(
    alias="Country",
    query="""
SELECT
    trm_ID as id,
    trm_Label as name,
    trm_Code as code
FROM trm
WHERE trm_ParentTermID = 509
""",
)
