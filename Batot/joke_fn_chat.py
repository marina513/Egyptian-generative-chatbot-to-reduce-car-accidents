import sys
sys.path.insert(1 , 'C:/Users/AnyOneElse/GP_POP/Batot/Jokes')
from Jokes.joke_num import joke_num
from Jokes.joke import joke_fn
sys.path.insert(1 , 'C:/Users/AnyOneElse/GP_POP/Batot/sounds')
from sounds.speak_ import  speak,speak_ar,play
from sounds.azure_speech import speech2txt
from mtranslate import  translate
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


##########################################################################
def joke_fn_main(again):

    if((again == False)):
        speak_ar("اهلا ما اسمك")
        name = speech2txt()
        if(name == '0'):
            speak_ar("لم أفهم")
            joke_fn_main(False)
        name = translate(name,'en')
        speak_ar(f"اهلا,{name}, اتشرفت بمقابلتك تحب تسمع نكتة")

    elif(again == True):
        speak_ar("تحب تسمع نكتة")   
   
    want_joke = speech2txt()
    
    ###################################################
    if(want_joke == '0'):
        speak_ar("لم أفهم")
        joke_fn_main(True)
    elif(want_joke != '0'):
        pass

    ###################################################################################
    print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSs")
    print(want_joke)
    want = translate( want_joke , 'en').replace('.','').lower()
    want_joke = lemmatizer.lemmatize(want)
    print(want_joke)

    if ( ( (want_joke.find('ah') != -1) or (want_joke.find('yes') != -1) or  (want_joke.find('oh') != -1)  
        or (want_joke.find('uh') != -1)  or (want_joke.find('ah') != -1) )) :
        
        speak_ar("عاوز نكتة معينة")
        print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSs")
        want_specific = speech2txt()
        want_specific = translate( want_specific , 'en').replace('.','').lower()
        want_specific = lemmatizer.lemmatize(want_specific)
        print(want_specific)
        specific_joke = want_specific

        if ((specific_joke.find( "yes") != -1) or (specific_joke.find( "ah") != -1) ):
            speak_ar(" ما الموضوع")
            topic = translate(speech2txt())
            print(topic)
            joke_rand, num = joke_num(topic, "ar")
        else:
            search = "random"
            joke_rand, num = joke_num(search, "ar")
            topic = joke_rand

        if ((num != 0) ):
            speak_ar(f"يوجد {num} نقطة,ما هو رقم حظك")
            num_lucky = speech2txt()
            num_lucky = translate(num_lucky, 'en')
            joke = joke_fn(topic, 4)
            print("\n")
            if ("Q" in joke[0]):
                Q = joke[0]
                A = joke[1]
            else:
                Q = joke[1]
                A = joke[0]
            speak(Q)
            speak(A)
            play("C:/Users/AnyOneElse/GP_POP/Batot/sounds/silly_joke.wav")
            
        elif ((num == 0) ):
            speak_ar("لم اجدها اختر واحده اخرى")


    elif(  (want_joke.find('no') != -1) ) :
        speak_ar("اممم طيب مع السلامه سوق بالراحه بحبك")


    elif( ((want_joke.find('no') == -1)  and (want_joke.find('ah') == -1))):
        print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
        speak_ar("لم افهم")
        joke_fn_main(True)

    else:
        return