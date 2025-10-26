from telegram import Update
from config.settings import Config
from database.db_manager import DatabaseManager

db = DatabaseManager()
def is_admin(user_id: int):
    return user_id in Config.ADMIN_IDS

async def restart_bot(update, context):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("Admins only.")
        return
    await update.message.reply_text("Restart bot manually via your server.")
# ...queue, clear, audio, codec, preset, crf, fsub, shortner, addpaid, listpaid, rempaid, update...
