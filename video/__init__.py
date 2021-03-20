"""import pytube
import time
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

_path_ = 'C:\Files\ytdownloader'


class Video:

    def __init__(self, url, time_borders=''):
        self.youTubeURL = url
        self.timeBorders = time
        self.currentTime = str(time.time()).replace('.', '_')

    def download(self):
        downloading_video = pytube.YouTube(self.youTubeURL)
        filename_downloaded = 'downloaded_' + self.currentTime
        downloading_video.streams.filter(progressive=True, file_extension='mp4') \
            .desc() \
            .first() \
            .download(output_path=__path__, filename=filename_downloaded + '.')


    def check_url(self):




filenameCut = 'cut_' + currentTime

ffmpeg_extract_subclip(f.txt"video/cutted{name}.mp4", 61, 360, targetname=f.txt"{name}.mp4")
"""