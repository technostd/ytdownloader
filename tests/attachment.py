import unittest
from bot.templates.attachment import Attachment
from bot.vk import VK
from urllib.parse import urlparse as parser

class MyTestCase(unittest.TestCase):

    def test_stringify(self):
        print(parser('https://vk.com/leodesignstudio?z=photo-201038246_457239020%2Falbum-201038246_0%2Frev'))


if __name__ == '__main__':
    unittest.main()
