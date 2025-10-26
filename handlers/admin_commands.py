"""
Admin Command Handlers
Handles admin-only commands: restart, queue, encoding settings, premium users, shorteners, force subscribe.
"""

from telegram import Update
from telegram.ext import ContextTypes
from config.settings import Config
from database.db_manager import DatabaseManager

db = DatabaseManager()

def is_admin(user_id: int) -> bool:
    """Check if user is an admin."""
    return user_id in Config.ADMIN_IDS

async def restart_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/restart - Restart the bot (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text("🔄 Bot restart not supported in stateless environments.
Please restart manually on your server/VPS/hosting.")

async def check_queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/queue - Check total queue (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    queue = await db.get_queue()
    count = len(queue)
    await update.message.reply_text(f"📋 Current Queue: {count} tasks
Use /clear to clear all tasks.")

async def clear_queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/clear - Clear all queue tasks (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    cleared = await db.clear_queue()
    await update.message.reply_text(f"✅ Cleared {cleared} tasks from queue.")

async def set_audio_bitrate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/audio - Set audio bitrate (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text(
        "🔊 Set audio bitrate:
96k, 128k, 192k, 256k, 320k

Example: /audio 192k"
    )

async def set_codec(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/codec - Set video codec (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text(
        "🎥 Set video codec:
1. libx264 (H.264, widely compatible)
2. libx265 (H.265, better compression)

Reply with 1 or 2"
    )

async def set_preset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/preset - Change encoding preset (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text(
        "⚙️ Encoding presets:
ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow

Slower = better quality but longer encoding time"
    )

async def set_crf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/crf - Set CRF value (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text(
        "🎚️ CRF value (0-51):
18 - Visually lossless
23 - Default (good quality)
28 - Lower quality, smaller file

Lower = better quality"
    )

async def add_fsub_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Add force subscribe channel (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text("📢 Send channel ID to add for force subscribe
Example: -1001234567890")

async def delete_fsub_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Delete force subscribe channel (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text("📢 Send channel ID to remove from force subscribe")

async def list_fsub_channels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """List all force subscribe channels (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    channels = await db.get_fsub_channels()
    if channels:
        channel_list = "
".join([f"• {ch}" for ch in channels])
        await update.message.reply_text(f"📢 Force Subscribe Channels:
{channel_list}")
    else:
        await update.message.reply_text("📢 No force subscribe channels set.")

async def fsub_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/fsub_mode - Check force subscribe mode (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    mode = "Enabled" if Config.FSUB_MODE else "Disabled"
    await update.message.reply_text(f"📢 Force Subscribe Mode: {mode}")

async def view_shortener(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/shortner - View URL shortener settings (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text(
        "🔗 URL Shortener Settings:
/shortner1 - View Shortener 1
/shortner2 - View Shortener 2"
    )

async def set_shortlink1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/shortlink1 - Set shortlink 1 API (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text("🔗 Send Shortlink 1 API URL and Key")

async def set_tutorial1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/tutorial1 - Set tutorial for shortener 1 (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text("📖 Send tutorial link for Shortener 1")

async def set_shortlink2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/shortlink2 - Set shortlink 2 API (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text("🔗 Send Shortlink 2 API URL and Key")

async def set_tutorial2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/tutorial2 - Set tutorial for shortener 2 (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text("📖 Send tutorial link for Shortener 2")

async def view_shortener1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/shortner1 - View shortener 1 config (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text(
        f"🔗 Shortener 1:
API: {Config.SHORTLINK1_URL}
Tutorial: {Config.TUTORIAL1}"
    )

async def view_shortener2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/shortner2 - View shortener 2 config (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text(
        f"🔗 Shortener 2:
API: {Config.SHORTLINK2_URL}
Tutorial: {Config.TUTORIAL2}"
    )

async def add_premium_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/addpaid - Add premium user (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text(
        "👑 Send user ID to add as premium
Format: /addpaid USER_ID DAYS"
    )

async def list_premium_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/listpaid - List premium users (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    premium = await db.get_premium_users()
    if premium:
        user_list = "
".join([f"• {u['user_id']}" for u in premium])
        await update.message.reply_text(f"👑 Premium Users:
{user_list}")
    else:
        await update.message.reply_text("👑 No premium users.")

async def remove_premium_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/rempaid - Remove premium user (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text("👑 Send user ID to remove from premium.")

async def update_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/update - Git pull latest updates (Admin only)"""
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ This command is for admins only.")
        return
    await update.message.reply_text("🔄 This bot does not support self-updates. Please pull changes manually on your server.")
    
