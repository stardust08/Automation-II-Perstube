from cgi import print_environ
from pytube import YouTube,Playlist,Channel,Search
from pytube.cli import on_progress
import os
import sys
from operator import index

def playlist():
    url = input("Enter URL of Playlist : ")
    pl = Playlist(url)
    print("\nEnter 1 to see the titles of playlist and videos of it 📽️\n","Enter 2 to download all videos at high resolution ⚡\n","Enter 3 to download all videos in low resolution 🐽")
    errorHandling(1,3)
    print(pl.title)
    for video in pl.videos:
        print(f'Title : {video.title}')
    for url in pl.video_urls:
        print(url)

def errorHandling(param1,param2):
    while True:
        try:
            question1 = int(input("\nOut of this which option would you like to choose ? : "))
            if question1>=param1 and question1<=param2:
                break
            else:
                print(f'Enter in range of [{param1,param2}]')
        except ValueError:
            print("Error! Enter an integer")


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
        errorHandling(1,2)
    if question==2:
        playlist()
    elif question==3:
        print("\nAgain now choose an option 😤\n","Enter 1 to give channel link 👍\n","Enter 2 to search by name 🔎 ")
        errorHandling(1,2)