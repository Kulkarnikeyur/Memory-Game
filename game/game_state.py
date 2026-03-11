class GameState:

    def __init__(self, back_image):

        self.open_images = []
        self.open_buttons = []
        self.matched_buttons = []

        self.moves = 0
        self.player_name = ""

        self.back_image = back_image

        # time tracking
        self.start_time = None
        self.end_time = None