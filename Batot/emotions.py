import sys
sys.path.insert(1 , 'D:/GP/sounds')
from sounds.speak_ import  speak,speak_ar,play

moods = ['kidding','hide' , 'angry', 'sad', 
        'neutral','happy', 'surprise','fear', 'disgust']
mood_song = ["انت شكلك فرحان و كلامك زعلان انت بتهزر",
             "شكلك متضايق بس كلامك فرحان لا تخبي عليا",
            "هدي نفيك لا تغضب",
            "لا تحزن ضحكتك بالدنيا",
            "",
            "شكلك فرحان يارب دايما",
            "لمازا انت متفاجىء",
            "لا تخاف انا بجانبك",
            "لماذا انت مشمئز" ]


def all_emotions(mood):
    print("MOOOOOOOOOOOOOOOOOOOOOOOODDDDDDDDDDDD")
    print(mood)
    if(mood == 'neutral'):
        pass
    else:
        for i in range(len(moods)):
            if( moods[i] == mood ):
                speak_ar(mood_song[i])
    
    return
