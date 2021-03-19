import vk_api as api
import random
from vk_api.longpoll import VkLongPoll as lPoll, VkEventType as eType


class Bot:

    def __init__(self, token):
        self.token = str(token)
        self.vk = api.VkApi(token=token)

    def send_msg(self, user_id, msg, attachment=''):
        self.vk.method('messages.send',
                       {'user_id': user_id, 'message': msg, 'random_id': random.randint(0, 10000000000000000000000000),
                        'attachment': attachment})

