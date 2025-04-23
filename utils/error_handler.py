import logging

logger = logging.getLogger("GundaBot")

async def on_error(client, update, error):
    logger.error(f"Error terjadi: {error}")
