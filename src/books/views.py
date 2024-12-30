from fastapi import APIRouter, HTTPException
from typing import List
from .models import Book
from .service import (create, read)

router = APIRouter()

@router.get("/{name}", response_model=Book)
async def get(name: str):
    """Get a book."""
    model = await read(name=name)
    return Book(**model)

@router.post("/", response_model=Book)
async def post(book: Book):
    """Create a new book."""
    return await create(book=book)
