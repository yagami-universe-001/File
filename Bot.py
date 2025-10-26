# bot.py (Root)
import asyncio
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
    app.add_handler(CommandHandler("getthumb", user_commands.get_thumbnail))
    app.add_handler(CommandHandler("delthumb", user_commands.delete_thumbnail))
    app.add_handler(CommandHandler("setwatermark", user_commands.set_watermark))
    app.add_handler(CommandHandler("getwatermark", user_commands.get_watermark))
    app.add_handler(CommandHandler("spoiler", user_commands.toggle_spoiler))
    app.add_handler(CommandHandler("setmedia", user_commands.set_media_type))
    app.add_handler(CommandHandler("upload", user_commands.set_upload_destination))
    app.add_handler(CommandHandler("compress", video_commands.compress_video))
    app.add_handler(CommandHandler("cut", video_commands.cut_video))
    app.add_handler(CommandHandler("crop", video_commands.crop_video))
    app.add_handler(CommandHandler("merge", video_commands.merge_videos))
    app.add_handler(CommandHandler("all", video_commands.encode_all))
    app.add_handler(CommandHandler("144p", video_commands.encode_144p))
    app.add_handler(CommandHandler("240p", video_commands.encode_240p))
    app.add_handler(CommandHandler("360p", video_commands.encode_360p))
    app.add_handler(CommandHandler("480p", video_commands.encode_480p))
    app.add_handler(CommandHandler("720p", video_commands.encode_720p))
    app.add_handler(CommandHandler("1080p", video_commands.encode_1080p))
    app.add_handler(CommandHandler("2160p", video_commands.encode_2160p))
    app.add_handler(CommandHandler("addwatermark", video_commands.add_watermark))
    app.add_handler(CommandHandler("sub", media_commands.add_soft_subtitles))
    app.add_handler(CommandHandler("hsub", media_commands.add_hard_subtitles))
    app.add_handler(CommandHandler("rsub", media_commands.remove_subtitles))
    app.add_handler(CommandHandler("extract_sub", media_commands.extract_subtitles))
    app.add_handler(CommandHandler("extract_audio", media_commands.extract_audio))
    app.add_handler(CommandHandler("addaudio", media_commands.add_audio))
    app.add_handler(CommandHandler("remaudio", media_commands.remove_audio))
    app.add_handler(CommandHandler("extract_thumb", media_commands.extract_thumbnail))
    app.add_handler(CommandHandler("mediainfo", media_commands.get_media_info))
    app.add_handler(CommandHandler("restart", admin_commands.restart_bot))
    app.add_handler(CommandHandler("queue", admin_commands.check_queue))
    app.add_handler(CommandHandler("clear", admin_commands.clear_queue))
    app.add_handler(CommandHandler("audio", admin_commands.set_audio_bitrate))
    app.add_handler(CommandHandler("codec", admin_commands.set_codec))
    app.add_handler(CommandHandler("preset", admin_commands.set_preset))
    app.add_handler(CommandHandler("crf", admin_commands.set_crf))
    app.add_handler(CommandHandler("addchnl", admin_commands.add_fsub_channel))
    app.add_handler(CommandHandler("delchnl", admin_commands.delete_fsub_channel))
    app.add_handler(CommandHandler("listchnl", admin_commands.list_fsub_channels))
    app.add_handler(CommandHandler("fsub_mode", admin_commands.fsub_mode))
    app.add_handler(CommandHandler("shortner", admin_commands.view_shortener))
    app.add_handler(CommandHandler("shortlink1", admin_commands.set_shortlink1))
    app.add_handler(CommandHandler("tutorial1", admin_commands.set_tutorial1))
    app.add_handler(CommandHandler("shortlink2", admin_commands.set_shortlink2))
    app.add_handler(CommandHandler("tutorial2", admin_commands.set_tutorial2))
    app.add_handler(CommandHandler("shortner1", admin_commands.view_shortener1))
    app.add_handler(CommandHandler("shortner2", admin_commands.view_shortener2))
    app.add_handler(CommandHandler("addpaid", admin_commands.add_premium_user))
    app.add_handler(CommandHandler("listpaid", admin_commands.list_premium_users))
    app.add_handler(CommandHandler("rempaid", admin_commands.remove_premium_user))
    app.add_handler(CommandHandler("update", admin_commands.update_bot))

async def main():
    app = Application.builder().token(Config.BOT_TOKEN).build()
    setup_handlers(app)
    logger.info("Bot started successfully!")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
