import numpy as np
from settings import Settings
import cv2
from display_screen import Display


class Levels:
    """A class to store all levels for Sketch It."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.answers = {1: ['wine glass','Thats a wine glass alright.'],
            2: ['sword','ZING ZING, thats a sword!'],
            3: ['angel','What a beautiful Angel'],
            4: ['yoga','Nice! Thats its, thanks for playing!']
            }

        self.settings = Settings()
        self.display_screen = Display()


    def play_level(self, cam):
        """Display the current level on the screen"""

        #Set the object to be drawn
        draw_object = self.answers[self.settings.current_level]

        #print the correct answer
        print(draw_object[0])

        while True:

            ret, frame = cam.read()
            






            
            self.display_screen.level_screen(frame, draw_object)
            
            key = cv2.waitKey(1)

            if key == ord("q"):
                sys.exit()





