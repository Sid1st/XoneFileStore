import re
import os
import random
from os import getenv, environ
from Script import script 
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.types import InputMediaPhoto

load_dotenv()


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

      
# Owner Information
API_ID = int(environ.get("API_ID", "28908582"))
API_HASH = environ.get("API_HASH", "0d79d297bb8f56caed2c8f08bfc17289")
ADMINS = int(environ.get("ADMINS", "5052476013"))

# Database Information
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://MissXone:09ahczILiv7DrtZW@cluster0.nmseyk3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CDB_NAME = environ.get("CDB_NAME", "XoneFileStoreClone")
DB_URI = environ.get("DB_URI", "mongodb+srv://statusringtones:fV2rGirOqMMhE1Sg@cluster0.i2jvgsx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "XoneFileStore")


# Bot Information
BOT_TOKEN = environ.get("BOT_TOKEN", "")
BOT_USERNAME = environ.get("BOT_USERNAME", "XoneFileStore_bot") # your bot username without @
PICS = (environ.get('PICS', ['https://telegra.ph/file/5bdceafb32c966c5b5b4c.jpg',
                              'https://telegra.ph/file/e2515f6559c7f4da99afd.jpg',])) # Bot Start Picture

# Auto Delete Information
AUTO_DELETE = int(environ.get("AUTO_DELETE", "20")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1200")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001700999955"))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002219601256')).split()]


# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
CLONE_DB_URI = is_enabled((environ.get('CLONE_DB_URI', "False")), False)

# File Stream Config
class Var(object):
    MULTI_CLIENT = False
    name = str(getenv('name', 'XoneFileStore'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001700999955'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = ""
    else:
        URL = ""


