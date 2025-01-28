from pyrogram import Client 
import json
from FUNC.server_stats import *

plugins = dict(root="BOT")

with open("FILES/config.json", "r", encoding="utf-8") as f:
    DATA      = json.load(f)
    API_ID    = DATA["24872155"]
    API_HASH  = DATA["36560cde182f779d6fe129dcd1d8f527"]
    BOT_TOKEN = DATA["8015410523:AAH2QPel_jq7lv5RKiNViu6Ih5_J-Cljntg"]

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
    # send_server_alert()
    print("Done Bot Active ✅")
    print("NOW START BOT ONCE MY MASTER")

    bot.run()
