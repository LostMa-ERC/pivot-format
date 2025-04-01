import click
import duckdb
from dotenv import find_dotenv, load_dotenv
import os

from app import HEURIST_DB
from heurist.api.client import HeuristAPIClient
from heurist.workflows.etl import extract_transform_load

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


def download(login: str | None, password: str | None):
    kwargs = get_vars(login, password)
    client = HeuristAPIClient(**kwargs)
    conn = duckdb.connect(HEURIST_DB)
    extract_transform_load(
        client=client, duckdb_connection=conn, record_group_names=RECORD_GROUP_NAMES
    )


@click.command(
    "heurist",
    help="Download Heurist data and transform it into a DuckDB database.",
)
@click.option("-l", "--login", type=click.STRING, required=False)
@click.option("-p", "--password", type=click.STRING, required=False)
def build_heurist_command(login, password):
    download(login=login, password=password)
