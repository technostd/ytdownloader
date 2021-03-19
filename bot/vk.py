import random

from bot.templates.attachment import Attachment
from bot.templates.dict import Methods


class VK:

    def __init__(self, vk):
        self.session = vk

    def get_long_poll(self, token):
        self.session.method(Methods.getLP, {'access_token': token})

    def send_msg(self, peer_id=None, peer_ids=None, msg=None, attachments=None):
        message = {
            'peer_id': peer_id,
            'peer_ids': peer_ids,
            'message': msg,
            'random_id': random.random(),
            'attachment': self.str_dict(attachments)
        }

        self.session.method(Methods.send, message)

    @staticmethod
    def str_dict(dictionary):
        result = ''
        for i in dictionary:
            result += str(i) + ','
        result = result[:len(result) - 1]
        return result

# user_id, random_id, peer_id, peer_ids, domain, chat_id, message, lat, long, attachment
