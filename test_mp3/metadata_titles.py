#this sript reads metadata titles from mp3 file and write it to file

from mutagen import File
from mutagen.id3 import ID3, TIT2, TPE1, TALB

import os

def print_titles(file_path):
    try:
        audio = File(file_path, easy=True)       
        print(audio['title'])
    except Exception as e:
        print("An error occurred:", str(e))

# Lists through all files in directory
def list_files(directory):
    i = 0
    for filename in os.listdir(directory):
        if filename == "meta.py":
            continue
            
        file_path = str(filename)
        i = i + 1
        print_titles(file_path)
        
list_files('.')