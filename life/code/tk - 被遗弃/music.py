from pydub import AudioSegment
from pydub.playback import play


############
# 需要ffmpeg  ?? 不清楚
#
#
############
import threading
import time

class Th(threading.Thread):
    def __init__(self, thread_name, song):
        threading.Thread.__init__(self)
        self.setName(thread_name)
        self.mysong = song

    def run(self):
        try:
            print("开始播放")
            play(self.mysong)
            print(2222222)
        except:
            print("noting")

    def _delete(self):
        print("进程结束")


class clock():
    def __init__(self):
        self.hour = 0
        self.min = 0
        self.sec = 0
        self.time = 0

    def getTime(self, time):
        self.time = int(time)
        self.hour, self.min, self.sec = self.sec_to_min(time)
        print("{:0>2}:{:0>2}:{:0>2}".format(self.hour, self.min, self.sec))

    def sec_to_min(self, time):
        hour = time // 3600
        min, sec = divmod((time % 3600), 60)
        return (int(hour), int(min), int(sec))

    def count_down(self):
        cd_time = self.time
        while cd_time:
            time.sleep(1)
            cd_time -=1
            print("{:0>2}:{:0>2}:{:0>2}".format(*self.sec_to_min(cd_time)))
        print("over")


fname = '06.伊藤由奈 - 真冬の星座.mp3'
mysong = AudioSegment.from_mp3(fname)
th = Th("线程1", song=mysong)
th.start()
print("开始")
a = clock()
a.getTime(mysong.duration_seconds)
a.count_down()
# a.count_down()
print("222")





## sudo apt-get install python-pyaudio python3-pyaudio  http://people.csail.mit.edu/hubert/pyaudio/#downloads
# from pydub import AudioSegment
# from pydub.playback import play
# song = AudioSegment.from_mp3("M1.mp3")
# play(song)
# print(song.duration_seconds)


#########vlc
# import vlc
# import time
# from pydub import AudioSegment
#
# song = AudioSegment.from_mp3('06.伊藤由奈 - 真冬の星座.mp3')
#
#
# instance = vlc.Instance()
#
# #Create a MediaPlayer with the default instance
# player = instance.media_player_new()
#
# #Load the media file
# media = instance.media_new('06.伊藤由奈 - 真冬の星座.mp3')
# print(media.get_duration())
# #Add the media to the player
# player.set_media(media)
#
# #Play for 10 seconds then exit
# player.play()
#
# time.sleep(song.duration_seconds)