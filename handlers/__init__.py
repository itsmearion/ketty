from .start_handler import start_handler
from .format_handler import format_handler

def register_handlers(app):
    start_handler(app)
    format_handler(app)
