import pygame


class GameWindow:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.color = ai_game.settings.game_window_color
        game_window_width = int(ai_game.settings.screen_width / 5 * 3)
        game_window_height = ai_game.settings.screen_height
        self.rect = pygame.Rect(
            int(ai_game.settings.screen_width / 20),
            0,
            game_window_width,
            game_window_height
        )
        self.center = (
            int(ai_game.settings.screen_width / 20) + int(ai_game.settings.screen_width / 5 * 3) / 2,
            ai_game.settings.screen_height / 2
        )
        ai_game.settings.segment_width = game_window_width / 10
        ai_game.settings.segment_height = game_window_height / 20


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class NextWindow:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.color = ai_game.settings.game_window_color
        self.rect = pygame.Rect(
            int(ai_game.settings.screen_width / 30 * 21),
            int(ai_game.settings.screen_height / 40 * 29),
            int(ai_game.settings.screen_width / 40 * 10),
            int(ai_game.settings.screen_height / 40 * 10)
        )

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
