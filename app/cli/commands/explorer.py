import subprocess
from pathlib import Path

from app import KUZU_DB


def run_kuzu_explorer(write: bool):
    db = Path(KUZU_DB)
    if not db.is_dir():
        raise NotADirectoryError(db)
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
