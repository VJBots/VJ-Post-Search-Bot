# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from info import *
from pyrogram import Client

class Bot(Client):   
    def __init__(self):
        super().__init__(   
           "vj-post-search-bot",
            api_id=API_ID,
            api_hash=API_HASH,           
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"})
    async def start(self):                        
        await super().start()  
        print("Bot Started 🔧 Powered By @VJ_Botz")   
    async def stop(self, *args):
        await super().stop()
