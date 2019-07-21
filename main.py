import os
import time
import logging
# import schedule
import schedule as schedule

from modules.latest_news_tg import get_latest_news
from modules.update_profile import run_update_profile


logging.basicConfig(filename="logs.log", level=logging.DEBUG)

get_latest_news()

schedule.every().hour.do(get_latest_news)
schedule.every().day.at("00:30").do(run_update_profile)

while 1:
    schedule.run_pending()
    time.sleep(1)

