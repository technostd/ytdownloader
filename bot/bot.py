from bot.longpoll import LongPoll
from bot.vk import VK


DOMAIN_VK = 'https://vk.com/'


class Bot:

    def __init__(self, token):
        self.session = VK(token)
        self.long_poll = LongPoll(self.session)

    def start_poll(self):
        self.long_poll.listen()

