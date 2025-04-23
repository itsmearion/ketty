import logging
from pyrogram import filters
from pyrogram.handlers import MessageHandler

async def on_error(client, message):
    try:
        logging.error(f"Error on message: {message}")
    except Exception as e:
        logging.error(f"Error in error_handler: {e}")