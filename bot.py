import time
import os
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, ADMINS

# Function to synchronize server time
def sync_time():
    if os.name == "posix":
        os.system('sudo ntpdate -s time.nist.gov')
        print("Time synchronized successfully.")
    else:
        print("Please sync time manually on your server.")

# Sync time before starting the bot
sync_time()

# Create bot client instance
bot = Client('droplink_search_bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             plugins=dict(root="plugins"),
             workers=50,
             sleep_threshold=10)

print("Bot Started")

# Running the bot
bot.run()
