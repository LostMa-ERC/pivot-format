from lxml import etree

from app.tei.data.witness.document import CompiledDocumentModel


def make_msDesc_msIdentifier(document_data: CompiledDocumentModel) -> etree.Element:
    # Add generic information about the document and its location
    msIdentifier = etree.Element("msIdentifier")
    msIdentifier.set("ref", f"#{document_data.document.xml_id}")
    country = etree.SubElement(msIdentifier, "country")
    settlement = etree.SubElement(msIdentifier, "settlement")
    if document_data.place and document_data.place.region:
        region = etree.SubElement(msIdentifier, "region")
        region.text = document_data.place.region
    repository = etree.SubElement(msIdentifier, "repository")
    if document_data.document.collection:
        collection = etree.SubElement(msIdentifier, "collection")
        collection.text = document_data.document.collection
    idno = etree.SubElement(msIdentifier, "idno")
    idno.text = document_data.document.shelfmark
    for old_shelfmark in document_data.document.old_shelfmark:
        altIdentifier = etree.SubElement(msIdentifier, "altIdentifier")
        altIdentifier.text = old_shelfmark
    # If the geographic information is known, update the generic XML tags
    if document_data.place:
        country.text = document_data.place.country.name
        country.set("ref", f"#{document_data.place.country.code}")
        settlement.text = document_data.place.name
        repository.set("ref", f"#{document_data.repository.xml_id}")
        repository.text = document_data.repository.name
    for url in document_data.document.urls:
        etree.SubElement(msIdentifier, "ref", target=url)

    return msIdentifier
