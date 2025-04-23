from pyrogram import filters
from utils.escape import escape_markdown
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_handler(app):
    @app.on_message(filters.command("start") & filters.private)
    async def start(client, message):
        chat_id = message.chat.id
        text = escape_markdown("༄❀ Welcome, traveler ~ ✧༄")

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("ᯓ ✎ format your wishes ✎", callback_data="format")]
        ])

        await client.send_message(
            chat_id,
            text,
            reply_markup=keyboard
        )