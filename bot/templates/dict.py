from bot.templates.message import Message


class Methods:
    SEND = 'messages.send'
    GET_LP = 'messages.getLongPollServer'
    GET_UPLOAD_SERVER = 'photos.getMessagesUploadServer'


class AttachmentsTypes:
    PHOTO = 'photo'
    VIDEO = 'video'
    AUDIO = 'audio'
    DOC = 'doc'
    WALL = 'wall'
    MARKET = 'market'
    POLL = 'poll'


class MessageTemplates:
    NOT_DEFINED = Message(message='Моя твоя не понимать!',
                          lat=None,
                          long=None,
                          attachment=None)


# Message(user_id=None,
#         random_id=None,
#         peer_id=None,
#         peer_ids=None,
#         domain=None,
#         chat_id=None,
#         message=None,
#         lat=None,
#         long=None,
#         attachment=None)
