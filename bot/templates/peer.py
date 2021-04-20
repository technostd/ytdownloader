class Peer:
    def __init__(self, json):
        self.id = json.get('id')
        self.last_action = json.get('last_action')
