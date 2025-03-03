import requests
from bs4 import BeautifulSoup
import re
import sys
import os
import subprocess

url = None

if len(sys.argv) > 1:
    url = sys.argv[1]
elif not url:
    url = input("Enter the TED Talk URL: ")
    if not url:
        sys.exit("Error: Please provide a valid URL")

r = requests.get(url)
print("Status Code:", r.status_code, "\nYour download is about to start")

soup = BeautifulSoup(r.content, 'lxml')
result = None

for val in soup.find_all('script'):
    if re.search("__NEXT_DATA__", str(val)):
        result = str(val)
        break

if not result:
    sys.exit("Error: Could not find video data.")

# Extract M3U8 URL
result_m3u8 = re.search(r'"(https?://[^\"]+\.m3u8.*?)"', result)
if result_m3u8:
    m3u8_url = result_m3u8.group(1)
    print(f"Found M3U8 Playlist: {m3u8_url}")

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    download_folder = os.path.join(desktop_path, "ttdownload")
    os.makedirs(download_folder, exist_ok=True)

    output_file = os.path.join(download_folder, "ted_talk.mp4")

    print("Downloading video using ffmpeg...")
    subprocess.run(["ffmpeg", "-i", m3u8_url, "-c", "copy", output_file])

    print(f"Download complete! File saved at: {output_file}")
    sys.exit()

# Extract MP4 URL if no M3U8 is found
result_mp4 = re.search(r'"(https?://[^\"]+\.mp4.*?)"', result)
if result_mp4:
    mp4_url = result_mp4.group(1)
    print("Downloading MP4 file from:", mp4_url)
else:
    sys.exit("Error: No valid MP4 or M3U8 URL found.")

file_name = mp4_url.split("/")[-1].split("?")[0]

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
download_folder = os.path.join(desktop_path, "ttdownload")
os.makedirs(download_folder, exist_ok=True)

file_path = os.path.join(download_folder, file_name)

headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(mp4_url, headers=headers, stream=True)

with open(file_path, "wb") as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

print(f"Download complete! File saved at: {file_path}")
