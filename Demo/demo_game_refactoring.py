import cv2

class SketchIt:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        #initialize video capture
        self.video = cv2.VideoCapture(1)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            ret, frame = self.video.read()
            cv2.imshow("CAN YOU DRAW",frame)

if __name__ == '__main__':
	# Make a game instance, and run the game.
	game = SketchIt()
	game.run_game()
