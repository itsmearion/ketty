from .start_handler import start_handler_fn
from .format_handler import format_handler
from .admin_to_user import admin_to_user_handler

def register_handlers(app):
    app.add_handler(start_handler)
    app.add_handler(format_handler)
    app.add_handler(admin_to_user_handler)