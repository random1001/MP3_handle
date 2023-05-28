#this renames mp3 file based on given Titles

from mutagen import File
from mutagen.id3 import ID3, TIT2, TPE1, TALB

import os


# Lists through all files in directory
def list_files(directory):
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
    except:
        pass
        
        
list_files('.')