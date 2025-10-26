from utils.ffmpeg_handler import FFmpegHandler
ffmpeg = FFmpegHandler()

async def add_soft_subtitles(update, context):
    await update.message.reply_text("Send subtitle file...")
# ...add_hard_subtitles, remove_subtitles, extract_audio, add/remove_audio, extract_thumb, mediainfo...
