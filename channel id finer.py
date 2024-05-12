from pytube import YouTube
from pytube import Channel

video = input("Enter the youtube video URL: ")

x = YouTube(video)
Cid = x.channel_id
Curl = x.channel_url

c = Channel(Curl)
Cname = c.channel_name

print("\n")
print("Channel Name: ", Cname)
print("Channel ID: ", Cid)
print("Channel URL: ", Curl)