from telegram import Update
from telegram.ext import ContextTypes
from config.settings import Config
from database.db_manager import DatabaseManager

db = DatabaseManager()

def is_admin(user_id: int) -> bool:
    return user_id in Config.ADMIN_IDS

async def restart_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("Admins only.")
        return
    await update.message.reply_text(
        """🔄 Bot restart is not available from commands.
You must restart manually on your server or hosting panel."""
    )

async def check_queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("Admins only.")
        return
    queue = await db.get_queue() if hasattr(db, "get_queue") else []
    count = len(queue) if queue else 0
    await update.message.reply_text(f"📋 Current Queue: {count} tasks.")

async def clear_queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("Admins only.")
        return
    cleared = await db.clear_queue() if hasattr(db, "clear_queue") else 0
    await update.message.reply_text(f"✅ Cleared {cleared} tasks from queue.")

async def set_audio_bitrate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("Admins only.")
        return
    await update.message.reply_text(
        "🔊 Set audio bitrate (e.g. /audio 128k)."
    )

async def set_codec(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("Admins only.")
        return
    await update.message.reply_text(
        "🎥 Set video codec: /codec libx264 or /codec libx265"
    )

async def set_preset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("Admins only.")
        return
    await update.message.reply_text(
        "⚙️ Set encoding preset: ultrafast, fast, medium, slow, veryslow (e.g. /preset medium)"
    )

async def set_crf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("Admins only.")
        return
    await update.message.reply_text(
        "🎚️ Set CRF value (0-51), lower is higher quality (e.g. /crf 23)."
    )

async def add_premium_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("Admins only.")
        return
    await update.message.reply_text("👑 Use /addpaid USER_ID DAYS to add a premium user.")

async def list_premium_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("Admins only.")
        return
    premium_users = await db.get_premium_users() if hasattr(db, "get_premium_users") else []
    if premium_users:
        lines = [f"• {u['user_id']}" for u in premium_users if 'user_id' in u]
        await update.message.reply_text("👑 Premium Users:\n" + "\n".join(lines))
    else:
        await update.message.reply_text("👑 No premium users.")

async def remove_premium_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("Admins only.")
        return
    await update.message.reply_text("👑 Use /rempaid USER_ID to remove a premium user.")

# Add more admin commands as needed, following the above format.
