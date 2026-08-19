import random
import pygame


class PowerUp:

    # ==========================================
    # INITIALIZE
    # ==========================================

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.size = 20

        self.types = [
            "SPEED",
            "DOUBLE",
            "SHIELD"
        ]

        self.type = random.choice(
            self.types
        )

        self.position = (
            0,
            0
        )

        self.active = True

        self.generate_position()


    # ==========================================
    # GENERATE POSITION
    # ==========================================

    def generate_position(self):

        x = random.randrange(
            20,
            self.width - 20,
            20
        )

        y = random.randrange(
            20,
            self.height - 20,
            20
        )

        self.position = (
            x,
            y
        )

        return self.position


    # ==========================================
    # GENERATE NEW POWER-UP
    # ==========================================

    def respawn(self):

        self.type = random.choice(
            self.types
        )

        self.generate_position()

        self.active = True


    # ==========================================
    # GET SYMBOL
    # ==========================================

    def get_symbol(self):

        if self.type == "SPEED":

            return "⚡"

        elif self.type == "DOUBLE":

            return "⭐"

        elif self.type == "SHIELD":

            return "🛡"

        return "?"


    # ==========================================
    # DRAW POWER-UP
    # ==========================================

    def draw(self, screen):

        if not self.active:

            return

        x, y = self.position

        # Outer circle

        pygame.draw.circle(
            screen,
            (255, 215, 0),
            (
                x + 10,
                y + 10
            ),
            12
        )

        # Inner circle

        pygame.draw.circle(
            screen,
            (30, 30, 40),
            (
                x + 10,
                y + 10
            ),
            8
        )

        # Text

        font = pygame.font.Font(
            None,
            18
        )

        text = font.render(
            self.get_symbol(),
            True,
            (255, 255, 255)
        )

        text_rect = text.get_rect(
            center=(
                x + 10,
                y + 10
            )
        )

        screen.blit(
            text,
            text_rect
        )