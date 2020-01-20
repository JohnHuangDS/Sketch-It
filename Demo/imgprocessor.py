import cv2
#from settings import Settings



class ImgProcessor():
    """A class to store all levels for Sketch It."""

    def __init__(self):
        """Initialize class"""
        #self.settings = Settings()

    def process_image(self, frame):
        """Standard method of processing images for Sketch It"""
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_gray_blur = cv2.GaussianBlur(frame_gray, (5,5),0)
        return(frame_gray_blur)

    def contour_preprocessing(self, frame, background_processed):
        """Preprocessing image to find contours"""

        #find the absolute difference between current frame and background frame
        frame = cv2.absdiff(background_processed,frame)

        #create a threshold to make the image black or white
        thresh = cv2.threshold(frame, 50, 255, cv2.THRESH_BINARY)[1]

        #dilate to increase thickeness of contours
        dilate = cv2.dilate(thresh, None, iterations = 2)

        return(dilate)