from kuzu import Connection


def create_kuzu_database_from_config(config: dict, conn: Connection) -> None:
    for node in config["nodes"]:
        queries = node["cypher"]
        conn.execute(query=queries["create"])
        conn.execute(query=queries["copy"])
    for edge in config["edges"]:
        queries = edge["cypher"]
        conn.execute(query=queries["create"])
        for copy_data in queries["copy"]:
            try:
                conn.execute(copy_data)
            except Exception as e:
                print(queries)
                raise e
