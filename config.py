import os

API_ID = os.environ.get('API_ID', "11450835")
API_HASH = os.environ.get('API_HASH', "0fadb61feae6ccf016932823bbf1565c")
BOT_TOKEN = os.environ.get('BOT_TOKEN', "5781009864:AAEdWzhoffBvdLcQBY4WQKpzuMYpDCAFm28")
OWNER_ID = int(os.environ.get("OWNER_ID", "1254785184"))
ADMINS = list(int(i) for i in os.environ.get("ADMINS", "1254785184").split(" ")) if os.environ.get("ADMINS") else []
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)
MONGODB = os.environ.get('MONGODB', "mongodb+srv://Alex1206:Alex1206@cluster0.itfqj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get('DATABASE_NAME', "Cluster0") 
COLLECTION_NAME = os.environ.get('COLLECTION_NAME', "myfiles")
CHANNELS = os.environ.get('CHANNELS', "True")
CHANNELS_LIST = list(int(i) for i in os.environ.get("CHANNELS_LIST", "-1002494518188").split(" ")) if os.environ.get("CHANNELS_LIST") else []
FORCESUB = os.environ.get('FORCESUB', "True")
PORT = int(os.environ.get('PORT', 8080))

# Other Settings
UPDATE_CHANNEL =  os.environ.get('UPDATE_CHANNEL' "-1001627812746")
USERNAME = UPDATE_CHANNEL
RESULTS_COUNT = int(os.environ.get('RESULT_COUNTS', 10))
AUTO_DELETE = os.environ.get('AUTO_DELETE', True)
AUTO_DELETE_TIME = int(os.environ.get('AUTO_DELETE_TIME', 300))
IMDB_TEMPLATE = os.environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
MAX_LIST_ELM = os.environ.get("MAX_LIST_ELM", None)
WELCOME_IMAGE = os.environ.get('WELCOME_IMAGE', 'https://bit.ly/3y8miWu')
RESULTS_IMAGE = os.environ.get('RESULTS_IMAGE', 'https://static.wikia.nocookie.net/ideas/images/e/e4/Movie_night.jpg')

