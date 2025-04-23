from pyrogram import filters
from utils.escape import escape_markdown
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

def format_handler(app):
    @app.on_callback_query(filters.regex("format"))
    async def format_button(client, callback_query):
        await callback_query.answer("Preparing your format...")

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
            message_content
        )

        await asyncio.sleep(420)  # Auto delete setelah 7 menit
        await sent.delete()

        try:
            await callback_query.message.delete()
        except:
            pass