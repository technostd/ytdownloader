from time import time
from datetime import datetime


class Video:

    DOWNLOAD_PATH = 'path'
    EDITED_PATH = 'path'

    def __init__(self, url, start_time=0, end_time=None):
        """
        Инициализация видео
        :param url: URL видео
        :param start_time: Таймкод начала обрезанного куска
        :param end_time: Таймкод конца обрезанного куска
        """
        
        '''
        В инициализаторе должны сохраняться ссылка, границы обрезки.
        '''

    def get_options(self):
        """
        Получить список доступных опций загрузки видео
        :return:  Список опций
        :type: list
        """

    def download(self):
        """
        Загрузка видео с YouTube
        """

        '''
        Функция self.download должна загружать видео с YouTube и сохранять в объекте путь к файлу.
        Должна вызывать функцию self.cut при необходимости.
        
        '''

    def cut(self):
        """
        Сохранить обрезанное видео
        :return:
        """

    def get_video_path(self):
        """
        Путь к файлу для отправки в ВК
        :return: Строка, содержащая путь к готовому файлу
        :type: str
        """