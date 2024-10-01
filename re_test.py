import re
from colorama import Fore
from music_link_exctractor import get_video_url

def get_argument_list():
    cmd_line = input(f"{Fore.BLUE}MagicDownload/VideoDL $ >> {Fore.WHITE}")

    if cmd_line == '..' or cmd_line is None:
        return [], False

    pattern = r'\s+'
    cmd_line_list = re.split(pattern, cmd_line)
    cmd_line_list = [re.sub(r'_', ' ', item) for item in cmd_line_list]

    if len(cmd_line_list) == 1:
        cmd_line_list.append(None)

    video = cmd_line_list[0]
    cmd_line_list[0] = get_video_url(video)

    return cmd_line_list, True

print(get_argument_list())
