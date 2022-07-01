import ast
import re
from pyrogram import Client, filters
from pyrogram.types import Message
from .database import collection
from config import *
from pyrogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
from .add_movies import caption


@Client.on_message(filters.chat(CHANNELS_LIST) & filters.media & filters.channel & filters.incoming)
async def channel_movie_handler(c: Client, m: Message):
    if m.caption_entities:
        message = m.caption
        captions = m.caption_entities

        for count, i in enumerate(await caption(captions)):
            message = message.replace("👉 Link 🔗", i['url'], 1)

        id = collection.insert_one(
            {"caption": message,
            'title': message.splitlines()[0]
            }
        )

        reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Delete", callback_data=f"delete#{id.inserted_id }")],
        ])
        txt = await c.send_message(
            chat_id=OWNER_ID,
            text=f"Post Added Successfully\n\nPost Link: [Click]({m.link})",
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    else:
        txt = await c.send_message(
            chat_id=OWNER_ID,
            text=f"Something went wrong on adding post \n\nPost Link: [Click]({m.id})",
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
