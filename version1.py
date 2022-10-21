from cgi import print_environ
from pytube import YouTube,Playlist,Channel,Search
from pytube.cli import on_progress
import os
import sys
from operator import index


if __name__ == '__main__':
    print("Choose an option from below : \n")
    print("Enter 1 to download a single video or music : \n")
    print("Enter 2 to download a whole playlist : \n")
    print("Enter 3 to download all videos from channel: \n")
    question = 0
    while True:
        try:
            question = int(input("Out of this which option would you like to choose ? : "))
            if question>=1 and question<=3:
                break
            else:
                print("Enter in range of [1,2]")
        except ValueError:
            print("Error! Enter an integer")

    if question==1:
        print("Again now choose an option : \n")
        print("skfj")
    else:
        print("ofjf")