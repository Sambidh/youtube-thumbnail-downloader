import requests
from bs4 import BeautifulSoup
import re

import pytube
import urllib.request

def get_video_ids(channel_url):
    try:
        # Fetch the HTML content of the channel page
        response = requests.get(channel_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        html_content = response.text

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all video links
        video_links = soup.find_all('a', {'href': re.compile(r'^/watch\?v=')})

        # Extract video IDs from the links
        video_ids = [link['href'].split('=')[-1] for link in video_links]

        return video_ids
    except Exception as e:
        print(f"Error fetching video IDs: {e}")
        return []

def download_all_thumbnails(channel_url):
    video_ids = get_video_ids(channel_url)
    if not video_ids:
        print("No video IDs found.")
        return

    # Download thumbnails for each video
    for i, video_id in enumerate(video_ids, start=1):
        try:
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            video = pytube.YouTube(video_url)
            thumbnail_url = video.thumbnail_url
            urllib.request.urlretrieve(thumbnail_url, f"thumbnails/{i}.jpg")
            print(f"Downloaded thumbnail {i} for video: {video_url}")
        except Exception as e:
            print(f"Error downloading thumbnail {i}: {e}")

# Example usage
channel_url = "https://www.youtube.com/@mattfreire"
download_all_thumbnails(channel_url)
# Example usage
channel_url = "https://www.youtube.com/@mattfreire"
download_all_thumbnails(channel_url)
