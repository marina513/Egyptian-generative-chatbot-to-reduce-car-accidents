import tensorflow as tf
import tensorflow_hub as hub
import operator
from mtranslate import translate
keras = tf.keras


emotion = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise']

def Predicted_Emotion_text (drop_model):
    ###################################
    file = open("C:/Users/AnyOneElse/GP_POP/Batot/data/file_chat_user_history.txt", "r" , encoding='utf-8')
    all_lines = file.readlines()
    if((len(all_lines) == 0)):
        print("empty user history or at end")
        input_msg = ""
        return input_msg, []
    else:
        input_msg = all_lines[len(all_lines)-1].replace("\n","")
        if (input_msg == "end" ):
            print("no conversation is going")
            input_msg = ""
            return input_msg, []
        
        print(" KLAAAAAAAAAAAAAMMMMMMM  PRRRREDDDDDDDDEDED")
        print("last msg: " , (input_msg))
    ###################################
        input_msg = translate(input_msg, 'en')
        drop_prediction = drop_model.predict([str(input_msg)])
        index, value = max(enumerate(drop_prediction[0]), key=operator.itemgetter(1))
        return   str(emotion[index]) ,drop_prediction 

