# Magicdownload


MagicDownload is an open-source tool usable in a terminal on Windows, Linux, and macOS, allowing you to download YouTube videos/playlists in MP3 format. Developed entirely in Python, it uses well-known packages such as [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [youtube-search-python](https://pypi.org/project/youtube-search-python/).

## Requirements

To download it on your machine:

```git
git clone https://github.com/EliasLd/magic_download.git
```

### Required Tools

MagicDownload relies on several packages and utilities. For ease of use, it is recommended to create a Python virtual environment. Go to the MagicDownload installation folder or any location on your machine:

```bash
python3 -m venv "name_of_your_venv"
```

Once done, you can install the necessary Python packages for running the program: 

```bash
pip install yt_dlp youtube-search-python colorama
```

The last program to install is `ffmpeg`, which converts the downloaded videos to MP3 format.
#### On Windows

The quickest way to install ffmpeg on Windows is to download [`scoop`](https://scoop.sh/): In a PowerShell terminal, enter the following command:

```PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

Then open another PowerShell terminal and enter the following command: 

```PowerShell
scoop install ffmpeg
```
#### On Linux

Open a terminal and enter the following command:

```bash
sudo apt install ffmpeg
```
#### On macOS

The simplest installation is with [HomeBrew](https://brew.sh/). If you do not already have HomeBrew, you can install it with this command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then, install ffmpeg with this command: 

```bash
brew install ffmpeg
```

(Note: macOS compatibility is not fully supported yet.)
### Usage

Once all dependencies are installed, source the virtual environment where you installed the dependencies and run the script.
#### On Windows:

```PowerShell
.\path\to\your\venv\Scripts\Activate
```

Then, run the script with `python3` or `py`:

```
py .\path\to\Magicdownload\folder\magic_download.py
### or
python3 .\path\to\MagicDownload\folder\magic_download.py
```
#### On Linux

Source the virtual environment:

```bash
source path/to/your/venv/bin/activate
```

Then run the script with `python3` :

```bash
python3 path/to/MagicDownload/folder/magic_download.py
```

## How to Use MagicDownload

Once the program is launched, you can use the `help` command to display the available actions. Currently, there are two modes, `dl` and `ply`, which respectively allow you to download a single video or an entire playlist/album.

Regardless of the mode used, the operation is the same. You need to enter one or two arguments: the first is the name of the video/playlist to search for, and the second is the name of the download folder.

You do not have to specify the second argument; if it is not specified, the video will be downloaded into a folder named with today's date in the format `YYYY-MM-DD-music`.

By default, regardless of the operating system, the music download folder is created in your machine's `Music` folder.

**IMPORTANT**: Do not use spaces in the video or download folder names; use underscores `_` instead. Only the two arguments should be separated by spaces.

#### Example:

Suppose you want to download the music **Dire Dire Docks** in a folder named **Video Games Music**. First, you need to access the `VideoDL` mode of MagicDownload. To do this, just type `dl`. Then, enter the following command:

```bash
Dire_Dire_Docks Video_Games_Music
```

This command will search for the music `dire dire docks` and download it in `Music/Video Games Music/` in MP3 format.

**Note**: If the specified download folder already exists, this is not a problem; the music will be downloaded there without overwriting the folder contents.

If you want to switch modes, you can go back by typing `..`.
