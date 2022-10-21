from cgi import print_environ
from pytube import YouTube,Playlist,Channel,Search
from pytube.cli import on_progress
import os
import sys
from operator import index


if __name__ == '__main__':
    print("Choose an option from below 👇👇")
    print("Enter 1 to download a single video or music 😂")
    print("Enter 2 to download a whole playlist 🥲")
    print("Enter 3 to download all videos from channel 😑")
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
        print("\nAgain now choose an option 😤")
        print("Enter 1 to download via Link 😀")
        print("Enter 2 to download via Search 🧐 ")
    elif question==3:
        print("Enter 1 to give channel link 👍")
        print("Enter 2 to search by name 🔎 ")