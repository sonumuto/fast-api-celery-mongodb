from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.books.views import router as books_router

app = FastAPI()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routes
app.include_router(books_router, prefix="/books", tags=["books"])

