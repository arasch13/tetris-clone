GB_BACKRGROUND_COLOR = (236, 245, 219)

class Settings:

    def __init__(self):
        """Initialize game settings"""
        ## static settings
        # fps settings
        self.fps = 60
        # screen settings
        self.screen_mode = 'window'  # 'window' or 'fullscreen'
        self.window_screen_width = 800
        self.window_screen_height = 800
        self.bg_color = (50, 50, 50)
        self.game_window_color = GB_BACKRGROUND_COLOR
        self.block_pause = 1000 # ms
        # object settings
        # self.bullet_width_factor = 0.005
        # self.bullet_height_factor = 0.02
        # self.bullet_color = (230, 230, 230)
        # self.bullets_allowed = 3
        # game settings
        # self.speedup_scale = 1.5
        # self.ship_limit = 3
        ## dynamic settings
        # self.initialize_dynamic_settings()