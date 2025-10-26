# bot.py (Root)
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config.settings import Config
from handlers import user_commands, video_commands, media_commands, admin_commands

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def setup_handlers(app: Application):
    app.add_handler(CommandHandler("start", user_commands.start))
    app.add_handler(CommandHandler("help", user_commands.help_command))
    app.add_handler(CommandHandler("setthumb", user_commands.set_thumbnail))
    app.add_handler(CommandHandler("144p", video_commands.encode_144p))
    app.add_handler(CommandHandler("sub", media_commands.add_soft_subtitles))
    app.add_handler(CommandHandler("restart", admin_commands.restart_bot))
    app.add_handler(CommandHandler("queue", admin_commands.check_queue))
    app.add_handler(CommandHandler("clear", admin_commands.clear_queue))
    app.add_handler(CommandHandler("audio", admin_commands.set_audio_bitrate))
    app.add_handler(CommandHandler("codec", admin_commands.set_codec))
    app.add_handler(CommandHandler("preset", admin_commands.set_preset))
    app.add_handler(CommandHandler("crf", admin_commands.set_crf))
    app.add_handler(CommandHandler("addpaid", admin_commands.add_premium_user))
    app.add_handler(CommandHandler("listpaid", admin_commands.list_premium_users))
    app.add_handler(CommandHandler("rempaid", admin_commands.remove_premium_user))

def main():
    app = Application.builder().token(Config.BOT_TOKEN).build()
    setup_handlers(app)
    logger.info("Bot started successfully!")
    app.run_polling()

if __name__ == "__main__":
    main()
