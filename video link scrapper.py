import scrapetube
import pandas as pd
from openpyxl.workbook import Workbook

channelid = input("Enter the Youtube channel ID: ")

list = []

url = "https://www.youtube.com/watch?v="

dataframe = pd.DataFrame(columns =  ["URL"])

videos = scrapetube.get_channel(channelid)

for video in videos:
    url1 = url + str(video['videoId'])
    print(url1)
    list.append(url1)

dataframe['URL'] = list

outputfile="MYURL.xlsx"
dataframe.to_excel(outputfile)
print("Task completed successfully")