from vk_api.longpoll import VkLongPoll

from bot.longpoll import LongPoll
from bot.vk import Vk
import bot.database as database

DOMAIN_VK = 'https://vk.com/'


class Bot:

    def __init__(self, token):
        self.session = Vk(token)
        self.long_poll = VkLongPoll(self.session)
        self.lp = LongPoll(self.session)

    def start_poll(self):
        self.lp.listen()
