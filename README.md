# YouTube MP3 Converter/Cropper

Want to listen to that good song you found on YouTube? Ever wished you could just crop out the song part of the video and listen to it forever on your phone? You're in the right place.

## Dependencies

`pip install` the following

- `youtube-dl` (Install [here](https://github.com/ytdl-org/youtube-dl#installation))
- `pydub` (Install [here](https://github.com/jiaaro/pydub#installation))
- `simpleaudio` (Install [here](https://simpleaudio.readthedocs.io/en/latest/installation.html))
- `pyaudio`

If you're feeling lazy, just copy & paste the following.

```
sudo -H pip install --upgrade youtube-dl
pip install pydub
pip install simpleaudio
pip install pyaudio
```

## How to use

![](https://media.giphy.com/media/db4aSg19d4aI8RJnuI/giphy.gif)

0. Type `python youtube_mp3.py`

1. Copy the URL of your favorite video.

2. Specify when the song starts and ends.

3. Copy and paste the title (.mp3).

4. Name the file whatever you want.

5. Enjoy the song!

## Add the songs to Spotify!

You can add these MP3 files to your Spotify playlist using Local Files on your Spotify Desktop app. See [here](https://support.spotify.com/us/using_spotify/features/listen-to-local-files/) for more details.

## Future enhancements

So far, there are only 39 lines of Python script. Obviously this is my one-night project, but please contribute and make it better!

- Write a bash script so that you don't have to copy and paste the title every time (or find/create a way to crop the MP3 with only `youtube-dl`).

- Add the songs to your Spotify playlist using Spotify Web API.

- Make this script a web app.

- Develop a Machine Learning model to detect when a song starts and ends in a video.
