# CLI Commands

You can run the individual components of the workflow as you need using the `lostma` commands.

When running commands individually, respect the order below:

1. Download the latest Heurist data.
    - [`lostma build heurist`](./download_heurist_data.md)
2. Transform the data into a graph.
    - [`lostma build graph`](./transform_into_graph.md)
3. Have fun!
    - [`lostma explorer`](./explore_network.md) : Visualise and query the network in a browser.
    - [`lostma pivot texts`](./pivot_data_to_tei.md): Generate TEI-XML documents.