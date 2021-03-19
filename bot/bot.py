from vk_api import VkApi
from bot.vk import VK

import random
from vk_api.longpoll import VkLongPoll as lPoll, VkEventType as eType


class Bot:

    def __init__(self, token):
        self.token = str(token)
        self.vk = VK(VkApi(token=token))

    def send(self):
        pass

