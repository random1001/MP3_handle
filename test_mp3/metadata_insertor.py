#Metadata insertor
from mutagen import File
from mutagen.id3 import ID3, TIT2, TPE1, TALB

import os

def change_metadata(file_path, title=None, artist=None, album=None, tracknumber=None):
    try:
        audio = File(file_path, easy=True)
        
        if title:
            audio['title'] = title
        if artist:
            audio['artist'] = artist
        if album:
            audio['album'] = album
        if album:
            audio['tracknumber'] = tracknumber
        
        audio.save()
        print("Metadata updated successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

# # Lists through all files in directory
def list_files(directory):
    i = 0
    for filename in os.listdir(directory):
        if filename == "metadata_insertor.py":
            continue
            
        file_path = str(filename)
        i = i + 1
        change_metadata(file_path, title=None, artist="Stephen Fry", album="Harry Potter And The Order of the Phoeniex", tracknumber=str(i))

list_files('.')
