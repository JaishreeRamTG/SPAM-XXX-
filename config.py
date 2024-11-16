import logging

from telethon import TelegramClient

from os import getenv
from SHUKLASPAM.data import SHASHANK


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR SHUKLABOTS
API_ID = 29308061
API_HASH = "462de3dfc98fd938ef9c6ee31a72d099"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = ""
BOT_TOKEN2 = ""
BOT_TOKEN3 = ""
BOT_TOKEN4 = ""
BOT_TOKEN5 = ""
BOT_TOKEN6 = ""
BOT_TOKEN7 = ""
BOT_TOKEN8 = ""
BOT_TOKEN9 = ""
BOT_TOKEN10 = ""

SUDO_USERS = "SUDO_USERS"
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="6762113050"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
