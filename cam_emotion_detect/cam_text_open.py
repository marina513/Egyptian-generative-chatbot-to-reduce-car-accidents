   
#------------------------------------------------------------------------------------------------------------
'''                                                  Liberaries ^_^                                       '''
#--------------------------------------------------------------------------------------------------------
from re import I
import cv2 
import numpy as np 
import torch
from collections import Counter
from Emotion_model import Deep_Emotion
from delay import wait
from mix_mood import mix_mood_fn
import tensorflow as tf
import tensorflow_hub as hub
import operator
from mtranslate import translate
from text_emotion import Predicted_Emotion_text
from sleep import FeatureVector, sleep_fn

keras = tf.keras
#----------------------------------------------------------------------------------------------------------
#sleep model
model_sleep = keras.models.load_model("C:/Users/AnyOneElse/GP_POP/cam_emotion_detect/models/GRU_model_layer.h5")
#----------------------------------------------------------------------------------------------------------
# text model
model_path = 'C:/Users/AnyOneElse/GP_POP/cam_emotion_detect/models/USE_dropoutMood_model.h5'
drop_model = tf.keras.models.load_model(model_path , custom_objects={'KerasLayer': hub.KerasLayer})
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
def most_frequent(List):
    print("***********************  8 emotions ***************")
    occurence_count = Counter(List)
    try:
        if (((occurence_count.most_common(1)[0][0]) == 2) and ( (occurence_count.most_common(2)[1][0] == 1)  or (occurence_count.most_common(2)[1][0] == 0) )  ):
            return  occurence_count.most_common(2)[1][0]
        return occurence_count.most_common(1)[0][0]

    except:
        return occurence_count.most_common(1)[0][0]

#------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
# camera emotion prediction
def Predicted_Emotion_camera(testimg_data , model, device):
    
    testimg_data = testimg_data.reshape(1, 1, 48, 48)
    testimg_data = torch.Tensor(testimg_data) # transform to torch tensor

    # prediction for test set
    with torch.no_grad():
        testimg_data = testimg_data.to(device)
        output_img = model(testimg_data)

    softmax_img = torch.exp(output_img).cpu()
    prob_img = list(softmax_img.numpy())
    predicted_img = np.argmax(prob_img, axis=1)

    return predicted_img, prob_img

                 
