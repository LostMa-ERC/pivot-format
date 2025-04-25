from neo4j import Driver


def create_neo4j_database_from_config(config: dict, driver: Driver) -> None:
    # Reset the database, removing any nodes
    driver.execute_query("MATCH (n) DETACH DELETE n")

    for node in config["nodes"]:
        queries = node["cypher"]["neo4j"]

        # Set up the node's primary key constraint
        constraint_label = queries["constraint_label"]
        driver.execute_query(f"DROP CONSTRAINT {constraint_label} IF EXISTS")
        driver.execute_query(queries["create_constraint"])

        # Create the individual nodes
        stmt = queries["create_nodes"]
        data = node["items"]

        def fix_data(data: list[dict]) -> list[dict]:
            new_data = {"data": []}
            items = data["data"]
            for i in items:
                new_dict = {}
                for k, v in i.items():
                    if isinstance(v, dict):
                        if v["timestamp_year"] is not None:
                            v = [v["timestamp_year"]]
                        elif v["est_min"] is not None and v["est_max"] is not None:
                            v = [v["est_min"], v["est_max"]]
                        elif v["est_min"] is not None:
                            v = [v["est_min"]]
                        else:
                            v = None
                    new_dict.update({k: v})
                new_data["data"].append(new_dict)
            return new_data

        data = fix_data(data)

        records, summary, _ = driver.execute_query(stmt, parameters_=data)

    # for edge in config["edges"]:
    #     queries = edge["cypher"]
    #     conn.execute(query=queries["create"])
    #     for copy_data in queries["copy"]:
    #         try:
    #             conn.execute(copy_data)
    #         except Exception as e:
    #             print(queries)
    #             raise e
