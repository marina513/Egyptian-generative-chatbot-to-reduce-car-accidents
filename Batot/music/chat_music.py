from __future__ import unicode_literals
import re
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
    speak_ar("عَاوِزُ مُوسِيقَى بالانجليزي و لا بالعربي")
    lang = speech2txt()
    lang = translate( lang , 'en').replace('.','').lower()
    print("lang: " , lang)
    
    if( (lang.find("en")!=-1) or (lang.find("ein") != -1) ):
        print("Engls")
        speak_ar("عَاوِزُ اني مُوسِيقَى قُلِّ اِسْمِهَا بالانجليزي")
        music_s = speech2txt_en()
        if(music_s == '0'):
            speak_ar("لَمْ اسْمَعْ  قُلَّ تاني ")
            return 5
        else:
            pass
        music_name = translate( music_s , 'en').replace('.','').lower()
        music_name = lemmatizer.lemmatize(music_name)
        print(music_name)   
        speak_ar("هو الاسم كِدَ صح")
        speak(music_name)

        
    elif(lang.find("ar") != -1):
        speak_ar("عَاوِزُ اني مُوسِيقَى قُلِّ اِسْمِهَا بالعربي")
        music_name = speech2txt().replace(".","")
        if(music_name == '0'):
            speak_ar("لَمْ اسْمَعْ  قُلَّ تاني ")
            return 5
        else:
            pass
        print(music_name)   
 
        speak_ar("هو الاسم كِدَ صح")
        speak_ar(music_name)

    elif(lang.find("bye") != -1):
        speak_ar("باي")
        return
    else:
        speak_ar("لم افهم")
        return 5

    s = speech2txt()
    want = translate( s , 'en').replace('.','').lower()
    want = lemmatizer.lemmatize(want)
    print(want)

    if (  ((want.find('aiwa') != -1) or (want.find('yes') != -1)  or (want.find('ah') != -1) or (want.find('ha') != -1) or (want.find('oh') != -1)  or (want.find('true') != -1) or (want.find('uh') != -1) )  ) :
        #############  LINK   ##############
        videosSearch = VideosSearch(music_name, limit = 2)
        link = videosSearch.result()['result'][0]['link']
        print(link)

        ############  Search database for music  #####
        with open('C:/Users/AnyOneElse/GP_POP/Batot/music/music_links.txt') as f:
            if link in f.read():
                print("FOUND  FOUND FOUND  FOUND  FOUNDFOUND  FOUNDFOUNDFOUND")
                speak_ar("لحظة هتأكد من ايقاعها")
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
      
        paths_play = open("C:/Users/AnyOneElse/GP_POP/Batot/music/paths_play_now_txt.txt", "w")
        paths_play.write(path+ "\n")
        paths_play.close()
       
        print(path)
        path = path.replace('\n','')
        print(path)
        no_again = True
        return path
        

    else:
        print("AGANIN AGAIN MUSIC MSIC ")
        speak_ar("أَسَفِ ممكن نحاول تاني ")
        return 5

