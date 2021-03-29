import time

from moviepy.editor import VideoClip, CompositeVideoClip, VideoFileClip
from pytube import YouTube


class Video:
    PATH = 'G:\\ytdownloader\\media\\'

    def __init__(self, url: str, start_time=0, end_time=None):

        """
        Инициализация видео

        :param url: URL видео
        :type url: str

        :param start_time: Таймкод начала обрезанного куска
        :type start_time: int

        :param end_time: Таймкод конца обрезанного куска
        :type end_time: int

        """

        self.filename = ''.join(str(int(time.time())))
        self.video = YouTube(url)
        self.start_time = start_time
        self.end_time = int(end_time) if end_time is not None else None

    def get_options(self):

        """

        Получить список доступных опций загрузки видео

        :return:  Список опций

        """

        return self.video.streams

    def download(self):

        """

           Загрузка видео с YouTube

           :return: Путь к загруженному видео

        """

        path = self.get_options().filter(progressive=True, file_extension='mp4')\
            .order_by('resolution').desc().first().download(self.PATH, self.filename)

        if self.start_time != 0 or self.end_time is not None:
            path = self.cut()
        return path

    def cut(self):

        """

          Путь к файлу для отправки в ВК

          :return: Строка, содержащая путь к готовому файлу

        """
        clip = VideoFileClip(self.PATH + self.filename + '.mp4', audio=True)
        clip.subclip(self.start_time, self.end_time)
        clip.write_videofile(self.PATH + self.filename + '_edited.mp4')
        # clip(self.PATH + self.filename + '.mp4', self.start_time, self.end_time,
        #      targetname=self.PATH + self.filename + '_edited.mp4', )
        return self.PATH + self.filename + '_edited.mp4'

    def get_video_path(self):
        return self.PATH + self.filename + '.mp4'


if __name__ == '__main__':
    v = Video('https://www.youtube.com/watch?v=mZVHbgKw558', 5000, 50000)
    v.download()
    v.cut()
