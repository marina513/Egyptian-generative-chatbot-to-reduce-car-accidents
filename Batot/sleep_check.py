from sounds.azure_speech import speech2txt
import sys
sys.path.insert(1 , 'D:/GP/sounds')
from sounds.speak_ import  speak,speak_ar,play
from mtranslate import translate

def sleep_read():
    print("sleep check")
    file = open("C:/Users/AnyOneElse/GP_POP/cam_emotion_detect/sleep.txt", "r")
    all_lines = file.readlines()
    sleep_cond = all_lines[len(all_lines)-1].replace("\n","")
    print(sleep_cond)
    if ( sleep_cond == 'drowsy'):
        return True
    else:
        return False

###*********************************************************************    
###*********************************************************************

def sleep_alaram():
    
    while(True):
        play("C:/Users/AnyOneElse/GP_POP/Batot/sounds/Alarm.wav")
        cancel = speech2txt()
        cancel_en = translate(cancel)
        print("*********************** AAAAAAAALARARAM   sleeeppeppepepp  ***********************")
        cancel_en = cancel_en.replace('.',' ').replace(',',' ').lower()
        print(cancel_en)

        if( (cancel_en.find("stop") != -1 ) or   (cancel_en.find("stood") != -1 ) ):
            speak_ar("من فضلك أركن و فَوِّقْ نفسك")
            break
    
