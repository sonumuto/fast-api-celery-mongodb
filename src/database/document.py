from pydantic import BaseModel
from src.database.core import get_db

class Document(BaseModel):
    """Document model."""

    @classmethod
    def get_collection(cls):
        return get_db().get_collection(cls.Config.collection)

    @classmethod
    async def insert_one(cls, document: dict):
        collection = cls.get_collection()
        result = await collection.insert_one(document)
        return result.inserted_id

    @classmethod
    async def find_one(cls, query: dict):
        collection = cls.get_collection()
        return await collection.find_one(query)

    async def insert_document(self):
        model = self.model_dump()
        return await self.insert_one(model)

    class Config:
        collection = "documents"
