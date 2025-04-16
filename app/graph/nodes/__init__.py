from app.graph.nodes.document import Document
from app.graph.nodes.genre import Genre
from app.graph.nodes.language import Language
from app.graph.nodes.part import Part
from app.graph.nodes.person import Person
from app.graph.nodes.scripta import Scripta
from app.graph.nodes.story import Story
from app.graph.nodes.storyverse import Storyverse
from app.graph.nodes.text import Text
from app.graph.nodes.tradition_status import TraditionStatus
from app.graph.nodes.witness import Witness

ALL_NODES = [
    Story,
    Storyverse,
    Text,
    Language,
    Genre,
    Witness,
    Person,
    TraditionStatus,
    Scripta,
    Part,
    Document,
]
