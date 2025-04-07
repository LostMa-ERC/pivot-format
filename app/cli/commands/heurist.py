import os

import duckdb
from dotenv import find_dotenv, load_dotenv
from heurist.api.client import HeuristAPIClient
from heurist.workflows.etl import extract_transform_load

from app import HEURIST_DB

HEURIST_DATABASE_NAME = "jbcamps_gestes"


def get_vars(*args) -> dict:
    load_dotenv(find_dotenv())
    login, password = args[0], args[1]
    if not login:
        login = os.getenv("DB_LOGIN")
    if not password:
        password = os.getenv("DB_PASSWORD")
    return {
        "database_name": HEURIST_DATABASE_NAME,
        "login": login,
        "password": password,
    }


RECORD_GROUP_NAMES = [
    "My record types",
    "Place, features",
    "People and organisations",
]


def heurist_download(login: str | None, password: str | None):
    kwargs = get_vars(login, password)
    client = HeuristAPIClient(**kwargs)
    conn = duckdb.connect(HEURIST_DB)
    extract_transform_load(
        client=client, duckdb_connection=conn, record_group_names=RECORD_GROUP_NAMES
    )
