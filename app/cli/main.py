import click
import importlib.metadata

from app.cli.pivot_texts import pivot_all_texts
from app.cli.build_commands import build
from app.cli.build_commands.heurist_download import download
from app.cli.build_commands.build_graph import build_graph
from app.cli.explorer import run_kuzu_explorer

__identifier__ = importlib.metadata.version("lostma-tei")


@click.group()
@click.version_option(__identifier__)
def cli():
    pass


@cli.command("workflow", help="[COMMAND] Run the full workflow.")
@click.option("-l", "--login", type=click.STRING, required=False)
@click.option("-p", "--password", type=click.STRING, required=False)
def run_workflow(login, password):
    download(login=login, password=password)
    build_graph()


if __name__ == "__main__":
    cli()

cli.add_command(build)
cli.add_command(run_kuzu_explorer)
cli.add_command(pivot_all_texts)
