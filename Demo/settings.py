class Settings:
    """A class to store all settings for Sketch It."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen settings
        self.screen_width = 1080
        self.font_size = int(self.screen_width/400)
        self.font_color = (0,0,0)
        self.font_y_pad = int(self.screen_width/10)

        # Level settings
        self.level_answers = {1: ['wine glass','Thats a wine glass alright.'],
            2: ['sword','ZING ZING, thats a sword!'],
            3: ['angel','What a beautiful Angel'],
            4: ['yoga','Nice! Thats its, thanks for playing!']
            }

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change through the game."""
        self.current_level = 1
        self.object_detection = "No drawing has been detected"
        self.guess = None

    def object_detected(self):
        self.object_detection = "Drawing detected"

    def level_passed(self):
        self.current_level += 1



