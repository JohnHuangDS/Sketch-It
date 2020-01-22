class Settings:
    """A class to store all settings for Sketch It."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen settings
        self.screen_width = 1080
        self.font_size = int(self.screen_width/400)
        self.font_color = (0,0,0)
        self.font_y_pad = int(self.screen_width/10)

        #padding for image crop 
        self.model_preprocessing_padding = int(self.screen_width/20)

        #minimum size for obejct detection
        self.minimum_contour_area = (self.screen_width**2)/50

        #Level settings
        self.level_responses = {1: ['wine glass','Thats a wine glass alright. Press (n) to continue'],
            2: ['sword','ZING ZING, thats a sword! Press (n) to continue'],
            3: ['angel','What a beautiful Angel. Press (n) to continue'],
            4: ['yoga','Nice! Thats all, thanks for playing! Press (n) to restart']
            }

        self.total_levels = 4

        #trained categories from cnn training
        self.categories = ['angel','sword','wine glass','yoga']


        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change through the game."""
        self.current_level = 1
        self.object_detection = "No drawing has been detected"
        self.response = None
        self.win_screen = False

    def object_detected(self):
        self.object_detection = "Drawing detected"

    def object_undetected(self):
        self.object_detection = "No drawing has been detected"

    def level_passed(self):
        self.current_level += 1

    def correct_drawing_response(self, current_level):
        self.response = self.level_responses[current_level][1]

    def reset_response(self):
        self.response = None

    def reset_game(self):
        self.current_level = 1
