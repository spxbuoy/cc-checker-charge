import os
from app import app
from pyrogram import Client 
import json
from FUNC.server_stats import *

plugins = dict(root="BOT")

with open("FILES/config.json", "r", encoding="utf-8") as f:
    DATA      = json.load(f)
    API_ID    = DATA["API_ID"]
    API_HASH  = DATA["API_HASH"]
    BOT_TOKEN = DATA["BOT_TOKEN"]

user = Client( 
            "Scrapper", 
             api_id   = API_ID, 
             api_hash = API_HASH
              )

bot = Client(
    "MY_BOT", 
    api_id    = API_ID, 
    api_hash  = API_HASH, 
    bot_token = BOT_TOKEN, 
    plugins   = plugins 
)



if __name__ == "__main__":
    port = int(os.environ.get("port", 4000))  #Get the port from environment or use 5000 from  main.py(host="0.0.0.0", port=port)
    print("Done Bot Active ✅")
    print("NOW START BOT ONCE MY MASTER")

    bot.run()
