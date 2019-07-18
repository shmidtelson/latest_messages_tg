import os
import schedule
import time
from telethon import TelegramClient
from modules.latest_news_tg import get_latest_news
from modules.update_profile import run_update_profile
from settings import NAME, APP_ID, API_HASH

client = TelegramClient(NAME, APP_ID, API_HASH)

get_latest_news(client)

schedule.every().hour.do(get_latest_news, client)
schedule.every().day.at("00:30").do(run_update_profile)

while 1:
    schedule.run_pending()
    time.sleep(1)

# get_latest_news(client)
# run_update_profile(client)
