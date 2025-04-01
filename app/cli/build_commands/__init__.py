import click

from .build_gexf import build_gexf_command
from .build_graph import build_graph_command
from .heurist_download import build_heurist_command


@click.group("build", help="[SUBCOMMANDS] Build database files.")
def build():
    pass


build.add_command(build_gexf_command)
build.add_command(build_graph_command)
build.add_command(build_heurist_command)
