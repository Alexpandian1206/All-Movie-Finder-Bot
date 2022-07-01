import os
from ssl import CHANNEL_BINDING_TYPES

# API_ID = os.environ.get('API_ID')
# API_HASH = os.environ.get('API_HASH')
# BOT_TOKEN = os.environ.get('BOT_TOKEN')
# OWNER_ID = int(os.environ.get("OWNER_ID"))
# ADMINS = list(int(i) for i in os.environ.get("ADMINS", "").split(" ")) if os.environ.get("ADMINS") else []
# if OWNER_ID not in ADMINS:
#     ADMINS.append(OWNER_ID)
# MONGODB = os.environ.get('MONGODB')
# DATABASE_NAME = os.environ.get('DATABASE_NAME') 
# COLLECTION_NAME = os.environ.get('COLLECTION_NAME')
# CHANNELS = os.environ.get('CHANNELS', "False")
# CHANNELS_LIST = list(int(i) for i in os.environ.get("CHANNELS_LIST", "").split(" ")) if os.environ.get("CHANNELS_LIST") else []

# # Other Settings
# UPDATE_CHANNEL =  os.environ.get('UPDATE_CHANNEL')
# USERNAME = UPDATE_CHANNEL
# RESULTS_COUNT = int(os.environ.get('RESULT_COUNTS', 10))
# AUTO_DELETE = os.environ.get('AUTO_DELETE', False)
# AUTO_DELETE_TIME = int(os.environ.get('AUTO_DELETE_TIME', 300))
# IMDB_TEMPLATE = os.environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
# MAX_LIST_ELM = os.environ.get("MAX_LIST_ELM", None)
# WELCOME_IMAGE = os.environ.get('START_PIC', 'https://bit.ly/3y8miWu')
# RESULTS_IMAGE = os.environ.get('RESULTS_IMAGE', 'https://static.wikia.nocookie.net/ideas/images/e/e4/Movie_night.jpg')


API_ID = 3102709
API_HASH = "1108ea82042eebcd78c70c73fbc2da05"
BOT_TOKEN = "5439845446:AAFT0Z7CcvUwY6j4hsMYcx9D9ScZc1mQtrs"
OWNER_ID = 1166625664
ADMINS = [1166625664, 1166625664, 1166625664, 1166625664]
MONGODB = "mongodb+srv://erichdaniken:erichdaniken@cluster0.hfpcv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority" + "&ssl=true&ssl_cert_reqs=CERT_NONE"
DATABASE_NAME = 'Films'
COLLECTION_NAME = 'WEB MOVIE DB'
USERNAME = 'T2linkss'
UPDATE_CHANNEL =  "T2LINKSS"
RESULTS_COUNT = 20
AUTO_DELETE =  False
AUTO_DELETE_TIME = 5
CHANNELS = True
CHANNELS_LIST = [-1001706503677, 1001706503677, 1001706503677, 1001706503677]

# Other settings
# A way to set a default value for a variable.
MAX_LIST_ELM = os.environ.get("MAX_LIST_ELM", None)
WELCOME_IMAGE = 'https://bit.ly/3y8miWu'
RESULTS_IMAGE = 'https://static.wikia.nocookie.net/ideas/images/e/e4/Movie_night.jpg'
IMDB_TEMPLATE = "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10"

