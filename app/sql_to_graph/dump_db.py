import json
from pathlib import Path

import duckdb
import pyarrow.parquet as pq

from app import HEURIST_DB
from app.graph import edges, nodes
from app.sql import entities, relations

from .constants import CYPHER_CONFIG_FILENAME

NODES = [
    (entities.Genre, nodes.Genre),
    (entities.Language, nodes.Language),
    (entities.Person, nodes.Person),
    (entities.Story, nodes.Story),
    (entities.Storyverse, nodes.Storyverse),
    (entities.Text, nodes.Text),
    (entities.TraditionStatus, nodes.TraditionStatus),
    (entities.Witness, nodes.Witness),
    (entities.Scripta, nodes.Scripta),
    (entities.Part, nodes.Part),
    (entities.Document, nodes.Document),
    (entities.Repository, nodes.Repository),
    (entities.Place, nodes.Place),
    (entities.Country, nodes.Country),
]

EDGES = [
    (relations.HAS_GENRE, edges.HAS_GENRE),
    (relations.HAS_LANGUAGE, edges.HAS_LANGAUGE),
    (relations.HAS_PARENT, edges.HAS_PARENT),
    (relations.HAS_STATUS, edges.HAS_STATUS),
    (relations.IS_ATTRIBUTED_TO, edges.IS_ATTRIBUTED_TO),
    (relations.IS_EXPRESSION_OF, edges.IS_EXPRESSION_OF),
    (relations.IS_MANIFESTATION_OF, edges.IS_MANIFESTATION_OF),
    (relations.IS_MODELED_ON, edges.IS_MODELED_ON),
    (relations.IS_PART_OF, edges.IS_PART_OF),
    (relations.IS_INSCRIBED_ON, edges.IS_INSCRIBED_ON),
    (relations.IS_OBSERVED_ON, edges.IS_OBSERVED_ON),
    (relations.LOCATION, edges.LOCATION),
    (relations.HAS_SCRIPT, edges.HAS_SCRIPT),
]


def dump_relational_database_to_config(
    duckdb_file: str = HEURIST_DB,
    output_dir: Path = Path.cwd().joinpath("tmp"),
) -> dict:
    # Connect to the data source (persistent DuckDB file)
    conn = duckdb.connect(duckdb_file, read_only=True)

    # Set up an empty config and parquet directories
    config = {"nodes": [], "edges": []}
    output_dir.mkdir(exist_ok=True, parents=True)
    node_dir = output_dir.joinpath("nodes")
    node_dir.mkdir(exist_ok=True)
    edge_dir = output_dir.joinpath("edges")
    edge_dir.mkdir(exist_ok=True)

    # For each node, save its data and cypher queries
    for sql_entity, graph_node in NODES:

        # From the DuckDB database, write the node's data to a parquet file
        fp = str(
            node_dir.joinpath(f"{graph_node.label}.parquet").relative_to(Path.cwd())
        )
        try:
            rel = conn.sql(sql_entity.query)
        except Exception as e:
            print(sql_entity.query)
            raise e
        rel.write_parquet(fp)

        # Save the node's cypher queries in the config
        config["nodes"].append(
            {
                "label": graph_node.label,
                "cypher": {
                    "create": graph_node.create_table_stmt(),
                    "copy": f"COPY {graph_node.label} FROM '{fp}';",
                },
            }
        )

    # For each edge, save its data and cypher queries
    for sql_relation, graph_edge in EDGES:

        copy_stmts = []

        # For each from-to pair in the edge, write the data to a parquet file
        for selector in sql_relation.selectors:
            try:
                rel = conn.sql(selector.query)
            except Exception as e:
                print(selector.query)
                raise e
            data = rel.to_arrow_table()
            stem = f"{graph_edge.label}_FROM-{selector.from_node}_TO-{selector.to_node}"
            fp = str(edge_dir.joinpath(f"{stem}.parquet").relative_to(Path.cwd()))
            pq.write_table(table=data, where=fp)

            # Update the list of copy statements with this pair's data and file path
            stmt = graph_edge.copy_stmt(
                from_node=selector.from_node, to_node=selector.to_node, fp=fp
            )
            copy_stmts.append(stmt)

        # Save the edge's cypher queries in the config
        config["edges"].append(
            {
                "label": sql_entity.alias,
                "cypher": {
                    "create": graph_edge.create_table_stmt(),
                    "copy": copy_stmts,
                },
            }
        )

    config_fp = output_dir.joinpath(CYPHER_CONFIG_FILENAME)
    with open(config_fp, "w") as f:
        json.dump(config, f, indent=4)

    return config
