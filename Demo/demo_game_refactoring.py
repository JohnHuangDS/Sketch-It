import cv2
from settings import Settings
class SketchIt:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""

        #attributes
        self.settings = Settings()
        self.background_processed = None

    #method
    def run_game(self):
        """Start the main loop for the game."""
        #start video capture
        video = cv2.VideoCapture(0)
        while True:
            #
            ret, frame = video.read()

            frame = self._start_screen(frame)
            #show frame
            cv2.imshow("CAN YOU DRAW",frame)

            #for testing functions
            print(self.background_processed)

            key = cv2.waitKey(1)

            if key == ord("c"):
                self.background_processed = self._calibrate_background()

            if key == ord("q"):
                break

    #helper method
    def _start_screen(self, frame):

        cv2.putText(frame, "Welcome to 'Can you draw?''",(10, self.settings.font_y_pad),
                cv2.FONT_HERSHEY_SIMPLEX, self.settings.font, self.settings.font_color, 2)

        cv2.putText(frame, "Press (s) to start",(10,frame.shape[0]-2*self.settings.font_y_pad),
                cv2.FONT_HERSHEY_SIMPLEX, self.settings.font, self.settings.font_color, 2)

        cv2.putText(frame, "Press (c) to calibrate background",(10,frame.shape[0]-self.settings.font_y_pad),
                cv2.FONT_HERSHEY_SIMPLEX, self.settings.font, self.settings.font_color, 2)

        return (frame)



    #helper method
    def _calibrate_background(self):
        cam = cv2.VideoCapture(0)
        background = None
        while True:
            ret, background = cam.read()

            cv2.putText(background, 'Calibrating Background',(10,self.settings.font_y_pad),
                cv2.FONT_HERSHEY_SIMPLEX, self.settings.font, (0, 0, 0), 2)

            cv2.putText(background, 'Press (y) to Continue',(10,background.shape[0]-self.settings.font_y_pad),
                cv2.FONT_HERSHEY_SIMPLEX, self.settings.font, (0, 0, 0), 2)

            cv2.imshow("CAN YOU DRAW",background)

            key = cv2.waitKey(1)

            if key == ord("y"):
                break
                
        background_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
        background_gray_blur = cv2.GaussianBlur(background_gray, (5,5),0)
        background_proccessed = background_gray_blur
        cam.release()
        cv2.destroyAllWindows
        return(background_proccessed)


if __name__ == '__main__':
	# Make a game instance, and run the game.
	game = SketchIt()
	game.run_game()