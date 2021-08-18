import operator
import numpy as np

def mix_mood_predict (camera_pred_list, text_pred_list):
    text_pred_list = text_pred_list[0]
    camera_pred_list = camera_pred_list[0]
    
    classes = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise','neutral'] 
    final_prediction =[]
    final_prediction.append((text_pred_list[0]+camera_pred_list[0])/2.0)
    final_prediction.append((text_pred_list[1]+0)/2.0)
    final_prediction.append((text_pred_list[2]+camera_pred_list[5])/2.0)
    final_prediction.append((text_pred_list[3]+camera_pred_list[3])/2.0)
    final_prediction.append((text_pred_list[4]+camera_pred_list[1])/2.0)
    final_prediction.append((text_pred_list[5]+camera_pred_list[4])/2.0)
    final_prediction.append((0+camera_pred_list[2])/2.0)
    max_index, max_value = max(enumerate(final_prediction), key=operator.itemgetter(1))
    return str(classes[max_index])

#************************************************************************************************************
mood = 'Null'  
camera_classes = ['angry', 'sad', 'neutral','happy', 'surprise','fear']
neg_classes = ['angry', 'sad','fear', 'disgust']
pos_classes = ['neutral','happy', 'surprise']

def mix_mood_fn(cam_mood, text_mood, cam_pred_list, text_pred_list):
    print("MIXMIXMIXMIXMIXMIXMIXMIXMIXMIX")
    print(cam_mood, text_mood)
     
    if( text_mood == ""):  #tested 
        mood = cam_mood

    elif( text_mood == cam_mood ): #tested
        mood = cam_mood

    #tested
    elif  ((cam_mood in neg_classes) and (text_mood in neg_classes)) or ((cam_mood in pos_classes) and (text_mood in pos_classes)): 
        mood = mix_mood_predict (cam_pred_list, text_pred_list)
        
    elif (text_mood in pos_classes )and (cam_mood in neg_classes ): #tested
        mood =  'hide'

    elif (text_mood in neg_classes )and (cam_mood in pos_classes ): #tested
        mood = 'kidding'
    else:
        pass
    
    print("MOOOOOOOOOOOOOOOOOOOOOOOODDDDDDDDDDDD")
    print(mood)
    
    file = open("C:/Users/AnyOneElse/GP_POP/cam_emotion_detect/mix_mood.txt", "a")
    file.write(mood + "\n")   
    file.close()
        
