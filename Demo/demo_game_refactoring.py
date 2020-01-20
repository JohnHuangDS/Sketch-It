import cv2
import sys
import imutils

from settings import Settings
from levels import Levels
from display_screen import Display
from imgprocessor import ImgProcessor

class SketchIt:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""

        #attributes
        self.settings = Settings()
        self.background_processed = None
        self.cam = cv2.VideoCapture(0)
        self.display = Display()
        self.imgprocessor = ImgProcessor()

        #calibrate background
        self.background_processed = self._calibrate_background(self.cam)

    #method
    def run_game(self):
        """Start the main loop for the game."""

        while True:

            #initiate start screen
            self._start_screen(self.cam)

            #check for events
            self._check_events()

    #helper method
    def _start_screen(self, cam):
        """Start screen is the first screen the user sees"""

        #read frame from camera feed
        ret, frame = cam.read()

        #diplay start screen
        self.display.start_screen(frame)


    #helper method
    def _check_events(self):
        """Checks for key presses and determines what to do next"""

        """Responds to key presses"""
        key = cv2.waitKey(1)

        #c = start calibration and assign to background_processed 
        if key == ord("c"):
            self.background_processed = self._calibrate_background(self.cam)

        #s = start game key
        if key == ord("s"):
            self._play_level(self.cam)

        #q = exit game key 
        if key == ord("q"):
            sys.exit()


    #helper method
    def _calibrate_background(self,cam):
        """Calibrates background to acccount for difference in lighting"""

        while True:
    
            #read frame from camera feed
            ret, frame = cam.read()

            #display calibration feed, feed a copy since we dont want to include the text
            #into process_image later on
            self.display.calibration_screen(frame.copy())

            key = cv2.waitKey(1)

            #wait for y to continue
            if key == ord("y"):
                break

            if key == ord("q"):
                sys.exit()
        
        #take the last frame and shown and process it (blur and grayscale)
        print(frame)
        background_proccessed = self.imgprocessor.process_image(frame)
        return(background_proccessed)

    def _play_level(self, cam):
        """Displays the current level being played and prompts user to draw"""

        draw_object = self.settings.level_answers[self.settings.current_level]

        print(draw_object)

        while True:
            # read frame frome camera
            ret, frame = cam.read()

            #process image for calculating contours
            contour_image = self.imgprocessor.process_image(frame)
            contour_image = self.imgprocessor.contour_preprocessing(contour_image, self.background_processed)

            #find the contours
            contour_dimensions = self._find_contours(contour_image.copy())
            
            #if a contour dimension is found, draw a bounding box and determine if image is passes
            if contour_dimensions:
                print(contour_dimensions)

                bounding_box_x, bounding_box_y, bounding_box_w, bounding_box_h = contour_dimensions[0], contour_dimensions[1], contour_dimensions[2], contour_dimensions[3],

                cv2.rectangle(frame, (bounding_box_x-20,bounding_box_y-20),(bounding_box_x+bounding_box_w+20, bounding_box_y+bounding_box_h+20),
                    (0,255,0),2)

            processed_frame = imgprocessor.model_preprocessing(contour_image)




            #display level screen
            self.display.level_screen(frame, draw_object)


            #Determining if a contour has been found
        


            key = cv2.waitKey(1)

            if key == ord("q"):
                sys.exit()

            if key == ord("r"):
                break

    def _find_contours(self,frame):
        cnts = cv2.findContours(frame, cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
 
        self.text_guess = 'Hmmmm'
        max_contour = 4000

        sketch_x = None
        sketch_y = None
        sketch_w = None
        sketch_h = None
        #loop through the contours, ignore them if they are too small
        for c in cnts:
            if cv2.contourArea(c) <self.settings.screen_width*self.settings.screen_width/250:
                continue
            #create and draw a bounding rectangle
            (x,y,w,h) = cv2.boundingRect(c)
            c_area = w*h
            if c_area > max_contour:
                sketch_x = x
                sketch_y = y
                sketch_w = w
                sketch_h = h

        contour_dimensions = [sketch_x, sketch_y, sketch_w, sketch_h]

        if contour_dimensions == [None, None, None, None]:
            pass
        else:
            return(contour_dimensions)

    




if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = SketchIt()
    game.run_game()