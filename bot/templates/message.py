import random
from time import time

from bot.templates.attachment import Attachment
from bot.templates.keyboard import Keyboard
# from bot.vk import Vk


class Message(dict):

    def __init__(self, user_id=None,
                 peer_id: int = None,
                 peer_ids: list = None,
                 domain: str = None,
                 chat_id: int = None,
                 message: str = None,
                 lat: float = None,
                 long: float = None,
                 attachment: Attachment or list = None,
                 keyboard=None):
        super().__init__()
        self.user_id = user_id
        random.seed = time()
        self.random_id = random.randint(-9223372036854775808, 9223372036854775807)
        self.peer_id = peer_id
        self.peer_ids = peer_ids
        self.domain = domain
        self.chat_id = chat_id
        self.message = message
        self.lat = lat
        self.long = long
        self.attachment = attachment
        self.keyboard = keyboard

    def __iter__(self):
        return self.dict().__iter__()

    def __getitem__(self, item):
        return self.dict()[item]

    def __len__(self):
        return len(self.dict())

    def dict(self):
        result = {
            'user_id': self.user_id,
            'random_id': self.random_id,
            'peer_id': self.peer_id,
            'peer_ids': self.peer_ids,
            'domain': self.domain,
            'chat_id': self.chat_id,
            'message': self.message,
            'lat': self.lat,
            'long': self.long,
            'attachment': self.attachment,
            'keyboard': self.keyboard
        }
        to_del = []
        for key in result:
            if result[key] is None:
                to_del.append(key)

        for key in to_del:
            result.__delitem__(key)

        return result

    def user_id(self, user_id: int):
        self.user_id = user_id
        return self

    def peer_id(self, peer_id: int):
        self.peer_id = peer_id
        return self

    def peer_ids(self, peer_ids: list):
        self.peer_ids = peer_ids
        return self

    def domain(self, domain: str):
        self.domain = domain
        return self

    def chat_id(self, chat_id: int):
        self.chat_id = chat_id
        return self

    def message(self, message: str):
        self.message = message
        return self

    def lat(self, lat: float):
        self.lat = lat
        return self

    def long(self, long: float):
        self.long = long
        return self

    def attachment(self, attachment: Attachment or list):
        self.attachment = attachment
        return self

    def keyboard(self, keyboard: Keyboard):
        self.keyboard = keyboard
        return self

    # def send(self):
    #     if self.peer_id or self.peer_ids or self.user_id or self.chat_id:
    #         Vk.vk.send_message(self)


class MessageTemplates:
    NOT_DEFINED = Message(
        message=random.choice(['Эм, что?', 'Я не понял.', 'Не понимаю.', 'Повтори еще раз. Не слышу.']))
    ASK_VIDEO_URL = Message(message='Пока что мы принимаем видео только с YouTube')
    HINT = Message(message='Заполните шаблон')

