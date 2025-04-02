from dataclasses import dataclass

from app import CONTRIBUTORS
from app.tei.data.text.language import LanguageModel


@dataclass
class RespPerson:
    name: str
    role: str


def list_resp_persons(lang: LanguageModel | None) -> list[RespPerson]:

    language_code = getattr(lang, "code", None)
    print(language_code)

    # Start list of people with data entry and proof correction
    # contributors
    languages = CONTRIBUTORS["data entry"]
    if language_code and languages.get(language_code):
        names = languages[language_code]
    else:
        names = languages["default"]
    people = [
        RespPerson(
            name=n,
            role="data entry and proof correction",
        )
        for n in names
    ]

    # Extend list with people responsible for metadata's TEI markup
    people.extend(
        [
            RespPerson(name=n, role="conversion of metadata to TEI markup")
            for n in CONTRIBUTORS["encoding"]["metadata"]
        ]
    )

    # Extend list with people responsible for text transcription's TEI
    # markup
    people.extend(
        [
            RespPerson(name=n, role="conversion of text to TEI markup")
            for n in CONTRIBUTORS["encoding"]["text"]
        ]
    )

    return people
