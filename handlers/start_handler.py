handlers/start_handler.py

import asyncio 
import logging 
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.escape import escape_markdown 
from config import ADMIN_GROUP_ID

@Client.on_message(filters.command("start") & filters.private) 
async def start_handler(client, message): chat_id = message.chat.id

try:
    # Teks pertama
    text1 = "༄❀ delicate petals drift around you... ௣༄"
    msg1 = await client.send_message(chat_id, escape_markdown(text1), parse_mode="MarkdownV2")
    await asyncio.sleep(2)
    await msg1.delete()

    # Teks kedua
    text2 = "༄ feathers of dreams flutter in the twilight ~ ❀༄"
    msg2 = await client.send_message(chat_id, escape_markdown(text2), parse_mode="MarkdownV2")
    await asyncio.sleep(2)
    await msg2.delete()

    # Tampilkan tombol format
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("௣ ✓ format your wishes ✓", callback_data="format")]]
    )

    await client.send_message(
        chat_id,
        escape_markdown("🕓 pilih pesonamu, wahai pengelana ~"),
        reply_markup=keyboard,
        parse_mode="MarkdownV2"
    )

except Exception as e:
    logging.error(f"Terjadi kesalahan saat start: {e}")

