#mp3_edit.py
#python mp3_edit.py "Artist" "Album"
#Add Titles.txt and Names.txt for next level of metadata editing

from mutagen import File
from mutagen.id3 import ID3, TIT2, TPE1, TALB

import os
import sys

#Read CMD arguments
args = sys.argv

#Set default metadata to None
Artist = None
Album  = None

#Try get some metadata variables
try:
    Artist = args[1]
except:
    pass
    
try:
    Album  = args[2]
except:
    pass    
    
def change_metadata(file_path, artist=None, album=None, tracknumber=None):
    try:
        audio = File(file_path, easy=True)
        
        if artist:
            audio['artist'] = artist
        if album:
            audio['album'] = album
        if album:
            audio['tracknumber'] = tracknumber
        
        audio.save()
    except Exception as e:
        print("An error occurred:", str(e))
        
# Lists through all files in directory
def list_files(directory, Artist, Album):
    i = 0
    try:    
        with open('Titles.txt', 'r') as file:    
            for filename in os.listdir(directory):
            
                if filename == "Titles.txt":
                    continue
                line = file.readline().strip('\n')    
                file_path = str(filename)
                audio = File(file_path, easy=True)
                
                print(line)
                audio['title'] = line  
                audio.save()
                
                file_path = str(filename)
                i = i + 1
                
                change_metadata(file_path, artist=Artist, album=Album, tracknumber=str(i))            
    except:
        pass
            
        



list_files('.', Artist, Album)
print("Metadata updated successfully.")
#Name Handle
try:
    for filename in os.listdir('.'):

        with open('Names.txt', 'r') as file:
            for filename in os.listdir('.'):
                if filename == "Names.txt":
                    continue
                line = file.readline().strip('\n')
                print(line)
                os.rename(filename, line)
except:
    pass