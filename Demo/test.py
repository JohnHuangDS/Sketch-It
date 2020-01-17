import cv2


video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    cv2.imshow("CAN YOU DRAW",frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
