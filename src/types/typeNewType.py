from typing import NewType
from dataclasses import dataclass


@dataclass
class Document:
    is_filled: bool


DocumentFill = NewType('DocumentFill', Document)


def send_document(document: DocumentFill) -> str:
    return 'Document was sent'


send_document(DocumentFill(Document(True)))
