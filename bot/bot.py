from vk_api.longpoll import VkLongPoll

from bot.longpoll import LongPoll
from bot.vk import Vk
import bot.peers as database

DOMAIN_VK = 'https://vk.com/'


class Bot:

    def __init__(self, token, group_id: int):
        self.session = Vk(token)
        self.long_poll = VkLongPoll(self.session)
        self.lp = LongPoll(self.session, group_id)

    def start_poll(self):
        self.lp.listen()
