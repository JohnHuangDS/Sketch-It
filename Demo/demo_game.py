#DEMO GAME
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
import numpy as np
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from keras.models import model_from_json
import test_functions


#determine window resize(1920x1080, 1280x720, 640,480)
set_width = 1080
set_font = int(set_width/400)
font_color = (0,0,0)
font_y_pad = int(set_width/10)

#Calibrate Background
background_processed = test_functions.get_background(set_width, set_font, font_y_pad)
print(background_processed)
print(background_processed.shape)

#Load Test models
model,sketch_list = test_functions.load_cnn_model('CNN_model.json','CNN_model.h5')
print(sketch_list)

what = cv2.VideoCapture(0)
run = True
while run:
    #Load Level

    result = 0
    ret, frame = what.read()
    frame = imutils.resize(frame, width = set_width)

    cv2.putText(frame, "Welcome to 'Can you draw?''",(10,font_y_pad),
            cv2.FONT_HERSHEY_SIMPLEX, set_font, font_color, 2)

    cv2.putText(frame, "Press (s) to start",(10,frame.shape[0]-2*font_y_pad),
            cv2.FONT_HERSHEY_SIMPLEX, set_font, font_color, 2)

    cv2.putText(frame, "Press (r) to recalibrate",(10,frame.shape[0]-font_y_pad),
            cv2.FONT_HERSHEY_SIMPLEX, set_font, font_color, 2)

    cv2.imshow("CAN YOU DRAW",frame)

    key = cv2.waitKey(1)

    if key == ord("r"):
        background_processed = test_functions.get_background(set_width, set_font, font_y_pad)

    if key == ord("s"):
        cv2.destroyAllWindows
        result = test_functions.get_level('wine glass','Thats a wine glass alright.',background_processed, model, sketch_list,2, set_width)

    if result == 2:
        result = test_functions.get_level('sword','ZING ZING, thats a sword!',background_processed, model, sketch_list,3,set_width)

    if result == 3:
        result = test_functions.get_level('angel','What a beautiful Angel',background_processed, model, sketch_list,4,set_width)

    if result == 4:
        result = test_functions.get_level('yoga','Nice! Thats its, thanks for playing!',background_processed, model, sketch_list,5,set_width)

    if key == ord("q"):
      break
