import click

from .build_gexf import build_gexf
from .build_graph import build_graph
from .heurist_download import download


@click.group("build", help="[SUBCOMMANDS] Build database files.")
def build():
    pass


build.add_command(build_gexf)
build.add_command(build_graph)
build.add_command(download)
