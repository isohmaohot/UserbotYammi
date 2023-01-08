import os

API_HASH = os.getenv("7457a2dd85fa14088d0bc7291143b617")
API_ID = int(os.getenv("18986903"))
MONGO_URI = os.getenv("MONGO_URI")
HEROKU_API = os.getenv("HEROKU_API")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
PY_SESSION = os.getenv("PYROGRAM_SESSION")
TE_SESSION = os.getenv("TELETHON_SESSION")
PREFIX = os.environ.get("PREFIX", ".")
LOG_CHAT = int(os.getenv("LOG_CHAT"))
