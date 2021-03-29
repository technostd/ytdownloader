import time
from datetime import datetime
from pytube import streams, YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


class Video:
    DOWNLOAD_PATH = 'C:\\Users\\pushk\\Downloads\\'
    EDITED_PATH = 'path'

    def __init__(self, url, start_time=0, end_time=None):
        """
        Инициализация видео
        :param url: URL видео
        :param start_time: Таймкод начала обрезанного куска
        :param end_time: Таймкод конца обрезанного куска

        """
        self.filename = int(time.time())
        self.video = YouTube(url)
        self.url = url
        self.end_time = end_time
        self.start_time = start_time

    def get_options(self):
        """
        Получить список доступных опций загрузки видео
        :return:  Список опций
        :type: list
        """
        return self.video.streams

    def download(self):
        """
           Загрузка видео с YouTube
        """

        name = self.video.title
        return self.get_options().filter(progressive=True, file_extension='mp4')\
            .order_by('resolution').desc().first().download(Video.DOWNLOAD_PATH, name)

    def cut(self):
        """
          Путь к файлу для отправки в ВК
          :return: Строка, содержащая путь к готовому файлу
          :type: str

        """
        name = self.video.title
        return ffmpeg_extract_subclip(name+".mp4", self.start_time, self.end_time, targetname=name+"_edited.mp4")

    def get_video_path(self):
        return 0


Video('https://www.youtube.com/watch?v=mZVHbgKw558', 50, 100).cut()