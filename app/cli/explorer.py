import click
from pathlib import Path
from app import KUZU_DB
import subprocess
import webbrowser


@click.command("explorer", help="[COMMAND] Launch Kùzu explorer on graph database.")
@click.option(
    "--write",
    default=False,
    is_flag=True,
    show_default=True,
    help="Allow edits to the database.",
)
def run_kuzu_explorer(write: bool):
    db = Path(KUZU_DB)
    if not db.is_dir():
        raise NotADirectoryError(db)
    webbrowser.open("http://localhost:8000", new=2)
    if write:
        command = f"""docker run -p 8000:8000 \
-v {db.absolute()}:/database \
--rm kuzudb/explorer:latest"""
    else:
        command = f"""docker run -p 8000:8000 \
-v {db.absolute()}:/database \
-e MODE=READ_ONLY \
--rm kuzudb/explorer:latest"""
    subprocess.call(command, shell=True)
