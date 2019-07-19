from telethon import TelegramClient, functions, sync
from settings import NAME, APP_ID, API_HASH

client = TelegramClient(NAME, APP_ID, API_HASH)
client.start()