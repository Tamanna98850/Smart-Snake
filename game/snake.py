import pygame


class Snake:

    def __init__(self):

        self.size = 20

        self.body = [
            (300, 300),
            (280, 300),
            (260, 300)
        ]

        self.direction = "RIGHT"

    def move(self):

        head_x, head_y = self.body[0]

        if self.direction == "RIGHT":
            head_x += self.size

        elif self.direction == "LEFT":
            head_x -= self.size

        elif self.direction == "UP":
            head_y -= self.size

        elif self.direction == "DOWN":
            head_y += self.size

        new_head = (head_x, head_y)

        self.body.insert(0, new_head)

        self.body.pop()

    def change_direction(self, new_direction):

        if new_direction == "UP":

            if self.direction != "DOWN":
                self.direction = "UP"

        elif new_direction == "DOWN":

            if self.direction != "UP":
                self.direction = "DOWN"

        elif new_direction == "LEFT":

            if self.direction != "RIGHT":
                self.direction = "LEFT"

        elif new_direction == "RIGHT":

            if self.direction != "LEFT":
                self.direction = "RIGHT"

    def grow(self):

        tail = self.body[-1]

        self.body.append(tail)

    def check_wall_collision(self, width, height):

        head_x, head_y = self.body[0]

        if head_x < 0:
            return True

        if head_x >= width:
            return True

        if head_y < 0:
            return True

        if head_y >= height:
            return True

        return False

    def check_self_collision(self):

        head = self.body[0]

        body = self.body[1:]

        if head in body:
            return True

        return False

    def draw(self, screen):

        for index, segment in enumerate(self.body):

            if index == 0:
                color = (0, 255, 100)
            else:
                color = (0, 180, 80)

            pygame.draw.rect(
                screen,
                color,
                (
                    segment[0],
                    segment[1],
                    self.size,
                    self.size
                )
            )