import os
import json
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

APP_PATH = os.path.dirname(os.path.abspath(__file__))
NAME = os.getenv("NAME")
APP_ID = os.getenv("APP_ID")
API_HASH = os.getenv("API_HASH")
PATH_TO_EXPORT_DATA = os.getenv("PATH_TO_EXPORT_DATA")
GROUP_NAME = os.getenv("GROUP_NAME")

def ROOT_DIR():
    """Returns project root folder."""
    return Path(__file__).parent

def CONFIGS_DIR():
    return os.path.join(ROOT_DIR(), 'confs')


def LOGGING_CONFIG():
    with open(CONFIGS_DIR() + '/logging.json', 'r') as jfile:
        return json.load(jfile)
