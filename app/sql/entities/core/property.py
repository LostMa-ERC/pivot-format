from dataclasses import dataclass

from .transformers import Methods, SQLTransformer


@dataclass
class Property:
    """Metadata about the property of a relational entity.

    Attributes:
        column (str): Name of the column on the entity's table.
        alias (str | None, optional): If the name desired for the output format is\
            different than the column name, an alias, i.e. '"column" AS "alias"'.\
            Defaults to column name.
        method (classmethod | None, optional): ...
    """

    column: str
    alias: str | None = None
    method: Methods = SQLTransformer.standard

    def __post_init__(self):
        # If missing, set the alias
        if not self.alias:
            object.__setattr__(self, "alias", self.column)

        # Edit the selection
        selection = self.method(self.column)
        object.__setattr__(self, "column", selection)
