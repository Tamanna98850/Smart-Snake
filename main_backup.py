import pygame

from game.game import Game
from game.menu import MainMenu
from game.player import Player


# ==========================================
# INITIALIZE PYGAME
# ==========================================

pygame.init()


# ==========================================
# SCREEN
# ==========================================

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Smart Snake"
)


# ==========================================
# GET PLAYER NAME
# ==========================================

player_name = input(
    "Enter your name: "
)


# ==========================================
# CREATE PLAYER
# ==========================================

player = Player(
    player_name
)


# ==========================================
# MAIN APPLICATION
# ==========================================

while True:

    # ======================================
    # CREATE MENU
    # ======================================

    menu = MainMenu(
        screen
    )


    # ======================================
    # SHOW MENU
    # ======================================

    choice = menu.run()


    # ======================================
    # START GAME
    # ======================================

    if choice == "START GAME":

        game = Game(
            player
        )

        game.run()


    # ======================================
    # LEADERBOARD
    # ======================================

    elif choice == "LEADERBOARD":

        print("\n")
        print("=" * 50)
        print("          🏆 LEADERBOARD")
        print("=" * 50)

        from database.db import Database

        database = Database()

        games = database.get_all_games()

        if not games:

            print("No games played yet.")

        else:

            for index, game_data in enumerate(
                games[:10],
                start=1
            ):

                print(
                    f"{index}. "
                    f"{game_data[1]} "
                    f"- Score: {game_data[2]}"
                )

        print("=" * 50)

        input(
            "\nPress ENTER to return to menu..."
        )


    # ======================================
    # ACHIEVEMENTS
    # ======================================

    elif choice == "ACHIEVEMENTS":

        print("\n")
        print("=" * 50)
        print("          🏆 ACHIEVEMENTS")
        print("=" * 50)

        from database.db import Database

        database = Database()

        achievements = (
            database.get_player_achievements(
                player.name
            )
        )

        if not achievements:

            print(
                "No achievements unlocked yet."
            )

        else:

            for achievement in achievements:

                print(
                    f"\n🏆 {achievement[0]}"
                )

                print(
                    f"   {achievement[1]}"
                )

                print(
                    f"   Score: {achievement[2]}"
                )

        print("=" * 50)

        input(
            "\nPress ENTER to return to menu..."
        )


    # ======================================
    # EXIT
    # ======================================

    elif choice == "EXIT":

        break


# ==========================================
# QUIT
# ==========================================

pygame.quit()