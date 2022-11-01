from distutils.log import error
from multiprocessing.sharedctypes import Value
import os
from pathlib import Path
from turtle import down
from pydantic import validate_email
from youtubesearchpython import ChannelsSearch
from pytube import YouTube, Playlist, Channel, Search, exceptions

from version1 import channelLink, channelSearch, searchLink, singleLink

# It will fetch the local path of "Download" for saving the downloads
local_download_path = str(Path.home()/"Downloads")

fuchsia = '\033[38;2;255;00;255m'  # color as hex #FF00FF
reset_color = '\033[39m'

#common function of errorHandling for checking the valid or required inputs from the user
def errorHandling(param1, param2):
    while True:
        try:
            valid_inp = int(input("\nOut of this which option would you like to choose ? : "))
            if valid_inp >= param1 and valid_inp <= param2:
                return valid_inp
        except ValueError:
            print("Error! Enter an integer value!! You fkin' dump asshole🤬")
        except KeyboardInterrupt:
            print("OOPs feelin' like very strong keyboard stroke⌨️")

def singleLink_download_option(answer,link):
    match answer:
        case 1:
            try:
                yt = YouTube(link)
            except exceptions.VideoUnavailable:
                print(f'Video {link} is unavaialable, skipping.')
            except KeyboardInterrupt:
                print("OOPs feelin' like very strong keyboard stroke⌨️")
            else:
                print(yt.title)
        case 2:
            try:
                yt = YouTube(link)
            except exceptions.VideoUnavailable:
                print(f'Video {link} is unavaialable, skipping.')
            except KeyboardInterrupt:
                print("OOPs feelin' like very strong keyboard stroke⌨️")
            else:
                print(f'\n' + fuchsia + 'Downloading: ',
                      yt.title, '~ viewed', yt.views, 'times.')
                yt.streams.filter(
                    file_extension='mp4').get_highest_resolution().download(local_download_path)
                print(f'\nFinished downloading:  {yt.title}' + reset_color)
        case 3:
            try:
                yt = YouTube(link)
            except exceptions.VideoUnavailable:
                print(f'Video {link} is unavaialable, skipping.')
            except KeyboardInterrupt:
                print("OOPs feelin' like very strong keyboard stroke⌨️")
            else:
                print(f'\n' + fuchsia + 'Downloading: ',
                      yt.title, '~ viewed', yt.views, 'times.')
            yt.streams.filter(
                file_extension='mp4').get_lowest_resolution().download(local_download_path)
            print(f'\nFinished downloading:  {yt.title}' + reset_color)
        case 4:
            try:
                yt = YouTube(link)
            except exceptions.VideoUnavailable:
                print(f'Video {link} is unavaialable, skipping.')
            except KeyboardInterrupt:
                print("OOPs feelin' like very strong keyboard stroke⌨️")
            else:
                print(f'\n' + fuchsia + 'Downloading: ',
                      yt.title, '~ viewed', yt.views, 'times.')
            out_file = yt.streams.filter(only_audio=True).first().download(local_download_path)
            print(f'\nFinished downloading:  {yt.title}' + reset_color)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

