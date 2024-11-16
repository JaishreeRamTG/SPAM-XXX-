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

BOT_TOKEN = "8089923307:AAFlG4-w43LeXfVqxkYOMI7AhQ4EqKTUU_M"
BOT_TOKEN2 = "7681410517:AAGh42p25Re-K3-_2wWv_nfQpJoROqLSO6A"
BOT_TOKEN3 = "8184760602:AAFfVSNgpy8l41N-NCEhWoZE0NrWzBYe7o8"
BOT_TOKEN4 = "8014190692:AAHTpWt_ocQ9K0XSH-SpVf-qpJhQtD2mbOk"
BOT_TOKEN5 = "7919089085:AAFLwH8JkhkhSM9ZBqGRdWhjp9SLTqE0xDY"
BOT_TOKEN6 = "7684246925:AAHuiEEC7eZB8NNHmG_XF3H1AUh0DZHD_PU"
BOT_TOKEN7 = "7936107468:AAEidq9zyULmVjk5HppXphX5gB40eSxM63I"
BOT_TOKEN8 = "7642418300:AAGuwmUmn9Z8wybsovBn0a0IsmZxsedywrY"
BOT_TOKEN9 = "7730646813:AAFI2uQa6u82fMEYwseZCcuDZutdu7qDGNY"
BOT_TOKEN10 = "8033634538:AAGqOvM5pFgq1uIBE48Mj542FsSSTNSG2g8"

SUDO_USERS = [8169621656]
OWNER_ID = "8169621656"
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
