import click

from .build_gexf import build_gexf
from .build_graph import build_graph
from .explorer import run_kuzu_explorer


@click.group("graph")
def graph():
    pass


graph.add_command(build_gexf)
graph.add_command(build_graph)
graph.add_command(run_kuzu_explorer)
