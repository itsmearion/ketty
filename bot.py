from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import register_handlers
from utils.logger import setup_logger
from utils.error_handler import on_error

setup_logger()
app = Client(
    "gunda_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode="MarkdownV2"
)

register_handlers(app)

# Setup global error handler
app.add_handler(None, group=-1)(on_error)

if __name__ == "__main__":
    app.run()
