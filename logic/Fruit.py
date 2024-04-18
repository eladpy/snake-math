from Constants import *
import pygame, random


class Fruit:
    def __init__(self):
        # Tuple that is responsible for the location
        self.position = (0, 0)
        self.color = COLORS["RED"]
        self.randomize_position()

    def randomize_position(self):
        self.position = (
        random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
        random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE, BLOCK_SIZE)))
        pygame.draw.rect(surface, COLORS["BLACK"],
                         pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE, BLOCK_SIZE)), 1)
