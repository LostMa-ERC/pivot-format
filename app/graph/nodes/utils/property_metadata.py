from .constants import CypherTypes


class PropertyMetadata:
    def __init__(
        self,
        property_label: str,
        property_type: CypherTypes | None = None,
        duckdb_col: str | None = None,
        is_temporal: bool = False,
    ):
        self.property_label = property_label
        if not duckdb_col:
            self.duckdb_col = property_label
        else:
            self.duckdb_col = duckdb_col
        self.is_temporal = is_temporal
        # If the metadata is a Heurist temporal object,
        # create a flat structured data type
        if is_temporal:
            self.property_type = """STRUCT(
start_earliest DATE,
start_latest DATE,
start_prob STRING,
start_cert STRING,
end_earliest DATE,
end_latest DATE,
end_prob STRING,
end_cert STRING,
timestamp_year DATE,
timestamp_type STRING,
timestamp_circa BOOL,
est_min DATE,
est_max DATE,
est_prob STRING,
est_cert STRING
)"""
        else:
            self.property_type = property_type

    @property
    def cypher_alias(self) -> str:
        return f"{self.property_label} {self.property_type}"

    @property
    def sql_alias(self) -> str:
        if self.is_temporal:
            s = f"""
'start_earliest': DATETRUNC('day', CAST({self.duckdb_col}.start.earliest AS TIMESTAMP)),
'start_latest': DATETRUNC('day', CAST({self.duckdb_col}.start.latest AS TIMESTAMP)),
'start_prob': CAST({self.duckdb_col}.start.estProfile AS VARCHAR),
'start_cert': CAST({self.duckdb_col}.start.estDetermination AS VARCHAR),
'end_earliest': DATETRUNC('day', CAST({self.duckdb_col}.end.earliest AS TIMESTAMP)),
'end_latest': DATETRUNC('day', CAST({self.duckdb_col}.end.latest AS TIMESTAMP)),
'end_prob': CAST({self.duckdb_col}.end.estProfile AS VARCHAR),
'end_cert': CAST({self.duckdb_col}.end.estDetermination AS VARCHAR),
'timestamp_year': DATETRUNC('day', CAST({self.duckdb_col}.timestamp.in AS TIMESTAMP)),
'timestamp_type': CAST({self.duckdb_col}.timestamp.type AS VARCHAR),
'timestamp_circa': CAST({self.duckdb_col}.timestamp.circa AS BOOL),
'est_min': DATETRUNC('day', CAST({self.duckdb_col}.estMinDate AS TIMESTAMP)),
'est_max': DATETRUNC('day', CAST({self.duckdb_col}.estMaxDate AS TIMESTAMP)),
'est_prob': CAST({self.duckdb_col}.estProfile AS VARCHAR),
'est_cert': CAST({self.duckdb_col}.estDetermination AS VARCHAR)
"""
            return f"""
            CASE WHEN "{self.duckdb_col}" IS NULL THEN NULL ELSE {{{s}}}
            END AS {self.property_label}"""
        elif self.property_type == "BOOLEAN":
            return f"""
CASE WHEN "{self.duckdb_col}" LIKE 'Yes' THEN True ELSE False
END AS {self.property_label}
"""
        else:
            return f'"{self.duckdb_col}" AS {self.property_label}'
