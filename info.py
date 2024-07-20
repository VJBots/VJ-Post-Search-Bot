import os
from os import environ

API_ID       = int(environ.get("API_ID", "22182189"))
API_HASH     = environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
BOT_TOKEN    = environ.get("BOT_TOKEN", "6627318053:AAHFeyNF255TOFm4jtyeiAAcqOukvIHyN-Q")
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://mihaja5084:yeIh95RrMkRNZ3It@cluster0.6voc3fm.mongodb.net/?retryWrites=true&w=majority")
LOG_CHANNEL  = int(environ.get("LOG_CHANNEL", "-1002131110143"))
ADMIN        = int(environ.get("ADMIN", "6073523936"))
CHANNEL      = environ.get("CHANNEL", "@VJ_Botz")
