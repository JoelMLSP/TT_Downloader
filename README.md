# TED Talk Video Downloader

## Overview
This project is a **Python script** that downloads TED Talk videos using **web scraping and ffmpeg**. It first tries to download an MP4 file, and if that fails, it extracts the M3U8 playlist and downloads it using ffmpeg.

## Features
- Extracts **MP4 or M3U8** video URLs from TED Talk pages.
- **Downloads videos automatically** and saves them to a folder.
- Uses **ffmpeg** for handling M3U8 streaming files.
- Saves all videos in a `ttdownload` folder on the **Desktop**.

## Prerequisites
- Python 3.x
- **ffmpeg** (must be installed and added to PATH)

## Installation
### **1️⃣ Install Dependencies**
Run the following command to install required Python libraries:
```sh
pip install requests beautifulsoup4 lxml
```

### **2️⃣ Install ffmpeg**
1. Download FFmpeg from **[Gyan.dev](https://www.gyan.dev/ffmpeg/builds/)**.
2. Extract the ZIP and move it to `C:\Program Files\ffmpeg`.
3. Add `C:\Program Files\ffmpeg\bin` to **System PATH**.
4. Test installation by running:
   ```sh
   ffmpeg -version
   ```

![image](https://github.com/user-attachments/assets/65750d0b-7a91-4d4a-a1bf-a573e974ef22)


## Usage
1. Run the script and provide a TED Talk URL:
   ```sh
   python script.py "https://www.ted.com/talks/example"
   ```
2. The script will:
   - Try downloading an **MP4** file.
   - If MP4 fails, it extracts an **M3U8 playlist** and downloads it with ffmpeg.
   - Save the video inside `Desktop/ttdownload/`.

![image](https://github.com/user-attachments/assets/e557241d-ce55-42b6-81e7-55e4f5d3f771)


## Example Output
```sh
Status Code: 200
Your download is about to start
Downloading MP4 file from: https://video.tedcdn.com/video.mp4
Download complete! File saved at: C:\Users\YourName\Desktop\ttdownload\video.mp4
```

![image](https://github.com/user-attachments/assets/0db0cca5-9008-4cd6-84ca-6cf89d1ce9c9)


## Notes
- If you get **Access Denied** on MP4, the script will automatically fall back to M3U8.
- If ffmpeg is missing, **M3U8 downloads will fail**.
- Ensure **ffmpeg is added to PATH** for smooth functionality.

## License
This project is open-source and free to use.

