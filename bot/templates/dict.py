from random import random

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
    NOT_DEFINED = Message(message='Моя твоя не понимать!')
    ASK_VIDEO_URL = Message(message='Укажите ссылку на видео')


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
