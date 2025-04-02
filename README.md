# Pivot Heurist database to TEI documents
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

From the relational entities in LostMa's Heurist database, this package (1) transforms the data into a graph network and (2) generates TEI documents, based at the level of a Text.

## Table of contents

- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Advanced Usage](./docs/README.md)
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

The last step of the full workflow is the generation of TEI-XML documents for each text entered into the graph database. You can find them in the output directory, which is specified in the [config YAML](./config.yml).

```console
$ lostma workflow
Get DB Structure ⠼ 0:00:00
Get Records ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 25/25 0:00:11
Rebuilding Kùzu database ⠋
Writing text documents... ━━━━━━━━━━━━━━━━━━ 0:00:15 517/517

```

Once the workflow has run (the graph database has been built), consider exploring the networked data with the command `lostma explorer`. See [this section](./docs/explore_network.md) for details.

![Screenshot of Kuzu Explorer schema view](./docs/img/kuzu_explorer.png)


## License

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

Attribution-ShareAlike 4.0 International.
