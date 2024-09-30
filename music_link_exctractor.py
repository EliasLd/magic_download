from youtubesearchpython import VideosSearch as vs
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

def get_video_url(video_name):
    '''
    Use the youtubesearchpython package to search a youtube video
    by its name and return the url of the video.
    ""return: str containing the video url.
    '''
    # Search for videos matching the name on youtube
    search = vs(video_name, limit=3).result()
    # return the url of the first video matching the duration limits
    for video in search['result']:  
        if is_valid_duration(video.get('duration')):
            print(f"{Fore.YELLOW}Found{Fore.WHITE} : {video.get('title')} \n{Fore.YELLOW}duration{Fore.WHITE} : {video.get('duration')}")
            validation = input(f"{Fore.YELLOW}Are you sure about this download [y/n] ? >> {Fore.WHITE}")
            if validation == 'y':
                return video['link']
    return None