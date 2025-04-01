# Pivot Heurist database to TEI documents
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

From the relational entities in LostMa's Heurist database, this package (1) transforms the data into a graph network and (2) generates TEI documents, based at the level of a Text.

## Table of contents

- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Advanced Usage](./docs/cli_commands.md)
- [Development](./docs/Contributor.md)
- [License](#license)

## Installation

1. Create and activate a virtual Python environment. (version 3.12)

2. Download this project's code. `git clone https://github.com/LostMa-ERC/pivot-format.git`

3. Change to the downloaded project directory. `cd pivot-format`

4. Install the project as a Python package.

```console
$ pip install .
```

## Basic Usage

_Optional: [Confirm](./docs/configure_project.md) the project's metadata in the [config YAML](./config.yml)._

Run the full workflow, providing your Heurist username (i.e. `"user.name"`) and password (i.e. `"pass"`) for downloading up-to-date data.

```console
$ lostma workflow --username "user.name" --password "pass"
```

> Currently, the workflow downloads data from Heurist and transforms it into an embedded graph database ([Kùzu](https://kuzudb.com/)). The goal is to have the workflow finish with the generation of TEI-XML files, but this last step is still in development.


## License

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

Attribution-ShareAlike 4.0 International.
