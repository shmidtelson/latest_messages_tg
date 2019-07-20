import os
import pytz
import json
from telethon import TelegramClient, functions, sync
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.users import GetFullUserRequest

from modules.client import client
from settings import PATH_TO_EXPORT_DATA, GROUP_NAME


def get_latest_news():
    for the_file in os.listdir(os.path.join(PATH_TO_EXPORT_DATA, 'images')):
        file_path = os.path.join(os.path.join(PATH_TO_EXPORT_DATA, 'images'), the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

    # GET CHANNEL ENTITY
    channel_entity = client.get_entity(GROUP_NAME)
    # GET HISTORY
    m = client(GetHistoryRequest(
        peer=channel_entity,
        limit=15,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))
    result = []
    for message in m.messages:
        date = message.date
        local_tz = pytz.timezone('Europe/Minsk')
        local_dt = date.replace(tzinfo=pytz.utc).astimezone(local_tz)

        user = client(GetFullUserRequest(
            id=message.from_id
        ))

        user = user.to_dict()
        photo = client(functions.photos.GetUserPhotosRequest(
            user_id=user['user']['id'],
            offset=0,
            max_id=0,
            limit=1
        ))

        dict_filepath = f'images/{user["user"]["id"]}.jpg'
        client.download_media(photo.photos[0], os.path.join(PATH_TO_EXPORT_DATA, dict_filepath))

        dict_id = message.id
        dict_message = message.message.replace("\n", "")
        dict_name = f'{user["user"].get("first_name")} {user["user"].get("last_name", "")}'
        dict_date = local_dt.strftime('%Y-%m-%d %H:%I:%S')

        result.append({
            'id': dict_id,
            'name': dict_name,
            'message': dict_message,
            'date': dict_date,
            'image_path': dict_filepath
        })
    result = list(reversed(result))
    with open(os.path.join(PATH_TO_EXPORT_DATA, 'latest_tg_messages.json'), 'w') as fm:
        fm.write(json.dumps(result))
