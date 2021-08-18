import pyttsx3
from gtts import gTTS
import platform
import signal
if platform.system() != 'Linux':
    signal.SIGINT = 2
import librosa
import soundfile as sf
import simpleaudio as sa
import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

converter = pyttsx3.init()

def speak(response):
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    converter.setProperty('voice', voice_id)
    converter.setProperty('rate', 120)
    converter.setProperty('volume', 12.5)
    converter.say(response)
    converter.runAndWait()




def speak_ar(text):
    #txt to wav 
    tts = gTTS(text=text, lang="ar")
    filename = "C:/Users/AnyOneElse/GP_POP/Batot/sounds/voice.wav"
    tts.save(filename)
    
    #write to temp wav to escape RIFF id error
    x,_ = librosa.load('C:/Users/AnyOneElse/GP_POP/Batot/sounds/voice.wav', sr=16000)
    sf.write('C:/Users/AnyOneElse/GP_POP/Batot/sounds/tmp.wav', x, 16000)

    #play wav file
    wave_obj = sa.WaveObject.from_wave_file("C:/Users/AnyOneElse/GP_POP/Batot/sounds/tmp.wav")
    play_obj = wave_obj.play() 
       
    play_obj.wait_done() 


def play(path):
    
    #play wav file
    wave_obj = sa.WaveObject.from_wave_file(path)
    play_obj = wave_obj.play() 
       
    play_obj.wait_done()

    