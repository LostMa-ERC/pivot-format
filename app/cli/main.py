import importlib.metadata

import click

from app.cli.commands import WORKFLOW_CHOICES
from app.cli.commands.explorer import run_kuzu_explorer
from app.cli.commands.graph import build_graph
from app.cli.commands.heurist import heurist_download
from app.cli.commands.pivot_texts import pivot_all_texts_to_tei
from app.cli.commands.workflow import run_workflow

__identifier__ = importlib.metadata.version("lostma-tei")


@click.group()
@click.version_option(__identifier__)
def cli():
    pass


@cli.command(
    "heurist",
    help="Download Heurist data and transform it into a DuckDB database.",
)
@click.option("-l", "--login", type=click.STRING, required=False)
@click.option("-p", "--password", type=click.STRING, required=False)
def command_download_heurist(login, password):
    heurist_download(login=login, password=password)


@cli.command(
    "graph",
    help="Build the Heurist data into a graph database.",
)
def command_build_graph():
    build_graph()


@cli.command(
    "tei",
    help="Pivot all the texts to TEI documents.",
)
def command_build_tei():
    pivot_all_texts_to_tei()


@cli.command("workflow", help="Run the full workflow.")
@click.option("-l", "--login", type=click.STRING, required=False)
@click.option("-p", "--password", type=click.STRING, required=False)
@click.option(
    "-s", "--stop-at-step", type=click.Choice(WORKFLOW_CHOICES), required=False
)
def command_workflow(login: str | None, password: str | None, stop_at_step: str | None):
    run_workflow(login=login, password=password, stop_at_step=stop_at_step)


@cli.command(
    "explorer",
    help="With Docker running, launch Kùzu Explorer.",
)
@click.option(
    "--write",
    default=False,
    is_flag=True,
    show_default=True,
    help="Allow edits to the database.",
)
def command_run_kuzu_explorer(write: bool):
    run_kuzu_explorer(write=write)


if __name__ == "__main__":
    cli()
