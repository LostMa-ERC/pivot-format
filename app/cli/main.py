import click
import importlib.metadata

# from app.cli.pivot import pivot
from app.cli.build_commands import build
from app.cli.explorer import run_kuzu_explorer

__identifier__ = importlib.metadata.version("lostma-tei")


@click.group()
@click.version_option(__identifier__)
def cli():
    pass


if __name__ == "__main__":
    cli()


cli.add_command(build)
cli.add_command(run_kuzu_explorer)
# cli.add_command(pivot)
