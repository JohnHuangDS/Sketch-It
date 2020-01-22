import cv2
import sys
import imutils
import numpy as np

from settings import Settings
from display_screen import Display
from imgprocessor import ImgProcessor
from trained_model import Trained_Model

class SketchIt:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""

        self.settings = Settings()
        self.background_processed = None
        self.cam = cv2.VideoCapture(0)
        self.display = Display()
        self.imgprocessor = ImgProcessor()
        self.trained_model = Trained_Model()
        self.background_processed = self._calibrate_background()

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            self._start_screen()

            if self.settings.current_level == 1:
                self._check_events()
            else:
                self._play_level()

    def _start_screen(self):
        """Display the starting screen for the game"""

        ret, frame = self.cam.read()
        self.display.start_screen(frame)


    def _check_events(self):
        """Checks for key presses and determines what to do next"""

        key = cv2.waitKey(1)

        if key == ord("c"):
            self.background_processed = self._calibrate_background()

        if key == ord("s"):
            self._play_level()

        if key == ord("q"):
            sys.exit()


    def _calibrate_background(self):
        """Returns an array for the static background image"""

        while True:
    
            ret, frame = self.cam.read()
            self.display.calibration_screen(frame.copy())
            key = cv2.waitKey(1)
            if key == ord("y"):
                break
            if key == ord("q"):
                sys.exit()
        
        background_proccessed = self.imgprocessor.image_preprocessing(frame)
        return(background_proccessed)

    def _play_level(self):
        """Displays the current level being played and prompts user to draw"""
        self.settings.reset_response()
        object_str = self.settings.level_responses[self.settings.current_level][0]
        prediction_array = []
        next_level_flag = False

        while True:
            ret, frame = self.cam.read()

            self.settings.object_undetected()
            contour_box = self._create_contour_box(frame)


            if contour_box:
                self.settings.object_detected()
                prediction = self._predict_drawing(frame, contour_box)
                prediction_array = np.append(prediction_array, prediction)

            if len(prediction_array) > 5:
                if len(np.unique(prediction_array[-5:])) == 1:

                    correct_response = self._check_response(prediction_array[-1], object_str)

                    if correct_response == True:
                        next_level_flag = True

            if next_level_flag == True:
                self.settings.correct_drawing_response(self.settings.current_level)
                self.display.level_screen(frame, object_str, self.settings.object_detection, self.settings.response, contour_box)

            else:
                self.display.level_screen(frame, object_str, self.settings.object_detection, self.settings.response, contour_box)


            key = cv2.waitKey(1)

            if key == ord("q"):
                sys.exit()

            if key == ord("r"):
                self.settings.reset_game()
                break

            if next_level_flag == True and key == ord("n"):

                if self.settings.current_level < self.settings.total_levels:
                    self.settings.level_passed()
                else:    
                    self.settings.reset_game()
                break

 
    def _create_contour_box(self, frame):
         #standard image processing
        test_image = self.imgprocessor.image_preprocessing(frame)

        #contour preprocessing dilates the strokes to make it larger
        dilated_test_image = self.imgprocessor.contour_preprocessing(test_image, self.background_processed)

        #creates a box around a drawing if it is detected
        contour_box = self._find_contours(dilated_test_image.copy())

        return(contour_box)


    def _find_contours(self,test_image):
        """Return a list of contour box dimensions"""

        #initialize variables
        x = None
        y = None
        w = None
        h = None

        #find contours
        cnts = cv2.findContours(test_image, cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        #go through the contours, ignore them if they are too small
        for c in cnts:
            if cv2.contourArea(c) <self.settings.minimum_contour_area:
                continue
            #create variables of a bounding rectangle
            (x,y,w,h) = cv2.boundingRect(c)
        
        #create varibale to return
        contour_box = [x, y, w, h]

        #if there are no contours, return nothings
        if contour_box == [None, None, None, None]:
            pass
        else:
            #print(type(contour_box))
            #print(contour_box)
            return(contour_box)

    def _predict_drawing(self, frame, contour_box):
        """Returns an string representing the class"""

        #standard image processing
        test_image = self.imgprocessor.image_preprocessing(frame)

        #contour preprocessing dilates the strokes to make it larger
        dilated_test_image = self.imgprocessor.contour_preprocessing(test_image, self.background_processed)

        #preprocess image for model_testing
        model_image_processed = self.imgprocessor.model_preprocessing(dilated_test_image, contour_box)

        #test image against trained model
        prediction = self.trained_model.predict_image(model_image_processed)

        return(prediction)


    def _check_response(self, stable_prediction, object_str):
        """Returns True or False"""
        if stable_prediction == object_str:
            return(True)
        else:
            return(False)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = SketchIt()
    game.run_game()