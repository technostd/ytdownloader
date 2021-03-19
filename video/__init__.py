import pytube
import time
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

yt = pytube.YouTube('https://www.youtube.com/watch?v=shyWnNdtqqM')
name = 'downloaded_' + str(time.time()).replace('.', '_')
print(name)
yt.streams.filter(progressive=True, file_extension='mp4').desc().first().download(output_path='D:\youtube',
                                                                                  filename=name + '.')
ffmpeg_extract_subclip(f"D:\youtube\{name}.mp4", 61, 360, targetname="output.mp4")

