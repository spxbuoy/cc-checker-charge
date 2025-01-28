from pyrogram import Client 
import os
import json
from FUNC.server_stats import *

plugins = dict(root="BOT")

# Load configuration from JSON file
with open("FILES/config.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)
    API_ID = DATA["API_ID"]
    API_HASH = DATA["API_HASH"]
    BOT_TOKEN = DATA["BOT_TOKEN"]

# Create a user client (if needed)
user = Client( 
    "Scrapper", 
    api_id=API_ID, 
    api_hash=API_HASH
)

# Create a bot client
bot = Client(
    "MY_BOT", 
    api_id=API_ID, 
    api_hash=API_HASH, 
    bot_token=BOT_TOKEN, 
    plugins=plugins 
)

if __name__ == "__main__":
    # Get the port from the environment variable (not used by Pyrogram)
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if not set
    print(f"Bot is running on port {port} (not actually used by Pyrogram) ✅")
    print("NOW START BOT ONCE MY MASTER")

    # Run the bot
    bot.run()
