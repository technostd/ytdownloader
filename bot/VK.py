import random

from bot.dict import Methods
from bot.dict import AttachmentsTypes as ATypes


class VK:

    def __init__(self, vk):
        self.vk = vk

    def send_msg(self, peer_id=None, peer_ids=None, msg=None, attachment=None):

        message = {
            'peer_id': peer_id,
            'peer_ids': peer_ids,
            'message': msg,
            'random_id': random.random(),
            'attachment': attachment
        }

        self.vk.method(Methods.send, message)
