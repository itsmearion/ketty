import asyncio
import logging
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from utils.escape import escape_markdown
from pyrogram.handlers import MessageHandler

# Ini fungsi yang ngerjain
async def start_handler_fn(client, message: Message):
    chat_id = message.chat.id

    try:
        text1 = "༄❀ delicate petals drift around you... ᯓ༄"
        msg1 = await client.send_message(chat_id, escape_markdown(text1), parse_mode="MarkdownV2")
        await asyncio.sleep(2)
        await msg1.delete()

        text2 = "༄ feathers of dreams flutter in the twilight ~ ❀༄"
        msg2 = await client.send_message(chat_id, escape_markdown(text2), parse_mode="MarkdownV2")
        await asyncio.sleep(2)
        await msg2.delete()

        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("ᯓ ✎ format your wishes ✎", callback_data="format")]]
        )

        await client.send_message(
            chat_id,
            escape_markdown("𖤓 pilih pesonamu, wahai pengelana ~"),
            reply_markup=keyboard,
            parse_mode="MarkdownV2"
        )

    except Exception as e:
        logging.error(f"Terjadi kesalahan saat start: {e}")

# Ini object handler yang di register ke app
start_handler = MessageHandler(start_handler_fn, filters.command("start") & filters.private)