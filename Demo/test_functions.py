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

def frame_preprocessing(frame_capture,x,y,w,h):

	#convert to image for grascaling and crop based on crop box co-ordinates
	pil_image = Image.fromarray(frame_capture)
	pil_image = pil_image.convert('L')
	if h>w:
		pil_crop = pil_image.crop((x-50-((h-w)/2),y-50,x+w+50+((h-w)/2),y+h+50))
	if h<w:
		pil_crop = pil_image.crop((x-50,y-50-((w-h)/2),x+w+50,y+h+50+((w-h)/2)))
	#convert to array for thresholding(theres probably a way to do this in an image)
	frame_array = np.array(pil_crop)
	frame_array = np.where(frame_array <= 100,0,frame_array)
	frame_array = np.where(frame_array > 100, 255, frame_array)

	#turn back into an image, subtract from 255 to normalize with dataset, then resize image with BICUBIC sampling and turn into an array
	resized_image = Image.fromarray(frame_array)
	test_array = np.array(resized_image.resize((28,28), Image.BICUBIC))

	#returns an array
	return(test_array)

#load_model function loads a trained model from a json and loads the weights from a h5 file.
def load_cnn_model(model_name, model_weight_name):
    json_file = open(model_name)
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(model_weight_name)
    loaded_model.compile(loss = 'sparse_categorical_crossentropy',
                      optimizer = 'Adam',
                      metrics = ['accuracy'])

    sketch_list = ['angel', 'sword', 'wine glass', 'yoga']

    return(loaded_model,sketch_list)

#model_reshape_predict function takes and image, model, and the unique targets and returns a guess for what image is shown.
def model_reshape_predict(image, model, y_unique):
    #Define the img rows and cols
    img_rows = 28
    img_cols = 28

    #Reshape the image
    test= image.reshape(1, img_rows, img_cols, 1)

    #Predict based on model
    prediction = model.predict(test)

    #Create the labels off of y_unique
    my_encoder = LabelEncoder()
    my_encoder.fit(y_unique)

    #Change prediction to label
    pred_label = my_encoder.inverse_transform([np.argmax(prediction)])[0]

    return (pred_label,prediction)

def get_background(set_width,set_font,font_y_pad):
	#initiate webcam
	cam = cv2.VideoCapture(0)

	background= None
	run = True
	while run:
		ret, frame = cam.read()

		frame2 = imutils.resize(frame, width = set_width)
		cv2.putText(frame2, 'Calibrating Background',(10,font_y_pad),
		cv2.FONT_HERSHEY_SIMPLEX, set_font, (0, 0, 0), 2)

		cv2.putText(frame2, 'Press (y) to Continue',(10,frame2.shape[0]-font_y_pad),
		cv2.FONT_HERSHEY_SIMPLEX, set_font, (0, 0, 0), 2)

		cv2.imshow("CAN YOU DRAW",frame2)

		key = cv2.waitKey(1)


		print(key)
		if key == ord("y"):
			run = False
		if key == ord("q"):
			break
	background = frame
	background_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
	background_gray_blur = cv2.GaussianBlur(background_gray, (5,5),0)
	background_proccessed = background_gray_blur
	cam.release()
	cv2.destroyAllWindows
	return(background_proccessed)


def get_level(level_name, correct_answer, background_processed, model, sketch_list,next_level,set_width):
	cv2.destroyAllWindows
	cam = cv2.VideoCapture(0)

	guess_array = np.array([])
	correct = level_name
	answer = 0
	result = 0
	set_font = int(set_width/400)
	font_color = (0,0,0)
	font_y_pad = int(set_width/10)

	start = True
	while start == True:
	    ret, frame = cam.read()

	    text_detection = "Undetected"

	    #Process image
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    wine = cv2.GaussianBlur(gray, (5,5),0)

	    #Get the Differenct, threshold and dilate it.
	    frameDelta = cv2.absdiff(background_processed,wine)
	    thresh = cv2.threshold(frameDelta, 50, 255, cv2.THRESH_BINARY)[1]
	    dilate = cv2.dilate(thresh, None, iterations = 2)

	    #Find and grab contours
	    cnts = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL,
	        cv2.CHAIN_APPROX_SIMPLE)
	    cnts = imutils.grab_contours(cnts)
	    if answer == 0:
	    	text_guess = 'Hmmmm'
	    max_contour = 4000

	    sketch_x = None
	    sketch_y = None
	    sketch_w = None
	    sketch_h = None
	    #loop through the contours, ignore them if they are too small
	    for c in cnts:
	        if cv2.contourArea(c) <set_width*set_width/250:
	            continue
	        #create and draw a bounding rectangle
	        (x,y,w,h) = cv2.boundingRect(c)
	        c_area = w*h
	        if c_area > max_contour:
	            sketch_x = x
	            sketch_y = y
	            sketch_w = w
	            sketch_h = h



	    cv2.putText(frame, 'Lets see you draw a {}'.format(level_name),(10,font_y_pad),
	            cv2.FONT_HERSHEY_SIMPLEX, int(set_font*1.5), (0, 0, 0), 2)

	    cv2.putText(frame, 'Sketch: {}'.format(text_detection),(10,2*font_y_pad),
	            cv2.FONT_HERSHEY_SIMPLEX, set_font, (0, 0, 0), 2)


	    cv2.putText(frame, "{}".format(text_guess), (10, frame.shape[0]-font_y_pad),
	            cv2.FONT_HERSHEY_SIMPLEX, set_font, (0, 0, 0), 2)



	    frame = imutils.resize(frame, width = set_width)

	    cv2.imshow("CAN YOU DRAW",frame)
	    try:
	        cv2.imshow("Frame_processing", processed_frame)
	    except:
	        pass
	    key = cv2.waitKey(1)


	    print(key)
	    if key == ord("n"):
	        start = False
	    if key == ord("q"):
	        result = 0
	        break

	cam.release()
	return(result)
