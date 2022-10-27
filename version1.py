from cgi import print_environ
from pytube import YouTube,Playlist,Channel,Search,exceptions
from pytube.cli import on_progress
import os
import sys
from operator import index

fuchsia = '\033[38;2;255;00;255m'   #  color as hex #FF00FF
reset_color = '\033[39m'

def playlist():
    url = input("Enter URL of Playlist : ")
    pl = Playlist(url)
    print("\nEnter 1 to see the titles of playlist and videos of it 📽️\n","Enter 2 to download all videos at high resolution ⚡\n","Enter 3 to download all videos in low resolution 🐽\n","Enter 4 to download just audio of whole playlist 😁")
    answer = errorHandling(1,4)
    match answer:
        case 1:
            print(pl.title)
            for video in pl.videos:
                print(f'Title : {video.title}')
            for url in pl.video_urls:
                print(url)
        case 2:
         for url in pl.video_urls:
            try:
                yt = YouTube(url)
            except exceptions.VideoUnavailable:
                print(f'Video {url} is unavaialable, skipping.')
            else:
                print(f'\n' + fuchsia + 'Downloading: ',yt.title, '~ viewed', yt.views, 'times.')
                yt.streams.filter(file_extension='mp4').get_highest_resolution().download()
                print(f'\nFinished downloading:  {yt.title}' + reset_color)
        case 3:
         for url in pl.video_urls:
            try:
                yt = YouTube(url)
            except exceptions.VideoUnavailable:
                print(f'Video {url} is unavaialable, skipping.')
            else:
                print(f'\n' + fuchsia + 'Downloading: ',yt.title, '~ viewed', yt.views, 'times.')
            yt.streams.filter(file_extension='mp4').get_lowest_resolution().download()
            print(f'\nFinished downloading:  {yt.title}' + reset_color)
        case 4:
         for url in pl.video_urls:
            try:
                yt = YouTube(url)
            except exceptions.VideoUnavailable:
                print(f'Video {url} is unavaialable, skipping.')
            else:
                print(f'\n' + fuchsia + 'Downloading: ',yt.title, '~ viewed', yt.views, 'times.')
            out_file = yt.streams.filter(only_audio=True).first().download()
            print(f'\nFinished downloading:  {yt.title}' + reset_color)
            base, ext = os.path.splitext(out_file)
            new_file = base+ '.mp3'
            os.rename(out_file, new_file)


def singleLink():
    link = input("Enter link of video : ")
    print("Enter 1 to see the title of video \n","Enter 2 to download all videos at high resolution ⚡\n","Enter 3 to download all videos in low resolution 🐽\n","Enter 4 to download audio 🎶\n")
    answer = errorHandling(1,4)
    match answer:
        case 1:
            try:
                yt = YouTube(link)
            except exceptions.VideoUnavailable:
                print(f'Video {link} is unavaialable, skipping.')
            else:
                print(yt.title)
        case 2:
            try:
                yt = YouTube(link)
            except exceptions.VideoUnavailable:
                print(f'Video {link} is unavaialable, skipping.')
            else:
                print(f'\n' + fuchsia + 'Downloading: ',yt.title, '~ viewed', yt.views, 'times.')
                yt.streams.filter(file_extension='mp4').get_highest_resolution().download()
                print(f'\nFinished downloading:  {yt.title}' + reset_color)
        case 3:
            try:
                yt = YouTube(link)
            except exceptions.VideoUnavailable:
                print(f'Video {link} is unavaialable, skipping.')
            else:
                print(f'\n' + fuchsia + 'Downloading: ',yt.title, '~ viewed', yt.views, 'times.')
            yt.streams.filter(file_extension='mp4').get_lowest_resolution().download()
            print(f'\nFinished downloading:  {yt.title}' + reset_color)
        case 4:
            try:
                yt = YouTube(link)
            except exceptions.VideoUnavailable:
                print(f'Video {link} is unavaialable, skipping.')
            else:
                print(f'\n' + fuchsia + 'Downloading: ',yt.title, '~ viewed', yt.views, 'times.')
            out_file = yt.streams.filter(only_audio=True).first().download()
            print(f'\nFinished downloading:  {yt.title}' + reset_color)
            base, ext = os.path.splitext(out_file)
            new_file = base+ '.mp3'
            os.rename(out_file, new_file)



