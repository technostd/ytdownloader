# -------------------------------------------------------------
# |
# | Copyright Techno's studio 2021
# |
# | Project GitHub: https://github.com/technostd/ytdownloader/
# | Project VK: https://vk.com/yt_download
# |
# | Developer's GitHub: https://github.com/technostd/
# | Developer's VK: https://vk.com/technostd
# |
# | All rights reserved
# |
# -------------------------------------------------------------

from bot.bot import Bot

# --- const --- #
TOKEN = 'd29f7cb21202b0ed5892a5cf732848ee54bae4e8accadef52d88140be1c9ab2d9bff7ca45bf306afa66ba'  # access token
GROUP_ID = 203330548  # group for connecting

if __name__ == '__main__':
    bot = Bot(token=TOKEN, group_id=GROUP_ID)  # bot initialisation
    t = bot.start_poll()  # start long pooling VK API
