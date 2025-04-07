from pathlib import Path

import yaml

config_file = Path("config.yml")
with open(config_file, mode="r") as f:
    config = yaml.safe_load(f)

CONTRIBUTORS = config["contributors"]
HEURIST_DB = config["file paths"]["heurist database"]
KUZU_DB = config["file paths"]["graph database"]
OUTDIR_PATH = config["file paths"]["output directory"]

TEXT_TEI_MODEL = Path.cwd().joinpath("tei_base_text.xml")
