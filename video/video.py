import time
import ffmpeg
from pytube import YouTube


class Video:
    PATH = 'G:\\Files\\ytdownloader\\media\\'
    EXT = '.mp4'

    def __init__(self, url: str, start_time=0, end_time=None):

        """ Инициализация видео

        :param url: URL видео
        :type url: str

        :param start_time: Таймкод начала обрезанного куска
        :type start_time: int

        :param end_time: Таймкод конца обрезанного куска
        :type end_time: int

        """

        self.filename = ''.join(str(int(time.time())))
        self.video = YouTube(url)
        self.start_time = int(start_time)
        self.end_time = int(end_time) if end_time is not None else None

    def get_options(self):

        """ Получить список доступных опций загрузки видео

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

        """ Путь к файлу для отправки в ВК

          :return: Строка, содержащая путь к готовому файлу

        """

        clip = ffmpeg.input(self.PATH + self.filename + self.EXT,
                            ss=self.timecode_to_hhmmss(self.start_time),
                            t=self.timecode_to_hhmmss(self.end_time - self.start_time))
        clip = ffmpeg.output(clip, self.PATH + self.filename + '_edited' + self.EXT)
        ffmpeg.run(clip)
        return self.PATH + self.filename + '_edited' + self.EXT

    def get_video_path(self):
        return self.PATH + self.filename + '.mp4'

    @staticmethod
    def timecode_to_hhmmss(timecode):
        timecode = int(timecode) % 86400
        sp_h = timecode // 3600
        timecode = timecode % 3600
        sp_m = timecode // 60
        sp_s = timecode % 60

        hh = str(sp_h).zfill(2)
        mm = str(sp_m).zfill(2)
        ss = str(sp_s).zfill(2)

        return f'{hh}:{mm}:{ss}'


if __name__ == '__main__':
    v = Video('https://www.youtube.com/watch?v=mZVHbgKw558', 5000, 50000)
    v.download()
    v.cut()
