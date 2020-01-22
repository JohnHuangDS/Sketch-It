import cv2
from settings import Settings



class ImgProcessor():
    """A class to store all levels for Sketch It."""

    def __init__(self):
        """Initialize class"""
        self.settings = Settings()

    def image_preprocessing(self, frame):
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
        dilate = cv2.dilate(thresh, None, iterations = 8)

        return(dilate)

    def model_preprocessing(self, frame, contour_dimensions):
        """Preprocessing image for model prediction"""

        #crop image
        crop_img = self._contour_crop(frame, contour_dimensions)

        #resize image
        model_array = cv2.resize(crop_img, (28,28), interpolation = cv2.INTER_AREA)

        #show processed image
        #cv2.imshow("Model_Preprocessing", model_array)

        #returns an array
        return(model_array)

    def _contour_crop(self, frame, contour_dimensions):
            """Crop an image based on contour box dimensions"""
            x, y, w, h = contour_dimensions[0], contour_dimensions[1], contour_dimensions[2], contour_dimensions[3]

            #add padding to crop box
            if h>w:
                #add additional padding (h-w)/2 to x if width is smaller than height
                crop_x = int(x-self.settings.model_preprocessing_padding-((h-w)/2))
                crop_y = int(y-self.settings.model_preprocessing_padding)
                crop_w = int(w+2*(self.settings.model_preprocessing_padding+((h-w)/2)))
                crop_h = int(h+2*self.settings.model_preprocessing_padding)
            if h<w:
                #add additional padding (w-h)/2 to h if height is smaller than weight
                crop_x = int(x-self.settings.model_preprocessing_padding)
                crop_y = int(y-(self.settings.model_preprocessing_padding+((w-h)/2)))
                crop_w = int(w+2*self.settings.model_preprocessing_padding)
                crop_h = int(h+2*(self.settings.model_preprocessing_padding+((w-h)/2)))

            if crop_x < 0:
                crop_x = 0
            if crop_y < 0:
                crop_y = 0
                
            crop_img = frame[crop_y:(crop_y+crop_h),crop_x:(crop_x+crop_w)]
            return(crop_img)