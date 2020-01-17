import cv2

class SketchIt:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        #initialize video capture
        #self.video = cv2.VideoCapture(0)

    def run_game(self):
        """Start the main loop for the game."""
        video = cv2.VideoCapture(0)
        while True:
            ret, frame = video.read()
            cv2.imshow("CAN YOU DRAW",frame)
            key = cv2.waitKey(1)
            if key == ord("q"):
                break


if __name__ == '__main__':
	# Make a game instance, and run the game.
	game = SketchIt()
	game.run_game()
