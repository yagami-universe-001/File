from datetime import datetime
import motor.motor_asyncio
from config.settings import Config

class DatabaseManager:
    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(Config.DATABASE_URL)
        self.db = self.client[Config.DB_NAME]
        self.users = self.db.users
        self.thumbnails = self.db.thumbnails
        self.queue = self.db.queue
        self.premium_users = self.db.premium_users

    async def add_user(self, user_id, username, first_name):
        await self.users.update_one(
            {"user_id": user_id},
            {"$set": {"username": username, "first_name": first_name, "last_seen": datetime.now()},
             "$setOnInsert": {"joined_date": datetime.now(), "total_encodes": 0}},
            upsert=True)
    # ... (complete with all necessary db methods for thumbnails, queue, premium, etc) ...
