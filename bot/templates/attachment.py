from bot.templates.dict import AttachmentsTypes as ATypes


class Attachment:
    def __init__(self, a_type, a_owner_id, a_media_id):
        if a_type not in [ATypes.photo,
                          ATypes.video,
                          ATypes.audio,
                          ATypes.doc,
                          ATypes.wall,
                          ATypes.market,
                          ATypes.poll]:
            raise Exception('UndefinedTypeException')
        self.type = str(a_type)
        self.owner = int(a_owner_id)
        self.media = int(a_media_id)

    def __str__(self):
        return self.type + str(self.owner) + '_' + str(self.media)

    def url(self):
        return 'https://vk.com/' + str(self)

    @staticmethod
    def str_dict(dictionary):
        result = ''
        for i in dictionary:
            result += str(i) + ','
        return result
