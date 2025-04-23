import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.escape import escape_markdown
import logging

logger = logging.getLogger("GundaBot")

def format_handler(app):
    @app.on_callback_query(filters.regex("format"))
    async def format_button(client, callback_query):
        try:
            await callback_query.answer("Menyiapkan format...")

            username = callback_query.from_user.username or "username"
            text = (
                f"Salutations I'm @{username}, I’d like to place an order for catalog t.me/blakeshley listed at Blakeshley, "
                f"Using payment method [dana, gopay, qriss, spay, ovo, bank.] "
                f"The total comes to IDR [00.000] Inrush add 5k [yay/nay]. "
                f"Kindly process this, Thanks a bunch."
            )

            escaped_text = escape_markdown(text)
            message_content = f"*Copy and Paste This:*\n\n```{escaped_text}```"

            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("ᯓ ✎ Copy Here", switch_inline_query=text)]
            ])

            sent = await client.send_message(
                callback_query.message.chat.id,
                message_content,
                reply_markup=keyboard
            )

            asyncio.create_task(delete_after(sent, 420))

            await callback_query.message.delete()

            msg = await client.send_message(
                callback_query.message.chat.id,
                escape_markdown("༄ sihir memudar ke dalam kabut... ༄")
            )
            asyncio.create_task(delete_after(msg, 3))

        except Exception as e:
            logger.error(f"Format handler error: {e}")

async def delete_after(message, delay):
    await asyncio.sleep(delay)
    try:
        await message.delete()
    except Exception as e:
        logging.warning(f"Gagal hapus pesan: {e}")
