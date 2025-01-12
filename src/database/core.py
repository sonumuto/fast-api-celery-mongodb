from motor.motor_asyncio import AsyncIOMotorClient

class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]

    async def close(self):
        self.client.close()

MONGO_URI = "mongodb://mongodb:27017"
DB_NAME = "books_api"

mongodb = MongoDB(MONGO_URI, DB_NAME)

def get_db():
    return mongodb.db