def multiLink_download_options(answer,link):
    match answer:
        case 1:
            print(playlist_url.title)
            for video in playlist_url.videos:
                print(f'Title : {video.title}')
            for url in playlist_url.video_urls:
                print(url)
        case 2:
            for url in playlist_url.video_urls:
                try:
                    yt = YouTube(url)
                except exceptions.VideoUnavailable:
                    print(f'Video {url} is unavaialable, skipping.')
                except KeyboardInterrupt:
                    print("OOPs feelin' like very strong keyboard stroke⌨️")
                else:
                    print(f'\n' + fuchsia + 'Downloading: ',
                          yt.title, '~ viewed', yt.views, 'times.')
                    yt.streams.filter(
                        file_extension='mp4').get_highest_resolution().download(local_download_path)
                    print(f'\nFinished downloading:  {yt.title}' + reset_color)
        case 3:
            for url in playlist_url.video_urls:
                try:
                    yt = YouTube(url)
                except exceptions.VideoUnavailable:
                    print(f'Video {url} is unavaialable, skipping.')
                except KeyboardInterrupt:
                    print("OOPs feelin' like very strong keyboard stroke⌨️")
                else:
                    print(f'\n' + fuchsia + 'Downloading: ',
                          yt.title, '~ viewed', yt.views, 'times.')
                yt.streams.filter(
                    file_extension='mp4').get_lowest_resolution().download(local_download_path)
                print(f'\nFinished downloading:  {yt.title}' + reset_color)
        case 4:
            for url in playlist_url.video_urls:
                try:
                    yt = YouTube(url)
                except exceptions.VideoUnavailable:
                    print(f'Video {url} is unavaialable, skipping.')
                except KeyboardInterrupt:
                    print("OOPs feelin' like very strong keyboard stroke⌨️")
                else:
                    print(f'\n' + fuchsia + 'Downloading: ',
                          yt.title, '~ viewed', yt.views, 'times.')
                out_file = yt.streams.filter(
                    only_audio=True).first().download(local_download_path)
                print(f'\nFinished downloading:  {yt.title}' + reset_color)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)

def singleLink():
    link = input("Enter link of video : ")
    print("Enter 1 to see the title of video \n", "Enter 2 to download all videos at high resolution ⚡\n",
          "Enter 3 to download all videos in low resolution 🐽\n", "Enter 4 to download audio 🎶\n")
    response = errorHandling(1, 4)
    singleLink_download_option(response,link)

def searchLink():
    search_result = Search(input("Enter your search : "))
    print(f'Search complete \n')
    videoId = search_result.results[0].video_id
    print("\nEnter 1 to see the title of video \n", "Enter 2 to download all videos at high resolution ⚡\n",
          "Enter 3 to download all videos in low resolution 🐽\n", "Enter 4 to download audio 🎶\n")
    response = errorHandling(1, 4)
    singleLink_download_option(response,"https://youtu.be/"+videoId)

def playlist():
    url = input("Enter URL of Playlist : ")
    playlist_url = Playlist(url)
    print("\nEnter 1 to see the titles of playlist and videos of it 📽️\n", "Enter 2 to download all videos at high resolution ⚡\n",
          "Enter 3 to download all videos in low resolution 🐽\n", "Enter 4 to download just audio of whole playlist 😁")
    answer = errorHandling(1, 4)
    

def channelLink():
    print("running good")

def channelSearch():
    print("running good")

#main function
if __name__ == '__main__':
    print("\nChoose an option from below 👇👇\n","Enter 1 to download a single video or music 😂\n","Enter 2 to download a whole playlist 🥲\n","Enter 3 to download all videos from channel 😑")

    valid_inp_main = 0
#another local error handling for input validation
    while True:
        try:
            valid_inp_main = int(input("\nOut of this which option would you like to choose ? : "))
            if valid_inp_main >= 1 and valid_inp_main <= 3:
                break
            else:
                print("Enter in range of [1,2]")
        except ValueError:
            print("Error! Enter an integer")

#switch cases as per response
    match valid_inp_main:

#It will call single video download from link and search function both as per user input at that moment
        case 1:
            print("\nAgain now choose an option 😤\n",
              "Enter 1 to download via Link 😀\n", "Enter 2 to download via Search 🔎 ")
            response = errorHandling(1,2)
            singleLink() if response==1 else searchLink()

#It will call whole playlist video downlaod function
        case 2:
            playlist()

#It will call channelsearch function
        case 3:
            print("\nAgain now choose an option 😤\n",
              "Enter 1 to give channel link 👍\n", "Enter 2 to search by name 🔎 ")
            response = errorHandling(1, 2)
            channelLink() if response==1 else channelSearch()