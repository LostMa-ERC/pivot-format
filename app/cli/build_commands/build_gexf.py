import click

from app.cli.build_commands.build_graph import build_command
from app.utils.write_gexf import write_gexf


@click.command("gexf", help="Transform the graph database into a GEXF file.")
@click.option("-n", "--node", multiple=True, type=click.STRING)
@click.argument("outfile")
def build_gexf(outfile: str, node: tuple[str]):
    kconn = build_command()
    if not node:
        query = "MATCH (n)-[r]->(m) RETURN n,r,m"
    else:
        nodes = ":".join(node)
        query = f"MATCH (n:{nodes})-[]->() RETURN *"
    res = kconn.execute(query=query)
    write_gexf(res=res, filepath=outfile)
