from .country import Country
from .document import Document
from .genre import Genre
from .language import Language
from .part import Part
from .person import Person
from .physDesc import PhysDesc
from .place import Place
from .repository import Repository
from .scripta import Scripta
from .story import Story
from .storyverse import Storyverse
from .text import Text
from .tradition_status import TraditionStatus
from .witness import Witness

ALL_ENTITIES = [
    Genre,
    Language,
    Person,
    Story,
    Storyverse,
    Text,
    TraditionStatus,
    Witness,
    Scripta,
    Part,
    Document,
    Repository,
    Place,
    Country,
    PhysDesc,
]
