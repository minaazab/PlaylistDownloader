from yt_dlp import YoutubeDL


# prompts user for relavent content
playlist_url = "Give me the url of the YouTube playlist you would like to download: "

playliststart = "Give me the song you would like to start downloading from (number position): "
playlistend = "Give me the song you would like to end downloading at (number position): "

print("In order to download mp3 files, make sure to have ffmpeg.exe and ffprobe.exe downloaded. Otherwise, the songs will download as webm files. If you don't care about this, simply write anything for the next input.")
ffmpegLocation = input("Give me the directory that ffmpeg and ffprobe is located: ")

# starts the download
ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "%(playlist_title)s/%(playlist_index)02d - %(title)s.%(ext)s",
    "ffmpeg_location": r"fmpegLocation",

    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
    "ignoreerrors": True,
    "playliststart": playliststart,
    "playlistend": playlistend,
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])