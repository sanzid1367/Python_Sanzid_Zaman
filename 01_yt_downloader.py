from pytube import YouTube
import os
from urllib.error import URLError

# Create downloads directory if it doesn't exist
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# Prompt user to enter the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

try:
    # Create a YouTube object
    yt = YouTube(video_url)
except Exception as e:
    print(f"Error: Invalid URL or connection issue - {str(e)}")
    exit(1)

# Display video details
print(f"Title: {yt.title}")
print(f"Author: {yt.author}")
print(f"Duration: {yt.length // 60} minutes {yt.length % 60} seconds")

# List available streams
streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
print("Available video streams:")
for i, stream in enumerate(streams):
    print(f"{i + 1}. {stream.resolution}")

# Ask user to choose a stream
while True:
    try:
        choice = int(input("Enter the number of the stream to download: ")) - 1
        if 0 <= choice < len(streams):
            selected_stream = streams[choice]
            break
        else:
            print(f"Please enter a number between 1 and {len(streams)}")
    except ValueError:
        print("Please enter a valid number")

# Download the video
try:
    print("Downloading...")
    selected_stream.download(output_path="downloads")
    print("Download completed! Check the 'downloads' folder.")
except Exception as e:
    print(f"Error during download: {str(e)}")
