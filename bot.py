from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import register_handlers
from utils.logger import setup_logger
from utils.error_handler import on_error
from pyrogram.errors import RPCError
from pyrogram.handlers import MessageHandler
from handlers import register_handlers


setup_logger()

app = Client(
    "gunda_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode="MarkdownV2"  # Global parse_mode
)

register_handlers(app)

# Handler error global

async def on_error(client, update, error):
    if isinstance(error, RPCError):
        # khusus RPC error
        logging.error(f"RPCError: {error}")
    else:
        # error umum
        logging.error(f"Unhandled error: {error}")

app.add_handler(MessageHandler(start_handler_fn, filters.command("start")))
app.add_error_handler(on_error)

register_handlers(app)

if __name__ == "__main__":
    app.run()