#------------------------------------------------------------------------------------------------------------
'''                                                  Facial Expression  model                              '''
#--------------------------------------------------------------------------------------------------------
def camera_pred(sleep_detect):
    device = torch.device("cpu")
    FER_Model = Deep_Emotion(256)
    FER_Model.load_state_dict(torch.load("C:/Users/AnyOneElse/GP_POP/cam_emotion_detect/models/Emotion_Recognition_model" , map_location=torch.device('cpu')))
    FER_Model.to(device)

    #--------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------
    '''                                                    Camera & model                                    '''
    #--------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Can't open camera ")

    predictions_8 = []
    predictions_8_list = []
    cam_emotions = ['angry', 'sad', 'neutral' , 'happy' , 'surprise' , 'fear']
    seq_frames = []
    iter_num = 0
    while True :
            #wait(3000000)
            print(" iter num : " , iter_num)
            iter_num = iter_num + 1
            ret, frame = cap.read()
            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            face_coordinates = trained_face_data.detectMultiScale(gray_img,1.1,4)
            #print(len(face_coordinates))
            if len(face_coordinates) == 0 :
                print(" Camera intializes")
            else :
                for coordinate in face_coordinates:
                    (x, y, w, h) = coordinate
                    roi_gray = gray_img[ y : y + h , x : x + w]
                    
                    #*************************************************************
                    #********** sleep
                    if(sleep_detect):
                        roi_color = frame[ y : y + h , x : x + w]
                        feature_Vector=FeatureVector(roi_color)
                        seq_frames.append(feature_Vector)
                        if(len(seq_frames) == 8):
                            iter_num = 0
                            sleepy = sleep_fn(seq_frames, model_sleep)
                            seq_frames = []
                            if(sleepy):
                                cv2.putText(frame , "Drowsy", ( 50,50 ) , cv2.FONT_HERSHEY_PLAIN, 3 , (0, 0,255) ,cv2.LINE_4)
                            else:
                                cv2.putText(frame , "Alert", ( 50,50 ) , cv2.FONT_HERSHEY_PLAIN, 3 , (0, 0,255) ,cv2.LINE_4)
                    else:
                        wait(3000000)
                                
                    #**********
                    #*************************************************************
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,0 ), thickness=2)
                    facesss = trained_face_data.detectMultiScale(roi_gray)
                    if len(facesss)==0 :
                        print("not detected")
                    else:
                        for (ex,ey , ew , eh ) in facesss:
                            face_roi=roi_gray[ex :  ex+ ew ,  ey : ey+ eh]
                        final_image= cv2.resize(face_roi , (48 ,48 ))
                        final_image= np.expand_dims(final_image ,0)
                        final_image= final_image / 255

                    # Emotion Recognition Part     
                    #--------------------------------------------------------------------------------------------------------
                    #--------------------------------------------------------------------------------------------------------
                        prediction, Emotions_list_cam = Predicted_Emotion_camera(final_image , FER_Model, device)
                        predictions_8.append(prediction[0]) 
                        predictions_8_list.append(Emotions_list_cam)
                        
                        if(len(predictions_8) == 4):

                            most_pred = most_frequent(predictions_8)
                            most_pred_list = predictions_8_list[ predictions_8.index(most_pred) ]
                           
                            print("@************************************************@")
                            print("most frequent prediction: " , cam_emotions[most_pred])

                            file = open("cam_emo.txt", "a")
                            file.write(cam_emotions[most_pred] + "\n")
                            file.close()
                                
                            text_mood, text_mood_list = Predicted_Emotion_text(drop_model)
                            mix_mood_fn(cam_emotions[most_pred], text_mood, most_pred_list, text_mood_list)
                            predictions_8 = []
                            predictions_8_list = []
                    
                    #--------------------------------------------------------------------------------------------------------
                    #--------------------------------------------------------------------------------------------------------
                    #--------------------------------------------------------------------------------------------------------
                    
                        if prediction[0] == 0 : #angry
                            cv2.putText(frame , " angry ", ( x  ,y ) , cv2.FONT_HERSHEY_PLAIN, 3 , (0, 0,255) ,cv2.LINE_4)
                            cv2.rectangle(frame , (x,y ) ,(x + w ,y+ h  ) , (0,0,225) )
                            
                        elif prediction[0]== 1 : # sad

                            cv2.putText(frame , " Sad ", ( x  ,y ) , cv2.FONT_HERSHEY_PLAIN, 3 , (0, 0,255) ,cv2.LINE_4)
                            cv2.rectangle(frame , (x,y ) ,(x + w ,y+ h  ) , (0,0,225) )
                        
                        elif prediction[0] == 2 : #neutral

                            cv2.putText(frame , " NEUTRAL ", ( x  ,y ) , cv2.FONT_HERSHEY_PLAIN, 3 , (0, 0,255) ,cv2.LINE_4)
                            cv2.rectangle(frame , (x,y ) ,(x + w ,y+ h  ) , (0,0,225) )
                            
                        elif prediction[0] == 3 : #happy

                            cv2.putText(frame , " HAPPY ", ( x  ,y ) , cv2.FONT_HERSHEY_PLAIN, 3 , (0, 0,255) ,cv2.LINE_4)
                            cv2.rectangle(frame , (x,y ) ,(x + w ,y+ h  ) , (0,0,225) )
                            
                        elif prediction[0] == 4 : #surprise

                            cv2.putText(frame ,  " SURPRISE ", ( x  ,y ) , cv2.FONT_HERSHEY_PLAIN, 3 , (0, 0,255) ,cv2.LINE_4)
                            cv2.rectangle(frame , (x,y ) ,(x + w ,y+ h  ) , (0,0,225) )
                            
                        else :

                            cv2.putText(frame ,  " FEAR ", ( x  ,y ) , cv2.FONT_HERSHEY_PLAIN, 3 , (0, 0,255) ,cv2.LINE_4)
                            cv2.rectangle(frame , (x,y ) ,(x + w ,y+ h  ) , (0,0,225) )
                            
            cv2.imshow('Image',frame)       

            if cv2.waitKey( 10)& 0xFF == ord('q') :
                break
    cap.release()
    cv2.destroyAllWindows()



                 
#------------------------------------------------------------------------------------------------------------
'''                                              THE END ^_^                                               '''
#-------------------------------------------------------------------------------------------------------