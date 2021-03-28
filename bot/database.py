import pickle

from bot.templates.peer import Peer


class Database:

    def __init__(self):
        self.db = open('database.pickle')

    def save_peer(self, peer_id: int):
        try:
            self.get_peer(peer_id)
        except Exception('NotFoundException'):


    def get_peer(self, peer_id: int):
        """
        Получить объект диалога по его ID

        :param peer_id: ID диалога
        :type: int

        :raise NotFoundException: Не найден диалог по указанному ID

        :return: Объект класса Peer
        :type: Peer
        """
        loaded = pickle.load(self.db)
        for i in loaded.peers:
            if i.get('id') == peer_id:
                return Peer(i)
        raise Exception('NotFoundException')