def searchLink():
    result = Search(input("Enter your search : "))
    print(f'Search complete \n')
    videoId = result.results[0].video_id
    print("\nEnter 1 to see the title of video \n","Enter 2 to download all videos at high resolution ⚡\n","Enter 3 to download all videos in low resolution 🐽\n","Enter 4 to download audio 🎶\n")
    answer = errorHandling(1,4)
    match answer:
        case 1:
            try:
                yt = YouTube("https://youtu.be/"+videoId)
            except exceptions.VideoUnavailable:
                print(f'Video {yt} is unavaialable, skipping.')
            else:
                print(yt.title)
        case 2:
            try:
                yt = YouTube("https://youtu.be/"+videoId)
            except exceptions.VideoUnavailable:
                print(f'Video {yt} is unavaialable, skipping.')
            else:
                print(f'\n' + fuchsia + 'Downloading: ',yt.title, '~ viewed', yt.views, 'times.')
                yt.streams.filter(file_extension='mp4').get_highest_resolution().download()
                print(f'\nFinished downloading:  {yt.title}' + reset_color)
        case 3:
            try:
                yt = YouTube("https://youtu.be/"+videoId)
            except exceptions.VideoUnavailable:
                print(f'Video {yt} is unavaialable, skipping.')
            else:
                print(f'\n' + fuchsia + 'Downloading: ',yt.title, '~ viewed', yt.views, 'times.')
            yt.streams.filter(file_extension='mp4').get_lowest_resolution().download()
            print(f'\nFinished downloading:  {yt.title}' + reset_color)
        case 4:
            try:
                yt = YouTube("https://youtu.be/"+videoId)
            except exceptions.VideoUnavailable:
                print(f'Video {yt} is unavaialable, skipping.')
            else:
                print(f'\n' + fuchsia + 'Downloading: ',yt.title, '~ viewed', yt.views, 'times.')
            out_file = yt.streams.filter(only_audio=True).first().download()
            print(f'\nFinished downloading:  {yt.title}' + reset_color)
            base, ext = os.path.splitext(out_file)
            new_file = base+ '.mp3'
            os.rename(out_file, new_file)

def errorHandling(param1,param2):
    while True:
        try:
            question1 = int(input("\nOut of this which option would you like to choose ? : "))
            if question1>=param1 and question1<=param2:
                return question1
            else:
                print(f'Enter in range of [{param1,param2}]')
        except ValueError:
            print("Error! Enter an integer value!! You fkin' dumb asshole🤬")


if __name__ == '__main__':
    print("Choose an option from below 👇👇\n","Enter 1 to download a single video or music 😂\n","Enter 2 to download a whole playlist 🥲\n","Enter 3 to download all videos from channel 😑")
    question = 0
    while True:
        try:
            question = int(input("\nOut of this which option would you like to choose ? : "))
            if question>=1 and question<=3:
                break
            else:
                print("Enter in range of [1,2]")
        except ValueError:
            print("Error! Enter an integer")

    if question==1:
        print("\nAgain now choose an option 😤\n","Enter 1 to download via Link 😀\n","Enter 2 to download via Search 🔎 ")
        answer = errorHandling(1,2)
        if answer==1:
            singleLink()
        else:
            searchLink()
    if question==2:
        playlist()
    elif question==3:
        print("\nAgain now choose an option 😤\n","Enter 1 to give channel link 👍\n","Enter 2 to search by name 🔎 ")
        errorHandling(1,2)