import yt_dlp
from datetime import date
from colorama import Fore
import os
import argparse

parser = argparse.ArgumentParser(description="Music Downloader")

parser.add_argument(
    'url',
    metavar='url',
    type=str,
    help='url of the video that will be downloaded'
)
parser.add_argument(
    '-path',
    help='Downloading path'
)
parser.add_argument(
    '-ply',
    action='store_true',
    help='Indicates that the url is a playlist'
)

args = parser.parse_args()

def max_duration_filter(info, *, incomplete):
    duration = info.get('duration')
    if duration > 600:
        return "Skipping the video -> too long"
    
def get_download_path() -> str:
    # Get the current user's name.
    user = os.getlogin()
    # Goes to the Music directory.
    music_path = 'C:/Users/{username}/Music'.format(username=user)
    os.chdir(music_path)
    # fetch toady's date.
    today = date.today()
    # create a path where downloaded music will be stored.
    if args.path is None:
        created_path = music_path + "/{date}-music".format(date=today)
    else:
        created_path = music_path + "/" + args.path

    # check if the new directory already exists
    if os.path.exists(created_path):
        pass
    else:
        os.mkdir(created_path)
    
    return created_path


def download_music(url, is_playlist=False):
    '''
    Download audio (.mp3 format) of the youtube video
    linked with the specified url.
    ""url : video's url
    '''
    # goes to the download directory
    download_path = get_download_path()
    os.chdir(download_path)

    # download options
    ydl_settings = {
        'format': 'bestaudio/best',
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
        'ffmpeg_location': "C:/Users/{username}/scoop/shims/ffmpeg.exe".format(username=os.getlogin()),
        'match_filter': max_duration_filter,
        'outtmpl': download_path + "/%(title)s.%(ext)s",
        'noplaylist': not is_playlist
    }

    with yt_dlp.YoutubeDL(ydl_settings) as ydl:
        ydl.download([url])

    print(f"{Fore.YELLOW}successfully downloaded{Fore.WHITE}")

download_music(args.url, args.ply)