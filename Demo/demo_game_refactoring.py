import cv2
import sys

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
        self.levels = Levels()
        self.cam = cv2.VideoCapture(0)
        self.display = Display()
        self.imgprocessor = ImgProcessor()

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
            self._start_level(self.cam)

        #q = exit game key 
        if key == ord("q"):
            sys.exit()


    #helper method
    def _calibrate_background(self,cam):
        """Calibrates background to acccount for difference in lighting"""

        while True:
    
            #read frame from camera feed
            ret, frame = cam.read()

            #display calibration feed
            self.display.calibration_screen(frame)

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

    def _start_level(self, cam):
        """Starts the current level"""
        self.levels.play_level(cam)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = SketchIt()
    game.run_game()