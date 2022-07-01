from pyrogram.types import Message
from plugins.database import collection
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *
from translation import *
from helpers.validate_query import validate_q
from helpers.link_to_hyper import link_to_hyperlink

BUTTONS = {}
async def get_movies(query:str, m:Message):
    list2 = []
    results = await search_for_videos(query)
    if results is not None:
        for result in results:   
            id = str(result['_id'])
            list2.append(
                {
                'id': id,
                'caption': f'**{result["caption"]}**'
                }
            )

        if len(list2) > 1: 
            ls = split_list(list2, 1)
            btns = list(ls) 
            keyword = f"{m.chat.id}-{m.id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = [
                [InlineKeyboardButton(text="📃 Pages 1/1",callback_data="pages")]
            ]

            if m.chat.id in ADMINS:
                buttons.append(
                [InlineKeyboardButton("🗑 Delete", callback_data=f"delete#{list2[0]['id']}")]
            )   
            
            reply_markup= InlineKeyboardMarkup(buttons)
            txt = await m.reply_photo(photo=RESULTS_IMAGE, caption=list2[0]['caption'], reply_markup=reply_markup, quote=True)
            return txt

        data = BUTTONS[keyword]

        buttons = []
        buttons.append(
            [InlineKeyboardButton(text="NEXT ⏩",callback_data=f"next_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"📃 Pages 1/{data['total']}", callback_data="pages")]
        )

        if m.chat.id in ADMINS:
            buttons.append(
            [InlineKeyboardButton("🗑 Delete", callback_data=f"delete#{list2[0]['id']}")]
        )   

        reply_markup = InlineKeyboardMarkup(buttons) 
        txt = await m.reply_photo(photo=RESULTS_IMAGE, caption=list2[0]['caption'], reply_markup=reply_markup, quote=True)
        return txt


async def search_for_videos(search_text:str):
    query = await validate_q(search_text)
    x = f"\"{query}\""
    pipeline= {
            '$text':{'$search': x }
        }
    db_list = collection.find(
            pipeline,
            {'score': {'$meta':'textScore'}}
        )
    query = db_list.sort([("score", {'$meta': 'textScore'})]) 
    quer = list(query)

    if query.count() > 0:
        replaced_query = AsyncIter(quer)
        replaced_query = await convert_to_hyperlink(replaced_query)
        return replaced_query

class AsyncIter:    
    def __init__(self, items):    
        self.items = items    

    async def __aiter__(self):    
        for item in self.items:    
            yield item  

    async def __anext__(self):
        try:
            return next(self.iter)
        except StopIteration:
            raise StopAsyncIteration


async def convert_to_hyperlink(query):
    lis = []
    async for i in query:
        cap = await link_to_hyperlink(i['caption'])
        i['caption'] = cap
        lis.append(i)
    return lis

def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]          



