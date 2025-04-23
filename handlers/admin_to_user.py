import logging
from pyrogram import filters
from pyrogram.types import Message
from config import ADMIN_GROUP_ID

async def admin_to_user_handler_fn(client, message: Message):
    if message.chat.id != ADMIN_GROUP_ID:
        return

    if not message.reply_to_message or not message.reply_to_message.text:
        return

    original_text = message.reply_to_message.text
    if "UserID:" not in original_text:
        return

    try:
        user_id = int(original_text.split("UserID:")[1].strip())

        await client.send_message(
            user_id,
            message.text
        )

    except Exception as e:
        logging.error(f"Terjadi kesalahan saat membalas ke user: {e}")

from pyrogram.handlers import MessageHandler
admin_to_user_handler = MessageHandler(admin_to_user_handler_fn, filters.reply & filters.text)