import os

API_HASH = os.getenv("")
API_ID = str(os.getenv(""))
MONGO_URI = os.getenv("")
HEROKU_API = os.getenv("HEROKU_API")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
PY_SESSION = os.getenv("PYROGRAM_SESSION")
TE_SESSION = os.getenv("TELETHON_SESSION")
PREFIX = os.environ.get("PREFIX", ".")
LOG_CHAT = str(os.getenv(""))
