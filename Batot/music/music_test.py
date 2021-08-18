from __future__ import unicode_literals
import youtube_dl
from mtranslate import translate
import sys
sys.path.insert(1 , 'C:/Users/AnyOneElse/GP_POP/Batot/sounds')
from sounds.speak_ import  speak,speak_ar
from sounds.azure_speech import speech2txt,speech2txt_en
import glob
import os
from youtubesearchpython import  VideosSearch
from nltk.stem import WordNetLemmatizer
from music_class import tempo


ydl_opts = {'postprocessors': [{'key': 'FFmpegExtractAudio',
                                        'preferredcodec': 'wav',
                                        'preferredquality': '192'}]}

lemmatizer = WordNetLemmatizer()


###############################################################################


def music_path():
    #############  Ask user   ##############
    music_name = "it is ok2"
    
    #############  LINK   ##############
    videosSearch = VideosSearch(music_name, limit = 2)
    link = videosSearch.result()['result'][0]['link']
    print(link)

    ############  Search database for music  #####
    with open('C:/Users/AnyOneElse/GP_POP/Batot/music/music_links.txt') as f:
        if link in f.read():
            print("FOUND  FOUND FOUND  FOUND  FOUNDFOUND  FOUNDFOUNDFOUND")
            ############  Search database for music link  #####
            line_number = 0
            with open('C:/Users/AnyOneElse/GP_POP/Batot/music/music_links.txt','r') as f:
                for line in f:
                    line_number += 1
                    if(link in line):
                        ############  Search database for music path  #####
                        line_number_path = 0
                        path = ""
                        with open('C:/Users/AnyOneElse/GP_POP/Batot/music/music_paths.txt','r') as f:
                            for line in f:
                                line_number_path += 1
                                if(line_number_path == line_number):
                                    path = line
                                    print("sssssssssseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                                    print(path)
                                    break
                        
        else:
            speak_ar("مَلقتهاش ثواني هحملها")
            #############  Download   ##############
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

            #############  add link   ##############
            File_object = open(r"C:/Users/AnyOneElse/GP_POP/Batot/music/music_links.txt",'a')
            File_object.write('"' + link + '"' + "\n")
            File_object.close()
            
            #############  add path   ##############
            list_of_files = glob.glob('C:/Users/AnyOneElse/GP_POP/Batot/*.wav',) # * means all if need specific format then *.csv
            latest_file = max(list_of_files, key=os.path.getctime)
            #music_name
            try:
                os.rename(latest_file,music_name+".wav")
            except:
                pass

            File_object = open(r"C:/Users/AnyOneElse/GP_POP/Batot/music/music_paths.txt",'a')
            File_object.write( music_name+".wav" + "\n")
            File_object.close()
            path = latest_file

            
            print("temp calculation")
            #############  search tempo   ##############
            path = music_name+".wav"
            print("1: ",path)
            t = tempo(path)
            t = str(int(t))
            File_object = open(r"C:/Users/AnyOneElse/GP_POP/Batot/music/tempos.txt",'a')
            File_object.write( t + "\n")
            File_object.close()
            

    ############  play music  #####
    print("PLAYPLAYPLAYPLAYPLAYPLAYPLAYPLAYPLAY")
    print(path)
    path = path.replace('\n','')
    print(path)
    return path

