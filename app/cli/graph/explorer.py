import click
from pathlib import Path
from app import KUZU_DB
import subprocess


@click.command("explorer")
def run_kuzu_explorer():
    db = Path(KUZU_DB).absolute()
    command = f"""docker run -p 8000:8000 \
-v {db}:/database \
-e MODE=READ_ONLY \
--rm kuzudb/explorer:latest"""
    subprocess.call(command, shell=True)
