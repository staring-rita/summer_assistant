from settings import LOGIN, PASSWORD

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType, VkLongpollMode
import requests


session = requests.Session()
print("я тут")
vk_session = vk_api.VkApi(LOGIN, PASSWORD)
vk_session.auth

try:
    vk_session.auth(token_only=True)
    print("всё хорошо")
except vk_api.AuthError as error_msg:
    print(error_msg)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        if event.from_user:
            vk.mess