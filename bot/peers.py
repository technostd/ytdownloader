"""import pickle

from bot.templates.peer import Peer


class Peers:

    def __init__(self):
        self.file = open('peers.pickle')
        self.peers = pickle.load(self.file)




    def save_peer(self, peer: Peer):
        loaded = pickle.load(self.file)
        try:
            peer = self.get_peer(peer.id)

        except Exception('NotFoundException'):
            peer = Peer({"id": peer.id, 'last_action': peer.last_action})


        pickle.dump(peer, self.file)

    def get_peer(self, peer_id: int):
        \"""
        Получить объект диалога по его ID

        :param peer_id: ID диалога
        :type: int

        :raise NotFoundException: Не найден диалог по указанному ID

        :return: Объект класса Peer
        :type: Peer
        \"""
        loaded = pickle.load(self.file)
        for i in loaded.peers:
            if i.get('id') == peer_id:
                return Peer(i)
        raise Exception('NotFoundException')
"""