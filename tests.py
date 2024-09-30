import yt_dlp
from datetime import date
import os

# Get the current user's name.
user = os.getlogin()
# Goes to the Music directory.
music_path = 'C:/Users/{username}/Music'.format(username=user)
os.chdir(music_path)
# fetch toady's date.
today = date.today()
# create a path where downloaded music will be stored.
created_path = music_path + "/{date}-music".format(date=today)

if os.path.exists(created_path):
    pass
else:
    os.mkdir("{date}-music".format(date=today))

os.chdir(created_path)

# download options
ydl_settings = {
    'format': 'bestaudio/best',
    'postprocessors':[{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }],
    'ffmpeg_location': "C:/Users/elabd/scoop/shims/ffmpeg.exe",
    'outtmpl': created_path + "/%(title)s.%(ext)s"
}

with yt_dlp.YoutubeDL(ydl_settings) as ydl:
    ydl.download(['https://youtu.be/XHdJS1D66G4'])

print("successfully downloaded")