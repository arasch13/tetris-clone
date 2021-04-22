import pygame
import random

BLOCK_TYPES = ["l", "z", "z_reverse", "w", "o"]

class Segment:
    def __init__(self,ai_game, x_pos, y_pos):
        self.screen = ai_game.screen
        self.width = ai_game.settings.segment_width
        self.height = ai_game.settings.segment_height
        self.color = (0, 0, 0)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = pygame.Rect(
            self.x_pos,
            self.y_pos,
            self.width,
            self.height
        )

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Block:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.x_start = int(ai_game.settings.screen_width / 20)
        self.x_step_size = ai_game.settings.segment_width
        self.y_step_size = ai_game.settings.segment_height
        self.segments = self.create_random()
        self.speed = 0
        self.counter = 0

    def draw(self):
        for segment in self.segments:
            segment.draw()

    def create_random(self):
        segments = []

        type = random.choice(BLOCK_TYPES)
        if type == "l":
            center_segment = Segment(self.ai_game, self.x_start + 4 * self.x_step_size, 0)
            segment2 = Segment(self.ai_game, center_segment.x_pos - self.x_step_size, 0)
            segment3 = Segment(self.ai_game, center_segment.x_pos + self.x_step_size, 0)
            segment4 = Segment(self.ai_game, center_segment.x_pos + 2 * self.x_step_size, 0)
        elif type == "z":
            center_segment = Segment(self.ai_game, self.x_start + 4 * self.x_step_size, 0)
            segment2 = Segment(self.ai_game, center_segment.x_pos - self.x_step_size, 0)
            segment3 = Segment(self.ai_game, center_segment.x_pos, center_segment.y_pos + self.y_step_size)
            segment4 = Segment(self.ai_game, center_segment.x_pos + self.x_step_size, center_segment.y_pos + self.y_step_size)

        elif type == "z_reverse":
            center_segment = Segment(self.ai_game, self.x_start + 4 * self.x_step_size, 0)
            segment2 = Segment(self.ai_game, center_segment.x_pos + self.x_step_size, 0)
            segment3 = Segment(self.ai_game, center_segment.x_pos, center_segment.y_pos + self.y_step_size)
            segment4 = Segment(self.ai_game, center_segment.x_pos - self.x_step_size,
                               center_segment.y_pos + self.y_step_size)

        elif type == "w":
            center_segment = Segment(self.ai_game, self.x_start + 4 * self.x_step_size, 0)
            segment2 = Segment(self.ai_game, center_segment.x_pos, center_segment.y_pos + self.y_step_size)
            segment3 = Segment(self.ai_game, center_segment.x_pos + self.x_step_size,
                               center_segment.y_pos + self.y_step_size)
            segment4 = Segment(self.ai_game, center_segment.x_pos - self.x_step_size,
                               center_segment.y_pos + self.y_step_size)

        elif type == "o":
            center_segment = Segment(self.ai_game, self.x_start + 4 * self.x_step_size, 0)
            segment2 = Segment(self.ai_game, center_segment.x_pos, center_segment.y_pos + self.y_step_size)
            segment3 = Segment(self.ai_game, center_segment.x_pos + self.x_step_size,
                               center_segment.y_pos)
            segment4 = Segment(self.ai_game, center_segment.x_pos + self.x_step_size,
                               center_segment.y_pos + self.y_step_size)

        segments.append(center_segment)
        segments.append(segment2)
        segments.append(segment3)
        segments.append(segment4)
        return segments

    def move(self, dt):
        self.counter += dt
        if self.counter >= self.ai_game.settings.block_pause:
            for segment in self.segments:
                segment.rect.y += self.y_step_size
            self.counter = 0


