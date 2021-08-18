import sys
sys.path.insert(1 , 'C:/Users/AnyOneElse/GP_POP/Batot/sounds')
from sounds.speak_ import  speak,speak_ar
from sounds.azure_speech import speech2txt
from mtranslate import translate
import simpleaudio as sa
import pyttsx3
converter = pyttsx3.init()
print("DD1")
from mtranslate import translate
print("DD2")
import simpleaudio as sa
print("DD3")
from joke_fn_chat import  joke_fn_main
print("DD4")
from nltk.stem import WordNetLemmatizer
print("DD5")
import sys
sys.path.insert(1 , 'C:/Users/AnyOneElse/GP_POP/Batot/music')
print("DD6")
from music.chat_music import music_path
print("DD7")
from music.music_class import  temp_retrieve 
print("DD8")
from nltk.stem.snowball import SnowballStemmer
print("DD9")
from nltk.corpus import stopwords
print("DD10")
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import import_ipynb
from Generative_Egyptian_Chatbot_Batot_7obo import evaluateInput
from sleep_check import sleep_read,sleep_alaram
###############################################################################
###############################################################################
stemmer = SnowballStemmer("english")
stop_words = set(stopwords.words('english'))
stop_words_list = list(stop_words)
stop_words_list.extend(["!" , "?", "'s", "," , ".", "'m","want" , '.'])
lemmatizer = WordNetLemmatizer()

speak("Importing Done")
speak("model loaded")

##################################################################################################################
##################################################################################################################
def Main_Chat(msg, first_time):
    # choose
    if (first_time):
        speak_ar("تسمع موسيقى أم نكتة أم تتكلم معايا")
    else:
        speak_ar("عاوز حاجة تاني")
    
    s = speech2txt()
    print(s)
    if(s == '0'):
        speak_ar("لم أسمع")
        Main_Chat("",True)
    else:
        pass

    want = translate( s , 'en').replace('.','').lower()
    want = lemmatizer.lemmatize(want)

    print("want translated: ", want)
    #######################################################################
    #######################################################################
    # music
    if ( (want.find('music')) != -1): 
        print("Music enter")
        work = music_path()
        while(work == 5):
            print("55555555555555555555555555555555555555555555555555555555555")
            work = music_path()

        print("music return")
        filename_music = open("C:/Users/AnyOneElse/GP_POP/Batot/music/paths_play_now_txt.txt", "r")
        filename = filename_music.readlines()[0].replace("\n", "")
        try:
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            print("file music name: ")
            print(filename)
            t = temp_retrieve(filename).replace("\n","")
            print(t)
            if(int(t) < 120 ):    
                speak_ar("مضبوط اتمنى تستمتع")
                wave_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wave_obj.play()
                #####################
                command = ""
                print("***********************************************************************************")
                while ((command.find("stood up") == -1) and (command.find("stop") == -1)  and (command.find("only") == -1) and (sleep_read() == False) and (command.find("shut") == -1)):
                    print("Music still playing")
                    s = speech2txt()
                    command = translate(s, 'en').replace('.','').lower()
                    command = lemmatizer.lemmatize(command)
                    print(command)
                play_obj.stop()
            elif(int(t) >= 100 ): speak_ar(" عزرا ايقاع الموسيقى مرتفع و يمكن يؤثر على سواقتك اختر حاجه تاني")
        except:
            speak_ar("عزرا ممكن نعيد مرة اخري")
    ######################################################################
    # joke 
    elif ( (want.find('point') != -1) or (want.find('joke') != -1)  ): # tested
        print("joke enter")
        speak_ar("تَعَالَى اقْلكَ نُكْتَةَ حلْوَةَ")
        joke_fn_main(False)

    ######################################################################
    ######################################################################
    #speak 
    elif ( (want.find('speak') != -1) or (want.find('talk') != -1) ): 
        print("speak enter")
        speak_ar("عاوز تتكلم عن اية")
        evaluateInput()

    elif ( want.find( "no") != -1 ): # tested tested
        print("no enter")
        speak_ar("مع السلامه سوق براحه")
        return 0
    elif(sleep_read()):
        return

    elif ( ((want.find('no') == -1) and (want.find('speak') == -1) and (want.find('talk') == -1) and  (want.find('music') == -1))
     and (want.find('point') == -1) and (want.find('joke') == -1)  ):
        print("nothing enter")
        speak_ar("من فضلك")
        Main_Chat("", True)


######################################################################
#######################################################################
speak_ar("ابدأ")
    
x = 0
r = 5
neg_classes = ['angry', 'sad','fear', 'disgust','hide']
said = False

while(x < 1000):  
    file_start = open("C:/Users/AnyOneElse/GP_POP/cam_emotion_detect/mix_mood.txt")
    starts = file_start.readlines()
    file_start.close()

    start = starts[len(starts) - 1].replace("\n","")
    print(start)

    if((start in neg_classes) or (sleep_read()== True)):
        print("x : ",x, "  ,  r : " , r)  
        if(sleep_read()):
            speak_ar("تم وقف سيستم الشات بوت لنومك اثناء القيادة")
            sleep_alaram()
            if (r == 0) :
                break
            break
        if( (r == 0)  ):
            print("end")
            break

        if(x==0):
            r = Main_Chat("inp", True)

        elif(x > 0):
            r = Main_Chat("inp", False)

        if( (r == 0)  ):
            print("end")
            break
        x = x + 1

    elif(said == False):
        speak_ar("حفاظا على سلامتك الشات بوت يشتغل فى حاله الحزن فقط")
        said = True