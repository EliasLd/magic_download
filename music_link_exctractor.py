from youtubesearchpython import VideosSearch as vs, PlaylistsSearch as ps
from colorama import Fore

def is_valid_duration(duration):
    '''
    Check if the video is not longer than 10 minutes.
    Original duration format is : mm:ss or hh:mm:ss
    -> Need ton convert it.
    ""return: Boolean.
    '''
    # Split the duration
    parts = list(map(int, duration.split(':')))
    # Format mm:ss
    if len(parts) == 2:
        minutes, seconds = parts
    # Format hh:mm:ss
    elif len(parts) == 3:
        hours, minutes, seconds = parts
        minutes += 60 * hours
    # Unknown format
    else:
        return False
    
    # Convert total duration to seconds
    total_seconds_duration = seconds + 60 * minutes
    # Check if the video is shorter than 10 minutes (600 seconds)
    return total_seconds_duration < 600

def get_video_url(name, is_playlist=False):
    '''
    Use the youtubesearchpython package to search a youtube video
    or playlist by its name and return the url.
    ""return: str containing the video or playlist url.
    '''
    if is_playlist:
        search = ps(name, limit=5).result()
        for playlist in search['result']:
            print(f"{Fore.YELLOW}Found playlist{Fore.WHITE} : {playlist.get('title')}")
            validation = input(f"{Fore.YELLOW}Are you sure about this download [y/n] ? >> {Fore.WHITE}")
            if validation == 'y':
                return playlist['link']
    else:
        search = vs(name, limit=5).result()
        for video in search['result']:  
            if is_valid_duration(video.get('duration')):
                print(f"{Fore.YELLOW}Found video{Fore.WHITE} : {video.get('title')} \n{Fore.YELLOW}duration{Fore.WHITE} : {video.get('duration')}")
                validation = input(f"{Fore.YELLOW}Are you sure about this download [y/n] ? >> {Fore.WHITE}")
                if validation == 'y':
                    return video['link']
    return None