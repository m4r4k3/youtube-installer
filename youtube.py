from pytube import YouTube 
from moviepy.editor import AudioFileClip
import os
import re
urll =input("enter your URL :").split(",")
os.system("cls")
regex ="(\w|\s)*"
type =input("what is the type V=1/A=0:")
for url in urll:
    yt = YouTube(url=url)
    if type =="0":
        path ="C:\\YourPath"
        video_stream = yt.streams.get_audio_only()
        title = re.search(regex , yt.title).group()
        video_stream.download(path , filename=title+".mp4")
        print("download complete")
        os.system("cls")
        audio = AudioFileClip(path+title+".mp4")
        audio.write_audiofile(path+title+".mp3")
        os.remove(path + title + ".mp4")
        os.system("cls")
        print("converting complete")
    elif type =="1":
        path="C:\\YourPath"
        ress= float("inf")
        stream = yt.streams
        res =[i.resolution for i in stream ]
        res =list(set(res))

        if None in res:
            res.remove(None)

        os.system("cls")
        res.sort()
        print("available resolutions :")
        [print("    ",i) for i in res]
        
        while ress > len(res):
            ress = int(input('choose a resolution:'))
        vid = stream.filter(res = res[ress-1]).first()
        vid.download(path )
        os.system("cls")
        print("download complete")
    else:
        print("error")
