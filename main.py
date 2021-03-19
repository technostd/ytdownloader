from bot.bot import Bot
from bot.templates.attachment import Attachment
from bot.vk import VK
from vk_api import VkApi

if __name__ == '__main__':
    token = '428421dfa3d754ab3a273c0344f77fa60b6d20832b1e00b385491af47ea3c9af7b8a248351c54cd0eb89b'
    bot = Bot(token=token)
    vk = VK(VkApi(token=token))
    vk.send_msg(peer_id=42589261,
                attachments=[Attachment('photo', -163553110, 457239017), Attachment('photo', -201038246, 457239020)])
