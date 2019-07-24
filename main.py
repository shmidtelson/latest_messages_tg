import os
import time
import logging
import schedule

from modules.latest_news_tg import get_latest_news
from modules.update_profile import run_update_profile

if __name__ == '__main__':
    logging.basicConfig(filename="logs.log", level=logging.DEBUG)

    schedule.every().hour.do(get_latest_news)

    while 1:
        schedule.run_pending()
        time.sleep(1)

