from pyrogram import Client
import re
from os import environ
from dotenv import load_dotenv
from Script import script 
import time 

# load_dotenv("./config.env")
load_dotenv("./dynamic.env", override=True)

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'series')
API_ID = '20400973' #bots
API_HASH = '047838cb76d54bc445e155a7cab44664'
BOT_TOKEN = '7448922857:AAEiLcjbuhP_XNSl0KOiCj70OpBJWFWKbCA'
#BOT_TOKEN = '7976955865:AAGZipH-V_-jrN5fKDrB0Bi_bPMtUzavA94' #test

API_ID2 = "29756440" #Userbot Should Be Added In ADMINS and In CHANNELS
API_HASH2 = "51bf53b8246dcea2a7a53246a032eca4"
SESSION_STRING = "BQHGDBgAfMkyGvstZaF0bV-s2bzrAfKYv1icxqfP_H4znATV0nGxcBAtZOZnqZDBluOkd0eWPNA8-glRIaEpAVpGH7Z6JcbCXYm_AhAVz-72rUWWpCJ_SmfnzkGfEXzQVEK8cmDvm_7fYeoWY8j6asLurZyi-KOA11HNHMar_aSc9dvfP04ySPqnmKptejTsw83Gg3vjkvsPmBidbtB_cqgviAL4MYJYc5x6GAtMcF-o2VjUVZWBQtQ9zgTjJtYolkZLhrW32Yy8gbOzYRZTmkGAmRf1q4loFuLG3AjzK7X3x23fjzg3sc3HXcdrP2MokKKhp7FFn3sspjR3zLKywpMLogrGsAAAAAGk03hfAA" #Pyrov2

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5677517133 5329179170 6544671421').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://SpidySeries:SpidySeries@cluster0.xreosjj.mongodb.net/?retryWrites=true&w=majority")
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []


STIC = ('CAACAgUAAxkBAAJ5iGaibnAzoinskJ5B2LDpA66GpMKlAAIgAwAClbKhVx_qcsdH29wKHgQ CAACAgUAAxkBAAJ5hGaibjRA5dyi2XAQrO1JSxz4dXUuAALdBAACQ7YIVvz4vy3OyyQAAR4E CAACAgUAAxkBAAJ5jGaibp7C2RDX1OgS1ex0j3GedHoeAAJAAQACqjqpV0SUvBwyov-QHgQ').split()

# MongoDB information
DATABASE_NAME = environ.get('DATABASE_NAME', "Spidyy")
COLLECTION_NAME = environ.get('COLLECTION_NAME', "Spidysries")

# FSUB 
auth_channel = environ.get('AUTH_CHANNEL' "-1002330118912")
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = environ.get("REQ_CHANNEL", -1002330118912)
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)
LIMIT = 2000
# Others
LOG_CHANNEL = '-1002361556192'
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{previouscaption}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", '{previouscaption}')
AUTO_DELETE_TIME = 0
AUTO_DELETE_MSG = """‼️ 𝗜𝗠𝗣𝗢𝗥𝗧𝗔𝗡𝗧 ‼️\n\n<blockquote>⚠️ 𝙁𝙞𝙡𝙚 𝙒𝙞𝙡𝙡 𝘽𝙚 𝘿𝙚𝙡𝙚𝙩𝙚𝙙 𝙄𝙣 10 𝙈𝙞𝙣𝙪𝙩𝙚𝙨.</blockquote>\n\n𝗜𝗳 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝘁𝗵𝗲𝘀𝗲 𝗳𝗶𝗹𝗲𝘀, 𝗞𝗶𝗻𝗱𝗹𝘆 𝗙𝗼𝗿𝘄𝗮𝗿𝗱 𝘁𝗵𝗲𝘀𝗲 𝗳𝗶𝗹𝗲𝘀 𝘁𝗼 𝗮𝗻𝘆 𝗰𝗵𝗮𝘁 (𝘀𝗮𝘃𝗲𝗱) 𝗮𝗻𝗱 𝘀𝘁𝗮𝗿𝘁 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱...\n\n𝗧𝗵𝗮𝗻𝗸 𝗬𝗼𝘂 :)\n@TEAM_COLD"""
DB_CHANNEL = [-1001747128591, -1001861941952, -1001877078944]
RAW_DB_CHANNEL = [1747128591, 1861941952, 1877078944]
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002433972763')).split()] #Required 
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10  \n🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)
PORT = "8080"

#userbot = Client("my_userbot", api_id=API_ID2, api_hash=API_HASH2, session_string=SESSION_STRING)
#userbot.start()
