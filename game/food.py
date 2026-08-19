import pygame
import random


class Food:

    def __init__(self):

        self.size = 20

        self.position = self.generate_position()

        self.type = self.generate_type()

    def generate_position(self):

        x = random.randrange(
            40,
            760,
            20
        )

        y = random.randrange(
            80,
            560,
            20
        )

        return (x, y)

    def generate_type(self):

        number = random.randint(1, 10)

        if number <= 6:
            return "normal"

        elif number <= 9:
            return "bonus"

        else:
            return "golden"

    def respawn(self):

        self.position = self.generate_position()

        self.type = self.generate_type()

    def get_points(self):

        if self.type == "normal":

            return 10

        elif self.type == "bonus":

            return 25

        elif self.type == "golden":

            return 50

        return 0

    def get_color(self):

        if self.type == "normal":

            return (255, 60, 60)

        elif self.type == "bonus":

            return (80, 150, 255)

        elif self.type == "golden":

            return (255, 215, 0)

        return (255, 255, 255)

    def draw(self, screen):

        color = self.get_color()

        pygame.draw.rect(
            screen,
            color,
            (
                self.position[0],
                self.position[1],
                self.size,
                self.size
            )
        )