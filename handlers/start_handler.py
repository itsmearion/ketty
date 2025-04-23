import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.escape import escape_markdown
import logging

logger = logging.getLogger("GundaBot")

def start_handler(app):
    @app.on_message(filters.command("start") & filters.private)
    async def start(client, message):
        chat_id = message.chat.id
        try:
            msg1 = await client.send_message(chat_id, escape_markdown("༄❀ delicate petals drift around you... ᯓ༄"))
            asyncio.create_task(delete_after(msg1, 3))

            msg2 = await client.send_message(chat_id, escape_markdown("༄ feathers of dreams flutter in the twilight ~ ❀༄"))
            asyncio.create_task(delete_after(msg2, 3))

            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("ᯓ ✎ format your wishes ✎", callback_data="format")]
            ])

            await client.send_message(
                chat_id,
                escape_markdown("𖤓 pilih pesonamu, wahai pengelana ~"),
                reply_markup=keyboard
            )
        except Exception as e:
            logger.error(f"Start handler error: {e}")

async def delete_after(message, delay):
    await asyncio.sleep(delay)
    try:
        await message.delete()
    except Exception as e:
        logging.warning(f"Gagal hapus pesan: {e}")
