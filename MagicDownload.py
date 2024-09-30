from music_link_exctractor import get_video_url
from music_downloader import download_music
from colorama import Fore
import subprocess

DESCRIPTION = r'''

[--------------------------------------------------------------------]
|     __  __           _    ___                  _              _    |
|    |  \/  |__ _ __ _(_)__|   \ _____ __ ___ _ | |___  __ _ __| |   |
|    | |\/| / _` / _` | / _| |) / _ \ V  V / ' \| / _ \/ _` / _` |   |
|    |_|  |_\__,_\__, |_\__|___/\___/\_/\_/|_||_|_\___/\__,_\__,_|   |
|                |___/                                               |
[--------------------------------------------------------------------]

'''

def menu():
    choix = input(f"{Fore.BLUE}MagicDownload $ >> {Fore.WHITE}")
    match choix:
        case "dl":
            end = False
            while not end : 
                subprocess.run(["cls"], shell=True)
                video_name =""
                video_name = input(f"{Fore.BLUE}Video name ('..' to exit dl mode) $ >> {Fore.WHITE}")
                # Check if the exit command is entered
                if video_name == "..":
                    end = True
                    break
                
                url = get_video_url(video_name)
                if url is not None:
                    download_music(url)
            return False
        case "help":
            print("commands manual", end= ' --- ')
            print("dl -> enter video downloader mode\n \
                   quit -> exit MagicDownload")
            return False
        case "quit":
            return True
        

def main():
    print(Fore.BLUE + DESCRIPTION + Fore.WHITE)
    end = False
    while not end:
        end = menu()
        
main()
        
    

