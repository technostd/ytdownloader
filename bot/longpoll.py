import json
import re
from threading import Thread as Process
from time import sleep

from vk_api.longpoll import Event, VkEventType, VkLongPoll

from bot.templates.attachment import Attachment
from bot.templates.dict import AttachmentsTypes as ATypes
from bot.templates.message import Message
from bot.vk import Vk
from video.video import Video


class LongPoll(VkLongPoll):
    LISTENING = True

    def __init__(self, vk: Vk, group_id: int):
        super().__init__(vk=vk, group_id=group_id)
        self.vk = vk

    def listen(self):
        self.LISTENING = True

        while self.LISTENING:
            for event in super().check():
                process = EventProcess(self, event)
                process.start()
                #  process.join(1)
            sleep(1)

    def for_event(self, event: Event):
        if event.type == VkEventType.MESSAGE_NEW and not event.from_me:
            patterns = {
                'command': r'http[s]*://[\S]+',
                'command_s': r'http[s]*://[\S]+\s\d+\s-s',
                'command_e': r'http[s]*://[\S]+\s\d+\s-e',
                'command_se': r'http[s]*://[\S]+\s\d+\s\d+',
            }
            if len(re.findall(patterns.get('command'), event.message)) != 0:
                for i in re.findall(patterns.get('command'), event.message):
                    message = Message(peer_id=event.peer_id,
                                      message='working')
                    self.send_message(message)
                    i = i.split(' ')
                    v = Video(i[0])

                    uploaded = self.vk.upload_message_document(v.download(), event.peer_id)

                    message = Message(peer_id=event.peer_id,
                                      attachment=Attachment(ATypes.DOC, uploaded.get('doc').get('owner_id'),
                                                            uploaded.get('doc').get('id')))
                    self.send_message(message)
            elif len(re.findall(patterns.get('command_s'), event.message)) != 0:
                for i in re.findall(patterns.get('command_s'), event.message):
                    message = Message(peer_id=event.peer_id,
                                      message='working')
                    self.send_message(message)
                    i = i.split(' ')
                    v = Video(i[0], i[1], i[2])

                    uploaded = json.loads(self.vk.upload_message_document(v.download(), event.peer_id))

                    message = Message(peer_id=event.peer_id,
                                      attachment=Attachment(ATypes.DOC, uploaded.get('doc').get('owner_id'),
                                                            uploaded.get('doc').get('id')))
                    self.send_message(message)

            #  user = JSONDecoder.decode(open('dialogs.json').re)
            message = Message(peer_id=event.peer_id)
            # if event.message == 'Видео':
            #     self.vk.send_message(self.get_message(MessageTemplates.ASK_VIDEO_URL, event.peer_id))
            # elif len(re.findall('(?P<url>https?://[^\s]+)', event.message)) != 0:
            #     p = parser(re.findall('(?P<url>https?://[^\s]+)', event.message)[0])
            #     if p.netloc in ['www.youtube.com', 'youtu.be', 'youtube.com']:
            #         self.send_message(message, message=MessageTemplates.HINT.message)
            #     else:
            #         self.send_message(message, message='Пока что мы принимаем видео только с YouTube')
            # else:
            #     self.send_message(message, MessageTemplates.NOT_DEFINED.message)

    def send_message(self, message_obj: Message, message=None, attachment=None):
        if message is not None:
            message_obj.message = message
        if attachment is not None:
            message_obj.attachment = attachment
        self.vk.send_message(message_obj)

    @staticmethod
    def get_message(template: Message, peer_id: int):
        message = template
        message.peer_id = peer_id
        return message


class EventProcess(Process):

    def __init__(self, pool: LongPoll, event: Event):
        super().__init__()
        self.event = event
        self.pool = pool

    def run(self):
        self.pool.for_event(self.event)
