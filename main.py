import os
import time
import logging.config
import schedule
from settings import LOGGING_CONFIG
from modules.latest_news_tg import get_latest_news

if __name__ == '__main__':
    logging.config.dictConfig(LOGGING_CONFIG())

    get_latest_news()

    schedule.every().hour.do(get_latest_news)

    while 1:
        schedule.run_pending()
        time.sleep(1)

