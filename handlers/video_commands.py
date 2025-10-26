from utils.ffmpeg_handler import FFmpegHandler
ffmpeg = FFmpegHandler()

async def encode_144p(update, context):
    await update.message.reply_text("Encoding to 144p...")
# ...other resolutions, compress, cut, crop, merge, addwatermark...
