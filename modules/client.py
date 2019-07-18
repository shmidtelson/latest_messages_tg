from telethon import TelegramClient
from settings import NAME, APP_ID, API_HASH

client = TelegramClient(NAME, APP_ID, API_HASH)
client.start()