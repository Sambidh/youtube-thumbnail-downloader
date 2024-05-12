import pytube
import urllib.request

def download_thumbnail(url):
    video = pytube.YouTube(url)
    thumbnail_url = video.thumbnail_url
    urllib.request.urlretrieve(thumbnail_url, "thumbnails/download.jpg")

download_thumbnail("https://www.youtube.com/watch?v=QHaKaeb7vfI")