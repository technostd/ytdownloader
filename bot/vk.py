import random

from bot.templates.dict import Methods


class VK:

    def __init__(self, vk):
        self.vk = vk

    def send_msg(self, peer_id=None, peer_ids=None, msg=None, attachments=None):

        message = {
            'peer_id': peer_id,
            'peer_ids': peer_ids,
            'message': msg,
            'random_id': random.random(),
            'attachment': attachment
        }

        self.vk.method(Methods.send, message)


#user_id, random_id, peer_id, peer_ids, domain, chat_id, message, lat, long, attachment