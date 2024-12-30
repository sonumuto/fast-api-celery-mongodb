"""Books models."""
from src.database.document import Document

class Book(Document):
    """Book model."""
    name: str
    author: str

    class Config:
        collection = "books"
