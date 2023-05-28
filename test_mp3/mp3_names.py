#this renames mp3 file based on given Titles

from mutagen import File
from mutagen.id3 import ID3, TIT2, TPE1, TALB

import os


# Lists through all files in directory
def list_files(directory):
       
    with open('Names.txt', 'r') as file:
        for filename in os.listdir(directory):
            if filename == "Names.txt":
                continue
            line = file.readline().strip('\n')
            print(line)
            os.rename(filename, line)         
        
list_files('.')