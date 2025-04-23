from .start_handler import start_handler
from .format_handler import format_handler
from .user_to_admin import user_to_admin_handler
from .admin_to_user import admin_to_user_handler

def register_handlers(app):
    start_handler(app)
    format_handler(app)
    user_to_admin_handler(app)
    admin_to_user_handler(app)