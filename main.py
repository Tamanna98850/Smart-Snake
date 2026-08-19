import pygame

from game.game import Game
from game.player import Player
from game.leaderboard import Leaderboard
from database.analytics.dashboard import Dashboard


# =========================================================
# PYGAME
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

name_font = pygame.font.Font(
    None,
    40
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
# NAME SCREEN
# =========================================================

def get_player_name():

    name = ""

    entering = True

    pygame.key.start_text_input()

    while entering:

        for event in pygame.event.get():

            # ---------------------------------------------
            # CLOSE
            # ---------------------------------------------

            if event.type == pygame.QUIT:

                pygame.key.stop_text_input()

                return None


            # ---------------------------------------------
            # TEXT INPUT
            # ---------------------------------------------

            elif event.type == pygame.TEXTINPUT:

                if len(name) < 20:

                    name += event.text


            # ---------------------------------------------
            # KEYBOARD
            # ---------------------------------------------

            elif event.type == pygame.KEYDOWN:

                # ENTER
                if event.key == pygame.K_RETURN:

                    if name.strip() == "":

                        name = "Player"

                    entering = False


                # BACKSPACE
                elif event.key == pygame.K_BACKSPACE:

                    name = name[:-1]


                # ESC
                elif event.key == pygame.K_ESCAPE:

                    pygame.key.stop_text_input()

                    return None


        # ---------------------------------------------
        # BACKGROUND
        # ---------------------------------------------

        screen.fill(
            (15, 15, 25)
        )


        # ---------------------------------------------
        # TITLE
        # ---------------------------------------------

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
                    120
                )
            )
        )


        # ---------------------------------------------
        # HEADING
        # ---------------------------------------------

        heading = name_font.render(
            "ENTER YOUR NAME",
            True,
            (255, 255, 255)
        )

        screen.blit(
            heading,
            heading.get_rect(
                center=(
                    WIDTH // 2,
                    250
                )
            )
        )


        # ---------------------------------------------
        # NAME BOX
        # ---------------------------------------------

        box = pygame.Rect(
            200,
            310,
            400,
            60
        )

        pygame.draw.rect(
            screen,
            (40, 40, 55),
            box
        )

        pygame.draw.rect(
            screen,
            (255, 215, 0),
            box,
            2
        )


        # ---------------------------------------------
        # NAME
        # ---------------------------------------------

        display_name = (
            name
            if name
            else
            "Type your name..."
        )

        text_color = (
            (255, 255, 255)
            if name
            else
            (120, 120, 120)
        )

        name_text = name_font.render(
            display_name,
            True,
            text_color
        )

        screen.blit(
            name_text,
            name_text.get_rect(
                midleft=(
                    box.left + 15,
                    box.centery
                )
            )
        )


        # ---------------------------------------------
        # INSTRUCTION
        # ---------------------------------------------

        instruction = small_font.render(
            "Type your name and press ENTER",
            True,
            (170, 170, 170)
        )

        screen.blit(
            instruction,
            instruction.get_rect(
                center=(
                    WIDTH // 2,
                    420
                )
            )
        )


        # ---------------------------------------------
        # UPDATE
        # ---------------------------------------------

        pygame.display.flip()

    pygame.key.stop_text_input()

    return name.strip()


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

    choice = menu_options[index]


    # =====================================================
    # START GAME
    # =====================================================

    if choice == "START GAME":

        pygame.event.clear()

        player_name = get_player_name()

        if player_name is None:

            return

        player = Player(
            player_name
        )

        game = Game(
            player
        )

        game.run()

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
# MAIN LOOP
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

            # UP
            if event.key == pygame.K_UP:

                selected_option -= 1

                if selected_option < 0:

                    selected_option = (
                        len(menu_options) - 1
                    )


            # DOWN
            elif event.key == pygame.K_DOWN:

                selected_option += 1

                if selected_option >= len(
                    menu_options
                ):

                    selected_option = 0


            # ENTER
            elif event.key == pygame.K_RETURN:

                open_menu(
                    selected_option
                )


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
                100
            )
        )
    )


    # =====================================================
    # MENU OPTIONS
    # =====================================================

    start_y = 210


    for index, option in enumerate(
        menu_options
    ):

        # -------------------------------------------------
        # SELECTED
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
        # RENDER
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
    # HELP
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