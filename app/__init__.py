from pathlib import Path

import yaml

from base_tei import TEXT_TEI_MODEL

config_file = Path("config.yml")
with open(config_file, mode="r") as f:
    config = yaml.safe_load(f)

CONTRIBUTORS = config["contributors"]
HEURIST_DB = config["file paths"]["heurist database"]
KUZU_DB = config["file paths"]["graph database"]
OUTDIR_PATH = config["file paths"]["output directory"]

if not TEXT_TEI_MODEL.is_file():
    raise FileNotFoundError()
