import pygame

from game.auth_screen import AuthScreen


pygame.init()

screen = pygame.display.set_mode(
    (800, 600)
)

pygame.display.set_caption(
    "Smart Snake - Login Test"
)

auth_screen = AuthScreen(screen)

user = auth_screen.run()

print("LOGIN RESULT:", user)

pygame.quit()