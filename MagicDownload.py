from colorama import Fore
import subprocess
import re

from music_link_exctractor import get_video_url

DESCRIPTION = r'''

[--------------------------------------------------------------------]
|     __  __           _    ___                  _              _    |
|    |  \/  |__ _ __ _(_)__|   \ _____ __ ___ _ | |___  __ _ __| |   |
|    | |\/| / _` / _` | / _| |) / _ \ V  V / ' \| / _ \/ _` / _` |   |
|    |_|  |_\__,_\__, |_\__|___/\___/\_/\_/|_||_|_\___/\__,_\__,_|   |
|                |___/                                               |
[--------------------------------------------------------------------]

'''

def get_argument_list():
    cmd_line = input(f"{Fore.BLUE}MagicDownload/VideoDL $ >> {Fore.WHITE}")

    if cmd_line == '..' or cmd_line is None:
        return [], True

    pattern = r'\s+'
    cmd_line_list = re.split(pattern, cmd_line)
    cmd_line_list = [re.sub(r'_', ' ', item) for item in cmd_line_list]

    if len(cmd_line_list) == 1:
        cmd_line_list.append(None)

    video = cmd_line_list[0]
    cmd_line_list[0] = get_video_url(video)

    return cmd_line_list, False


def menu():
    choix = input(f"{Fore.BLUE}MagicDownload $ >> {Fore.WHITE}")
    match choix:
        case "dl":
            end = False
            while not end : 
                cmd_args, end = get_argument_list()
                if end:
                    break
                if cmd_args[1] is None:
                    subprocess.call(['python', 'music_downloader.py', cmd_args[0]])
                else :
                    subprocess.call(['python', 'music_downloader.py', cmd_args[0], "-path", cmd_args[1]])
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
        
    

