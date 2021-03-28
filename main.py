from threading import Thread

from bot.bot import Bot

TOKEN = 'd29f7cb21202b0ed5892a5cf732848ee54bae4e8accadef52d88140be1c9ab2d9bff7ca45bf306afa66ba'

if __name__ == '__main__':
    bot = Bot(token=TOKEN)
    t = bot.start_poll()

    # vk = VK(VkApi(token=TOKEN))
    # vk.send_msg(peer_id=42589261,
    #             attachments=[Attachment('photo', -163553110, 457239017), Attachment('photo', -201038246, 457239020)])
