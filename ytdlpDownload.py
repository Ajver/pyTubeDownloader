import subprocess

def download_video(link, output_path="out"):
    command = ["yt-dlp", "-o", f"{output_path}/%(title)s.%(ext)s", link]
    subprocess.run(command)

link = "https://youtu.be/qgPc3QtqTIw?si=x6i2gSW4zjx9bgqK"
download_video(link)
