import os
from os import environ

API_ID       = int(environ.get("API_ID", ""))
API_HASH     = environ.get("API_HASH", "")
BOT_TOKEN    = environ.get("BOT_TOKEN", "")
DATABASE_URI = environ.get("DATABASE_URI", "")
LOG_CHANNEL  = int(environ.get("LOG_CHANNEL", ""))
ADMIN        = int(environ.get("ADMIN", ""))
CHANNEL      = environ.get("CHANNEL", "@VJ_Botz")
