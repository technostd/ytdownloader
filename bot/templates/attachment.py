from bot.templates.dict import AttachmentsTypes as ATypes
from urllib.parse import urlparse as parser

DOMAIN_VK = 'https://vk.com/'


class Attachment:
    def __init__(self, a_type, a_owner_id, a_media_id, a_access_key=''):
        if a_type not in [ATypes.PHOTO,
                          ATypes.VIDEO,
                          ATypes.AUDIO,
                          ATypes.DOC,
                          ATypes.WALL,
                          ATypes.MARKET,
                          ATypes.POLL]:
            raise Exception('UndefinedTypeException')
        self.type = str(a_type)
        self.owner = int(a_owner_id)
        self.media = int(a_media_id)
        self.key = str(a_access_key)

    def __str__(self):
        if self.key == '':
            return self.type + str(self.owner) + '_' + str(self.media)
        else:
            return self.type + str(self.owner) + '_' + str(self.media) + '_' + str(self.key)

    def url(self):
        return  + str(self)

    @staticmethod
    def parse(url):

        str(url)
        parsed = Attachment()
