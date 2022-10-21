from pytube import Playlist
import os
import moviepy.editor as mob

link = input("Enter link: ")

yt = Playlist(link)

for video in yt.videos:
    print("Title: ", video.title)
    print("View: ", video.views.numerator)
    print("Author: ", video.author)
    print("Duration: ", video.length)
    print("Date: ", video.publish_date)

    stream = video.streams
    clip = stream.filter(mime_type="video/mp4")
    audio = stream.filter(mime_type="audio/mp4")

    clips = list(enumerate(clip))
    audios = list(enumerate(audio))

    for i in clips:
        print(i)

    print("Note: You can download Video and Audio up to only 720p")
    indexv = int(input("Which file you want: "))

    choice = int(input("Enter 1 to download audio file otherwise enter 0: "))

    for i in audios:
        print(i)

    indexa = int(input("Which file you want: "))
    print("Downloading...  video")
    old_file = clip[indexv].download('C:/Users/Hp/Videos/YouTubeVideo/')

    print("Video Downloading Done.")

    if choice:
        clip_file = 'C:/Users/Hp/Videos/YouTubeVideo/file1.mp4'
        audio_file = 'C:/Users/Hp/Videos/YouTubeVideo/file2.mp3'
        os.rename(old_file, clip_file)
        print("Downloading...  audio")
        old_file = audio[indexa].download()
        base, ext = os.path.splitext(old_file)
        os.rename(old_file, audio_file)
        print("Audio Downloading Done.")
        final_file = mob.VideoFileClip(clip_file).set_audio(mob.AudioFileClip(audio_file))
        final_file.write_videofile('C:/Users/Hp/Videos/YouTubeVideo/' + str(video.title) + '.mp4')
        os.remove(clip_file)
        os.remove(audio_file)
    print(video.title + " is Ready to Play")

os.startfile('C:/Users/Hp/Videos/YouTubeVideo/')
print('The playlist is ready to play')

