import random
from time import time


class Message(dict):

    def __init__(self, user_id=None, peer_id=None,
                 peer_ids=None, domain=None, chat_id=None, message=None, lat=None, long=None, attachment=None):
        super().__init__()
        self.user_id = int(user_id) if user_id is not None else None
        random.seed = time()
        self.random_id = random.randint(-9223372036854775808, 9223372036854775807)
        self.peer_id = int(peer_id) if peer_id is not None else None
        self.peer_ids = list(peer_ids) if peer_ids is not None else None
        self.domain = str(domain) if domain is not None else None
        self.chat_id = int(chat_id) if chat_id is not None else None
        self.message = str(message) if message is not None else None
        self.lat = float(lat) if lat is not None else None
        self.long = float(long) if long is not None else None
        self.attachment = attachment if attachment is not None else None

    def __iter__(self):
        return self.dict().__iter__()

    def __getitem__(self, item):
        return self.dict().get(item)

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
            'attachment': self.attachment
        }
        to_del = []
        for i in result:
            if result.get(i) is None:
                to_del.append(i)

        for i in to_del:
            result.__delitem__(i)

        return result
