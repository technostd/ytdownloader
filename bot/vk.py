import random

from vk_api.vk_api import VkApiGroup

from bot.templates.attachment import Attachment
from bot.templates.message import Message
from bot.templates.dict import Methods


class VK(VkApiGroup):

    def __init__(self, token):
        super().__init__(token=token)

    def get_long_poll(self, token):
        self.method(Methods.GET_LP, {'access_token': token})

    def send_message(self, message: Message):
        self.method(Methods.SEND, message)

    def upload_message_photo(self, filename: str):
        self.method(Methods.GET_UPLOAD_SERVER)

    @staticmethod
    def str_dict(dictionary):
        result = ''
        for i in dictionary:
            result += str(i) + ','
        result = result[:len(result) - 1]
        return result

# Message:
# {
#   user_id: int,
#   random_id: float,
#   peer_id: int,
#   peer_ids: str,
#   domain: str,
#   chat_id: int,
#   message: str,
#   lat: float,
#   long: float,
#   attachment: str
# }
