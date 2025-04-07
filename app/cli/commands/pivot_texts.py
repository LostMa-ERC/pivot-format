import shutil
from pathlib import Path

import kuzu
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    TextColumn,
    TimeElapsedColumn,
)

from app import KUZU_DB, OUTDIR_PATH
from app.tei.builders.text.encodingDesc import build_encondingDesc
from app.tei.parsers.text_tree import TextXMLTree
from app.tei.text_builder import TextDocument

OUTDIR = Path(OUTDIR_PATH)


def get_all_texts(conn: kuzu.Connection) -> list[int]:
    response = conn.execute("MATCH (t:Text) RETURN t.id ORDER BY t.id")
    ids = []
    while response.has_next():
        ids.append(response.get_next()[0])
    return ids


def pivot_all_texts_to_tei():
    if not Path(KUZU_DB).is_dir():
        raise NotADirectoryError()
    # Connect to Kuzu database
    db = kuzu.Database(KUZU_DB, read_only=True)
    conn = kuzu.Connection(db)
    # Get texts
    texts = get_all_texts(conn=conn)
    # Prepare the output directory
    if OUTDIR.is_dir():
        shutil.rmtree(OUTDIR)
    assert not OUTDIR.is_dir()
    OUTDIR.mkdir()

    # Build the standard encodingDesc, which applies to all documents
    encodingDesc = build_encondingDesc(conn=conn, root=TextXMLTree().encodingDesc)

    # Build each text's TEI document
    with Progress(
        TextColumn("{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
        MofNCompleteColumn(),
    ) as p:
        t = p.add_task("Writing text documents...", total=len(texts))
        for i in texts:
            stem = f"text_{i}.xml"
            doc = TextDocument(conn=conn, text_id=i, encodingDesc_node=encodingDesc)
            subdir = OUTDIR.joinpath("null")
            if doc.lang.code != "":
                subdir = OUTDIR.joinpath(doc.lang.code)
            else:
                subdir = OUTDIR.joinpath("null")
            subdir.mkdir(exist_ok=True)
            doc.write(outfile=subdir.joinpath(stem))
            p.advance(t)
