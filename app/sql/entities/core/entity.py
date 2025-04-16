from dataclasses import dataclass, field

from .property import Property


@dataclass
class Entity:
    """Metadata about an entity in a relational SQL database.

    Either enumerate the columns to be selected ('aliases' attribute) or write out the \
        SQL query ('query' attribute).

    Attributes:
        alias (str): Name / filepath stem for the entity in its output format.
        table_name (str | None, optional): If the entity's name in the SQL database\
            is different than the name desired for the output (i.e. parquet file),\
            the name of the SQL table. Defaults to output_name.
        properties (list[Property], optional): If the targeted properties are all on \
            the entity (without joins) and do not require transformation, a list of \
            their column names and--if different--the serialization alias for the \
            output format. If the alias is the same as the column name, alias defaults\
            to column name.
        query (str | None, optional): If the targeted properties require transformation\
            (i.e. conditionals or functions) or a join, the full SQL query. Otherwise, \
            if the selection is simpler, list the properties in the 'aliases' attribute.

    """

    alias: str
    table_name: str | None = None
    properties: list[Property] = field(default_factory=list)
    query: str | None = None

    def __post_init__(self):
        # If the table name inherits from the output name, set the table name
        if not self.table_name:
            object.__setattr__(self, "table_name", self.alias)

        # Confirm that all the required attributes are present
        if not self.query and len(self.properties) == 0:
            raise IndexError
        if len(self.properties) > 0 and not self.table_name:
            raise AttributeError

        # If the query is inferred from the aliases, construct the SQL query
        if not self.query:
            cols = ",\n\t".join([f"{p.column} AS {p.alias}" for p in self.properties])
            query = f"SELECT\n\t{cols}\nFROM {self.table_name};"
            object.__setattr__(self, "query", query)
        elif not self.query.endswith(";"):
            query = f"{self.query};"
            object.__setattr__(self, "query", query)
