from bot.longpoll import LongPoll
from bot.vk import Vk

DOMAIN_VK = 'https://vk.com/'


class Bot:

    def __init__(self, token: str, group_id: int):
        self.session = Vk(token)
        Vk.vk = self.session
        self.lp = LongPoll(self.session, group_id)

    def start_poll(self):
        self.lp.listen()
