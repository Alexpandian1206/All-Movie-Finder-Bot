from pyrogram import Client
from flask import Flask
from threading import Thread
from config import *

API_ID = API_ID
API_HASH = API_HASH
BOT_TOKEN = BOT_TOKEN
ADMIN = ADMINS

# Initialize the bot
bot = Client('droplink search bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             plugins=dict(root="plugins"),
             workers=50,
             sleep_threshold=10)

# Initialize Flask app for health checks
app = Flask(__name__)

@app.route('/health')
def health_check():
    return "Bot is running", 200

# Function to run the Flask app in a thread
def run_app():
    app.run(host='0.0.0.0', port=8080)

# Start Flask in a separate thread
Thread(target=run_app).start()

print("Bot Started")

# Running the bot
bot.run()
