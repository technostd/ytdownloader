import re
from threading import Thread as Process
from time import sleep
from urllib.parse import urlparse as parser

from vk_api.longpoll import Event, VkEventType, VkLongPoll

from bot.templates.dict import MessageTemplates
from bot.templates.message import Message
from bot.vk import Vk


class LongPoll(VkLongPoll):
    LISTENING = True

    def __init__(self, vk: Vk):
        super().__init__(vk=vk)
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
            #  user = JSONDecoder.decode(open('dialogs.json').re)
            message = Message(peer_id=event.peer_id)
            if event.message == 'Видео':
                self.vk.send_message(self.get_message(MessageTemplates.ASK_VIDEO_URL, event.peer_id))
            elif len(re.findall('(?P<url>https?://[^\s]+)', event.message)) != 0:
                p = parser(re.findall('(?P<url>https?://[^\s]+)', event.message)[0])
                if p.netloc in ['www.youtube.com', 'youtu.be', 'youtube.com']:

                    self.send_message(message, message=)
                else:
                    self.send_message(message, message='Пока что мы принимаем видео только с YouTube')
            else:
                self.send_message(message, MessageTemplates.NOT_DEFINED.message)

    def send_message(self, message_obj: Message, message=None, attachment=None):
        message_obj.message = message
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
