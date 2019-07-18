import os
import pytz
import json
from telethon import functions
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.users import GetFullUserRequest

from settings import PATH_TO_EXPORT_DATA, GROUP_NAME


def get_latest_news(client):
    def clear_images(folder):
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)

    clear_images(os.path.join(PATH_TO_EXPORT_DATA, 'images'))


    # GET CHANNEL ENTITY
    channel_entity = client.get_entity(GROUP_NAME)
    # GET HISTORY
    messages = client(GetHistoryRequest(
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
    for message in messages.messages:
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

        filepath = f'images/{user["user"]["id"]}.jpg'
        client.download_media(photo.photos[0], os.path.join(PATH_TO_EXPORT_DATA, filepath))

        result.append({
            'id': message.id,
            'name': f'{user["user"]["first_name"]} {user["user"]["last_name"]}',
            'message': message.message,
            'date': local_dt.strftime('%Y-%m-%d %H:%I:%S'),
            'image_path': filepath
        })
    result = list(reversed(result))
    with open(os.path.join(PATH_TO_EXPORT_DATA, 'latest_tg_messages.json'), 'w') as fm:
        fm.write(json.dumps(result))