import pygame, random
from Constants import *

class Snake:
    # Constructor
    def __init__(self):
        # Initial length
        self.length = 1
        # positions = [x, y] -> x -> middle x , y -> middle
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]

        # left, right, up, down
        self.direction = random.choice(
            [DIRECTIONS["UP"], DIRECTIONS["DOWN"], DIRECTIONS["LEFT"], DIRECTIONS["RIGHT"]])
        # Choose the color of the snake
        self.color = COLORS["GREEN"]

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * BLOCK_SIZE)) % SCREEN_WIDTH),
               (cur[1] + (y * BLOCK_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice(
            [DIRECTIONS["UP"], DIRECTIONS["DOWN"], DIRECTIONS["LEFT"], DIRECTIONS["RIGHT"]])

    #[x, y] ->
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, COLORS["BLACK"], r, 1)
