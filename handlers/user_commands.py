from database.db_manager import DatabaseManager
db = DatabaseManager()

async def start(update, context):
    await update.message.reply_text("Welcome to the Video Encoder Bot!")

async def help_command(update, context):
    await update.message.reply_text("Help message with command list.")

async def set_thumbnail(update, context):
    await update.message.reply_text('Send a photo for thumbnail...')
# ...get_thumbnail, delete_thumbnail, set_watermark, get_watermark, etc...
