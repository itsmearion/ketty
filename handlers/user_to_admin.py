from pyrogram import filters
from config import ADMIN_GROUP_ID
from utils.escape import escape_markdown

def user_to_admin_handler(app):
    @app.on_message(filters.private & filters.text & ~filters.command(["start"]))
    async def forward_user_message(client, message):
        user = message.from_user
        text = escape_markdown(message.text)
        caption = (
            f"*New Message from {escape_markdown(user.first_name)}*\n\n"
            f"{text}\n\n"
            f"User ID: `{user.id}`"
        )

        await client.send_message(
            ADMIN_GROUP_ID,
            caption
        )