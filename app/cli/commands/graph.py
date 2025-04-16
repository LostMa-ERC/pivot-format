import shutil
from pathlib import Path

import kuzu
import rich
import rich.text
from rich.progress import Progress, SpinnerColumn, TextColumn

from app import CONFIG_DIR, HEURIST_DB, KUZU_DB
from app.sql_to_graph import (
    create_kuzu_database_from_config,
    dump_relational_database_to_config,
)


def build_graph() -> kuzu.Connection:
    if not Path(HEURIST_DB).is_file():
        rich.print(rich.text.Text("Error.", style="red"))
        rich.print(f"No downloaded database file at '{HEURIST_DB}'.")
        rich.print("Run the command 'lostma-tei heurist download'.")
        rich.print("Exiting...")
        exit()

    with Progress(TextColumn("{task.description}"), SpinnerColumn()) as p:
        _ = p.add_task("Rebuilding Kùzu database")
        if Path(KUZU_DB).is_dir():
            shutil.rmtree(KUZU_DB)
        db = kuzu.Database(KUZU_DB)
        kconn = kuzu.Connection(db)
        config = dump_relational_database_to_config(
            duckdb_file=HEURIST_DB, output_dir=CONFIG_DIR
        )
        create_kuzu_database_from_config(config=config, conn=kconn)

    return kconn
