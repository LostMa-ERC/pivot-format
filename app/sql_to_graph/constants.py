from pathlib import Path

CYPHER_CONFIG_FILENAME = "cypher.json"


def get_config(dir: Path) -> Path:
    return dir.joinpath(CYPHER_CONFIG_FILENAME)
