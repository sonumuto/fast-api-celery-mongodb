from .models import Book

# CREATE #


async def create(book: Book):
    """Create a new book."""
    await book.insert_document()
    return book

# READ #


async def read(name: str):
    """Read a book."""
    return await Book.find_one({"name": name})
