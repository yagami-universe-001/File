import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    ADMIN_IDS = [int(i) for i in os.getenv("ADMIN_IDS", "").split()]
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    DB_NAME = os.getenv("DB_NAME", "video_encoder_bot")

    @classmethod
    def create_directories(cls):
        for directory in ["downloads", "outputs", "thumbnails"]:
            os.makedirs(directory, exist_ok=True)
Config.create_directories()
