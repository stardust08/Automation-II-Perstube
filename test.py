from cmath import nan
from operator import index
from tkinter.ttk import Progressbar
from turtle import width
from pytube import YouTube,Playlist,Channel
import pprint
from pytube import Search
from pytube.cli import on_progress
import os
import sys
from youtubesearchpython import ChannelsSearch
from bs4 import BeautifulSoup
import datetime as dt
# yt = YouTube("https://youtu.be/pJZ9tT8OwFk")
# p = Playlist("https://youtube.com/playlist?list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2")
# p.download()
# print(yt.title)
# print(yt.thumbnail_url)
# print(yt.age_restricted)
# print(yt.author)
# print(yt.length)
# print(str(yt.description))
# print(yt.streams)

fuchsia = '\033[38;2;255;00;255m'   #  color as hex #FF00FF
reset_color = '\033[39m'

# s = Search(input("Enter your search : "))
# print(s.results[0])
# videoID = s.results[0].video_id
# print(s.results[0].video_id)
# print(s.get_next_results())


# yt1 = YouTube("https://youtu.be/"+videoID,on_progress_callback=on_progress)
# yt1 = YouTube("https://youtu.be/"+videoID,on_progress_callback = on_progress)
# print(yt1.title)
# yt1.streams.filter(only_audio=True).first().download()
# print(yt1.streams)
# print(yt1.captions)
# yt1.streams.filter(file_extension='mp4').get_highest_resolution().download()
# print(f'\n' + fuchsia + 'Downloading: ',yt1.title, '~ viewed', yt1.views, 'times.')
# yt1.streams.filter(file_extension='mp4').get_lowest_resolution().download()
# out_file = yt1.streams.filter(only_audio=True).first().download()
# print(f'\nFinished downloading:  {yt1.title}' + reset_color)
# base, ext = os.path.splitext(out_file)
# new_file = base + '.mp3'
# os.rename(out_file, new_file)




# s = input("Enter playlist link : ")
# p = Playlist(s)

# print(f'Donwloading : ${p.title}')

# for video in p.videos:
#     print(f'Title : ${video.title}')
#     print(f'URL : ${video.video_urls}')



# i = input("Enter channel name : ")
c = Channel(f'https://www.youtube.com/c/neetcode')
# c = Channel(i)
# print(f'Downloading videos by: {c.channel_name}')
c1 = c.channel_url
c2 = Channel(c1)
# print(c.channel_url)
for video_link in c2.video_urls:
    print(video_link)
#     yt = YouTube(video)
#     print(f'\n' + fuchsia + 'Downloading: ',yt.title, '~ viewed', yt.views, 'times.')
#     out_file = yt.streams.filter(only_audio=True).first().download()
#     print(f'\nFinished downloading:  {yt.title}' + reset_color)
#     base, ext = os.path.splitext(out_file)
#     new_file = base+ '.mp3'
#     os.rename(out_file, new_file)


# channelSearch = ChannelsSearch(i,limit=2)
# ans = channelSearch.result()
# pprint.pprint(dict(ans),width=2)

# print ("\nnext line\n")
# # pprint.pprint(dict(ans['result'][0]),width=1)
# print(ans['result'][0]['link'])


# project finished. Feels so..

# yt = YouTube('https://www.youtube.com/watch?v=aV9gfuUhegE')
# # print(yt.)
# # caption = yt.captions['a.en']

# # print(caption.xml_captions)
# # from pytube import YouTube

# url = "https://www.youtube.com/watch?v=aV9gfuUhegE"

# yt = YouTube(url)
# caption = yt.captions.get_by_language_code('en')
# print(caption.xml_captions)


# yt = YouTube('https://youtu.be/aV9gfuUhegE')
# caption = "Sorry didn't have any caption in this video"
# # print(caption)
# result = ['en','en-GB','a.en']
# result_cnt = 0
# checker = True
# while checker:
#     try:
#         caption = yt.captions[result[result_cnt]]
#         checker = False
#     except:
#         # print("Sorry didn't have any caption")
#         if result_cnt<2:
#             result_cnt+=1
#         else:
#             checker = False

# # print(caption['en']||caption['en-GB'])
# #to this selection view go run terminal help file edit

# print(caption)
# # print(a)