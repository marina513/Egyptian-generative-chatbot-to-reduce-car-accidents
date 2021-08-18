import re
import cv2 
import numpy as np
from tensorflow.keras.applications.inception_v3 import InceptionV3

def FeatureVector(face):
      img=cv2.resize(face,(224,224))
      model = InceptionV3(include_top=False,weights='imagenet',pooling='avg',input_shape=(224,224,3))
      feature_Vector=model.predict(np.array([img])/255)[0]

      return feature_Vector


def sleep_fn(seq_frames, model_sleep):
    if(len(seq_frames) == 8):
        print("**************** sleep detect ***********")
        seq_frames = np.array(seq_frames)
        seq_frames = seq_frames.reshape(1,8,2048)
        y_pred=model_sleep.predict_classes(seq_frames)
        #score= model.predict_proba(seq_frames)
        file_sleep = open("C:/Users/AnyOneElse/GP_POP/cam_emotion_detect/sleep.txt", "a")
        if y_pred[0] == 0 :                 
            case= False #Alert
            print("Alert")
            file_sleep.write("Alert" + "\n")
            
        elif y_pred[0]== 1 :
            case = True #Drowsy
            print("drowsy")
            file_sleep.write("drowsy" + "\n")
        
        file_sleep.close()
        return case

    else:
        print("len sleep frames != 8")
        return False