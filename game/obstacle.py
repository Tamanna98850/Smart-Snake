import pygame
import random


class Obstacle:

    def __init__(self, width, height):

        self.size = 20

        self.position = self.generate_position(
            width,
            height
        )

    def generate_position(self, width, height):

        x = random.randrange(
            40,
            width - 40,
            20
        )

        y = random.randrange(
            80,
            height - 40,
            20
        )

        return (x, y)

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (120, 120, 120),
            (
                self.position[0],
                self.position[1],
                self.size,
                self.size
            )
        )