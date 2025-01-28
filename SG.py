import json
from pyrogram import Client

with open("FILES/config.json", "r",encoding="utf-8") as f:
    DATA         = json.load(f)
    API_ID       = DATA["24872155"]
    API_HASH     = DATA["36560cde182f779d6fe129dcd1d8f527"]
    BOT_TOKEN    = DATA["8015410523:AAH2QPel_jq7lv5RKiNViu6Ih5_J-Cljntg"]
    PHONE_NUMBER = DATA["+254799505823"]

user = Client("Scrapper",
              api_id       = API_ID,
              api_hash     = API_HASH ,
              phone_number = PHONE_NUMBER
              )

user.start()


