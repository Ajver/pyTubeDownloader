import time
import sys

from pytube import YouTube, Stream
from pytube.exceptions import RegexMatchError

if len(sys.argv) > 1:
    link = sys.argv[1]
else:
    print("Auto setting link...")
    link = "https://youtu.be/dCNTQmbqFSs?si=bATSRVvXJQwCZHW2"


def on_download_progress(stream: Stream, _chunk: bytes, bytes_remaining: int):
    downloaded = stream.filesize - bytes_remaining
    percentage_done = downloaded * 100.0 / stream.filesize
    print(f"{percentage_done:5.1f} %")


yt = YouTube(link, on_progress_callback=on_download_progress)

print("Link: ", link)
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length, "seconds")
print("Description: ", yt.description)
print("Ratings: ", yt.rating)

print("All streams:\n", yt.streams)

try:
    audio_streams = yt.streams.filter(only_audio=True)
    print(f"Audio streams only: ({len(audio_streams)} found)\n", "\n".join(str(stream) for stream in audio_streams))
except RegexMatchError:
    print("An error occurred. Please try again.")
    sys.exit(0)

stream = audio_streams.get_audio_only()
print("Stream with the best audio\n", stream)


def get_yn_input(message) -> bool:
    while True:
        decision = input(message + " [y/n]: ")

        if decision.lower()[0] == "y":
            return True

        if decision.lower()[0] == "n":
            return False


if stream is not None and get_yn_input("Download?"):
    start = time.time()
    print("Downloading...")
    saved_path = stream.download("out")
    duration = time.time() - start
    print(f"Video downloaded within {duration} seconds. Saved to:\n{saved_path}")
else:
    print("Exit without downloading...")
