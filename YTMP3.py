import ssl
from pytube import YouTube

BLUE = "\033[1;34m"
RESET = "\033[0m"

print ("  ")
print(f"{BLUE}By : M1   |   IG : 1e.az{RESET}")

ssl._create_default_https_context = ssl._create_unverified_context

def download_video():
    video_url = input(f"{BLUE}Enter YouTube video URL to download (MP3): {RESET}")
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download()
        print(f"{BLUE}Download completed successfully!{RESET}")
    except Exception as e:
        print(f"{BLUE}Failed to download the video.{RESET}")
        print(f"{BLUE}Error: {RESET}", str(e))

if __name__ == '__main__':
    download_video()