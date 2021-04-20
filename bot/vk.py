import random

from vk_api.upload import VkUpload
from vk_api.vk_api import VkApiGroup  # , VkApiMethod

from bot.templates.dict import Methods
from bot.templates.message import Message


class Vk(VkApiGroup):

    vk = None

    def __init__(self, token):
        super().__init__(token=token)
        # self.method = VkApiMethod(self)
        self.upload = VkUpload(self)

    def get_long_poll(self, token):
        return self.method(Methods.GET_LP, {'access_token': token})

    def send_message(self, message: Message):
        # @debug m = message.dict()
        return self.method(Methods.SEND, message.dict())

    def upload_message_document(self, filename: str, peer_id):
        return self.upload.document_message([filename], 'video', peer_id=peer_id)

    def upload_message_photo(self, filename: str, peer_id):
        return self.upload.photo_messages([filename], peer_id=peer_id)

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
