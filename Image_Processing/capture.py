import cv2
import numpy

#initiate camera
cam = cv2.VideoCapture(0)

while True:

    #read frame
    ret, frame = cam.read()
    cv2.imshow("CAN YOU DRAW",frame)


    key = cv2.waitKey(1)

    #c = capture and save frame as .npy
    if key == ord("c"):
        #print(frame)
        a = numpy.asarray(frame)
        #print(a)
        numpy.save("imagecapture", a)

    if key == ord("q"):
        break