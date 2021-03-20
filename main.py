from bot.bot import Bot
from bot.templates.attachment import Attachment
from bot.vk import VK
from vk_api import VkApi

TOKEN = '428421dfa3d754ab3a273c0344f77fa60b6d20832b1e00b385491af47ea3c9af7b8a248351c54cd0eb89b'

if __name__ == '__main__':
    bot = Bot(token=TOKEN)
    bot.start_poll()

    # vk = VK(VkApi(token=TOKEN))
    # vk.send_msg(peer_id=42589261,
    #             attachments=[Attachment('photo', -163553110, 457239017), Attachment('photo', -201038246, 457239020)])
