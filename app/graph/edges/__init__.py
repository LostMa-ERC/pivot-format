from .has_genre import HAS_GENRE
from .has_language import HAS_LANGAUGE
from .has_parent import HAS_PARENT
from .has_status import HAS_STATUS
from .is_attributed_to import IS_ATTRIBUTED_TO
from .is_expression_of import IS_EXPRESSION_OF
from .is_inscribed_on import IS_INSCRIBED_ON
from .is_manifestation_of import IS_MANIFESTATION_OF
from .is_modeled_on import IS_MODELED_ON
from .is_observed_on import IS_OBSERVED_ON
from .is_part_of import IS_PART_OF
from .location import LOCATION

ALL_EDGES = [
    HAS_GENRE,
    HAS_LANGAUGE,
    HAS_PARENT,
    HAS_STATUS,
    IS_ATTRIBUTED_TO,
    IS_EXPRESSION_OF,
    IS_MANIFESTATION_OF,
    IS_MODELED_ON,
    IS_PART_OF,
    IS_INSCRIBED_ON,
    IS_OBSERVED_ON,
    LOCATION,
]
