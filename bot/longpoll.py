from vk_api.longpoll import VkLongPoll as lPoll, VkEventType as eType
from bot.templates.dict import MessageTemplates

from bot.vk import VK


class LongPoll(lPoll):

    def __init__(self, vk: VK):
        super().__init__(vk=vk)
        self.vk = vk

    def listen(self):
        while True:
            event = super().check()
            if event.type == eType.MESSAGE_NEW:
                if False:
                    pass
                else:
                    message = MessageTemplates.NOT_DEFINED
                    message.peer_id = event.peer_id
                    self.vk.send_message(message)
