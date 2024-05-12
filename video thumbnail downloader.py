import pandas as pd
import pytube
import urllib.request

# Read the Excel file containing the video URLs
# Enter you path of the file
df = pd.read_excel("C:\\Users\\Hp\\Documents\\projects\\python\\youtube thumbnail downloader\\MYURL.xlsx")

def download_thumbnails(df):
    for index, row in df.iterrows():
        url = row['URL']
        try:
            video = pytube.YouTube(url)
            thumbnail_url = video.thumbnail_url
            filename = f"thumbnails/thumbnail_{index+1}.jpg"  
            urllib.request.urlretrieve(thumbnail_url, filename)
            print(f"Thumbnail downloaded for video {index}")
        except Exception as e:
            print(f"Error downloading thumbnail for video {index}: {e}")

# Call the function
download_thumbnails(df)
