

from os import environ

API_ID = int(environ.get("API_ID", "22484497"))
API_HASH = environ.get("API_HASH", "c38cb053916c47a97590c244663cbaef")
BOT_TOKEN = environ.get("BOT_TOKEN", " ")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "selectionway_free_course")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/selectionway_free_course")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "6252997817").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "6252997817"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")








