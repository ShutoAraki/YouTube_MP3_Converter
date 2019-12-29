from __future__ import unicode_literals
import youtube_dl, subprocess, pipes
from pydub import AudioSegment

print("======= Welcome to YouTube MP3 Downloader =========")
url = input("Enter an URL: ")

start_min = float(input("\nStart min: "))
start_sec = float(input("Start sec: "))
end_min = float(input("End min: "))
end_sec = float(input("End sec: "))

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

start_time = (start_min*60 + start_sec) * 1000
end_time = (end_min*60 + end_sec) * 1000

file_name = input("\nCopy and paste the title here (including .mp3): ")

song = AudioSegment.from_mp3(file_name)
extract = song[start_time:end_time]

pref_file_name = input("Preferred file name?: ")

extract.export(pref_file_name + '.mp3', format='mp3')

file_name_esc = pipes.quote(file_name)
rm_old_file = "rm " + file_name_esc
subprocess.run(rm_old_file, shell=True)
