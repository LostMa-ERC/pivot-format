from enum import Enum


class Type(Enum):
    boolean = "BOOLEAN"
    date = "DATE"
    dates = "DATE[]"
    duration = "DURATION"
    float = "FLOAT"
    float_list = "FLOAT[]"
    int = "INT"
    ints = "INT[]"
    map = "MAP"
    point = "POINT"
    string = "STRING"
    string_list = "STRING[]"
    struct = "STRUCT"
    temporal = """STRUCT(
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
