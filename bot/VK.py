import random


class VK:

    def __init__(self, vk):
        self.vk = vk

    def send_msg(self, user_id, user_ids=None, msg=None, attachment=None):
        self.vk.method('messages.send',
                       {
                           'user_id': user_id,
                           'message': msg,
                           'random_id': random.randint(0, 10000000000000000000000000),
                           'attachment': attachment
                       })
