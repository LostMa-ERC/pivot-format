from enum import Enum


class SQLTransformer:

    @staticmethod
    def standard(column: str) -> str:
        return f'"{column}"'

    @staticmethod
    def boolean(column: str) -> str:
        return f"""CASE WHEN "{column}" LIKE 'Yes' THEN True ELSE False END"""

    @staticmethod
    def temporal(column: str) -> str:
        s = f"""
            'start_earliest': DATETRUNC('day', CAST({column}.start.earliest AS \
TIMESTAMP)),
            'start_latest': DATETRUNC('day', CAST({column}.start.latest AS TIMESTAMP)),
            'start_prob': CAST({column}.start.estProfile AS VARCHAR),
            'start_cert': CAST({column}.start.estDetermination AS VARCHAR),
            'end_earliest': DATETRUNC('day', CAST({column}.end.earliest AS TIMESTAMP)),
            'end_latest': DATETRUNC('day', CAST({column}.end.latest AS TIMESTAMP)),
            'end_prob': CAST({column}.end.estProfile AS VARCHAR),
            'end_cert': CAST({column}.end.estDetermination AS VARCHAR),
            'timestamp_year': DATETRUNC('day', CAST({column}.timestamp.in AS TIMESTAMP\
)),
            'timestamp_type': CAST({column}.timestamp.type AS VARCHAR),
            'timestamp_circa': CAST({column}.timestamp.circa AS BOOL),
            'est_min': DATETRUNC('day', CAST({column}.estMinDate AS TIMESTAMP)),
            'est_max': DATETRUNC('day', CAST({column}.estMaxDate AS TIMESTAMP)),
            'est_prob': CAST({column}.estProfile AS VARCHAR),
            'est_cert': CAST({column}.estDetermination AS VARCHAR)
"""
        return f"""CASE WHEN "{column}" IS NULL THEN NULL ELSE {{{s}}} END"""


METHODS = {
    repr(func): func
    for func in dir(SQLTransformer)
    if callable(getattr(SQLTransformer, func))
}

Methods = Enum("Methods", METHODS)
