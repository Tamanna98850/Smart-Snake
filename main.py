import pygame

from game.game import Game
from game.player import Player
from game.leaderboard import Leaderboard
from database.analytics.dashboard import Dashboard
from game.auth_screen import AuthScreen


# =========================================================
# PYGAME INITIALIZATION
# =========================================================

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "SmartSnake"
)


# =========================================================
# FONTS
# =========================================================

title_font = pygame.font.Font(
    None,
    70
)

menu_font = pygame.font.Font(
    None,
    35
)

small_font = pygame.font.Font(
    None,
    25
)

user_font = pygame.font.Font(
    None,
    24
)


# =========================================================
# MENU
# =========================================================

menu_options = [
    "START GAME",
    "LEADERBOARD",
    "STATISTICS",
    "EXIT"
]

selected_option = 0

running = True


# =========================================================
# CURRENT USER
# =========================================================

current_user = None

current_username = ""


# =========================================================
# RESTORE MENU
# =========================================================

def restore_menu():

    global screen

    pygame.init()

    screen = pygame.display.set_mode(
        (WIDTH, HEIGHT)
    )

    pygame.display.set_caption(
        "SmartSnake"
    )

    pygame.event.clear()


# =========================================================
# OPEN SELECTED MENU
# =========================================================

def open_menu(index):

    global running
    global current_username

    choice = menu_options[index]


    # =====================================================
    # START GAME
    # =====================================================

    if choice == "START GAME":

        pygame.event.clear()

        # Use logged-in username
        player_name = current_username

        if not player_name:

            print(
                "No user logged in."
            )

            return

        print(
            "Starting game for:",
            player_name
        )

        # Create player
        player = Player(
            player_name
        )

        # Create game
        game = Game(
            player
        )

        # Run game
        game.run()

        # Restore main menu
        restore_menu()


    # =====================================================
    # LEADERBOARD
    # =====================================================

    elif choice == "LEADERBOARD":

        pygame.event.clear()

        print(
            "Opening Leaderboard..."
        )

        leaderboard = Leaderboard()

        leaderboard.run()

        restore_menu()


    # =====================================================
    # STATISTICS
    # =====================================================

    elif choice == "STATISTICS":

        pygame.event.clear()

        print(
            "Opening Statistics..."
        )

        dashboard = Dashboard()

        dashboard.run()

        restore_menu()


    # =====================================================
    # EXIT
    # =====================================================

    elif choice == "EXIT":

        running = False


# =========================================================
# LOGIN / REGISTER
# =========================================================

auth_screen = AuthScreen(
    screen
)

current_user = auth_screen.run()


# =========================================================
# LOGIN CANCELLED
# =========================================================

if current_user is None:

    pygame.quit()

    raise SystemExit


# =========================================================
# GET LOGGED-IN USERNAME
# =========================================================

try:

    current_username = current_user[1]

except (TypeError, IndexError):

    current_username = str(
        current_user
    )


print(
    "================================"
)

print(
    "Login successful!"
)

print(
    "Logged in user:",
    current_username
)

print(
    "================================"
)


# Clear old login events
pygame.event.clear()


# =========================================================
# MAIN MENU LOOP
# =========================================================

while running:


    # =====================================================
    # EVENTS
    # =====================================================

    for event in pygame.event.get():


        # -------------------------------------------------
        # WINDOW CLOSE
        # -------------------------------------------------

        if event.type == pygame.QUIT:

            running = False

            continue


        # -------------------------------------------------
        # KEYBOARD
        # -------------------------------------------------

        if event.type == pygame.KEYDOWN:


            # ---------------------------------------------
            # UP
            # ---------------------------------------------

            if event.key == pygame.K_UP:

                selected_option -= 1

                if selected_option < 0:

                    selected_option = (
                        len(menu_options) - 1
                    )


            # ---------------------------------------------
            # DOWN
            # ---------------------------------------------

            elif event.key == pygame.K_DOWN:

                selected_option += 1

                if selected_option >= len(
                    menu_options
                ):

                    selected_option = 0


            # ---------------------------------------------
            # ENTER
            # ---------------------------------------------

            elif event.key == pygame.K_RETURN:

                open_menu(
                    selected_option
                )


            # ---------------------------------------------
            # ESC
            # ---------------------------------------------

            elif event.key == pygame.K_ESCAPE:

                # Exit application from main menu
                running = False


        # -------------------------------------------------
        # MOUSE CLICK
        # -------------------------------------------------

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_position = event.pos

                start_y = 210


                for index in range(
                    len(menu_options)
                ):

                    option_rect = pygame.Rect(
                        250,
                        start_y + index * 65 - 25,
                        300,
                        50
                    )


                    if option_rect.collidepoint(
                        mouse_position
                    ):

                        selected_option = index

                        open_menu(
                            index
                        )

                        break


        # -------------------------------------------------
        # MOUSE MOVE
        # -------------------------------------------------

        elif event.type == pygame.MOUSEMOTION:

            mouse_position = event.pos

            start_y = 210


            for index in range(
                len(menu_options)
            ):

                option_rect = pygame.Rect(
                    250,
                    start_y + index * 65 - 25,
                    300,
                    50
                )


                if option_rect.collidepoint(
                    mouse_position
                ):

                    selected_option = index


    # =====================================================
    # BACKGROUND
    # =====================================================

    screen.fill(
        (15, 15, 25)
    )


    # =====================================================
    # TITLE
    # =====================================================

    title = title_font.render(
        "SMART SNAKE",
        True,
        (255, 215, 0)
    )

    screen.blit(
        title,
        title.get_rect(
            center=(
                WIDTH // 2,
                90
            )
        )
    )


    # =====================================================
    # LOGGED-IN USER
    # =====================================================

    user_text = user_font.render(
        f"Welcome, {current_username}",
        True,
        (180, 180, 180)
    )

    screen.blit(
        user_text,
        user_text.get_rect(
            center=(
                WIDTH // 2,
                155
            )
        )
    )


    # =====================================================
    # MENU OPTIONS
    # =====================================================

    start_y = 220


    for index, option in enumerate(
        menu_options
    ):


        # -------------------------------------------------
        # SELECTED OPTION
        # -------------------------------------------------

        if index == selected_option:

            color = (
                255,
                215,
                0
            )

            text = (
                "> "
                + option
                + " <"
            )


        else:

            color = (
                255,
                255,
                255
            )

            text = option


        # -------------------------------------------------
        # RENDER OPTION
        # -------------------------------------------------

        option_text = menu_font.render(
            text,
            True,
            color
        )


        option_rect = option_text.get_rect(
            center=(
                WIDTH // 2,
                start_y + index * 65
            )
        )


        screen.blit(
            option_text,
            option_rect
        )


    # =====================================================
    # HELP TEXT
    # =====================================================

    help_text = small_font.render(
        "UP/DOWN = Select   ENTER / CLICK = Open",
        True,
        (160, 160, 160)
    )

    screen.blit(
        help_text,
        help_text.get_rect(
            center=(
                WIDTH // 2,
                500
            )
        )
    )


    # =====================================================
    # FOOTER
    # =====================================================

    footer = small_font.render(
        "Python + Pygame + SQLite + Pandas",
        True,
        (100, 100, 100)
    )

    screen.blit(
        footer,
        footer.get_rect(
            center=(
                WIDTH // 2,
                550
            )
        )
    )


    # =====================================================
    # DISPLAY
    # =====================================================

    pygame.display.flip()


# =========================================================
# FINAL QUIT
# =========================================================

pygame.quit()