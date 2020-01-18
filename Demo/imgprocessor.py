import cv2
from settings import Settings



class ImgProcessor():
    """A class to store all levels for Sketch It."""

    def __init__(self):
        """Initialize class"""
        self.settings = Settings()

    def process_image(self, frame):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_gray_blur = cv2.GaussianBlur(frame_gray, (5,5),0)
        return(frame_gray_blur)

