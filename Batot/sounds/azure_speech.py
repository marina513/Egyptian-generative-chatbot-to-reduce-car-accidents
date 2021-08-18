import os
import arabic_reshaper
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, AudioConfig ,ResultReason ,CancellationReason
import  azure.cognitiveservices.speech as speechsdk


def speech2txt():
    cog_key = 'dc7da06fdb02445b997439d804b5e17e'
    cog_location = 'eastus'
    
    speech_config = speechsdk.SpeechConfig(subscription= cog_key, region= cog_location)
    speech_config.speech_recognition_language="ar-EG" 

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    speech_config.set_property(speechsdk.PropertyId.Speech_LogFilename, "LogfilePathAndName")

    print("Say something...please")
    result = speech_recognizer.recognize_once()

    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
        return '0'
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    # </code>

    return result.text




##################################################

def speech2txt_en():
    cog_key = 'dc7da06fdb02445b997439d804b5e17e'
    cog_location = 'eastus'
    
    speech_config = speechsdk.SpeechConfig(subscription= cog_key, region= cog_location)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    speech_config.set_property(speechsdk.PropertyId.Speech_LogFilename, "LogfilePathAndName")

    print("Say something...please")
    result = speech_recognizer.recognize_once()

    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
        return '0'
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    # </code>

    return result.text

