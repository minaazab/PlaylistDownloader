import requests
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL
from ddgs import DDGS

# prompts the user to enter necessary details for the program to work
folder = input("Give me what the folder name should be: ")

print("In order to download mp3 files, make sure to have ffmpeg.exe and ffprobe.exe downloaded. Otherwise, the songs will download as webm files. If you don't care about this, simply write anything for the next input.")
ffmpegLocation = input("Give me the directory that ffmpeg and ffprobe is located: ")

url = input("Give me the url of the Spotify song you would like to download: ")

# gets specific song information
r = requests.get(url)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")
sname = soup.find("title").get_text()

song, rest = sname.split("-", 1)
middle, part3 = rest.split("by", 1)
author, trash = part3.split("|", 1)


# searches for the song
with DDGS() as ddgs:
    result = ddgs.videos(song + " by " + author + " youtube", max_results=1)

# parses the song
song_url = result[0]["content"]
print("Downloading " + song_url + " " + result[0]["title"])


# downloads the song to the specific folder the user targets
ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": f"{folder}/{author} - %(title)s.%(ext)s",
    "ffmpeg_location": r"ffmpegLocation",

    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
    "ignoreerrors": True,
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([song_url])


