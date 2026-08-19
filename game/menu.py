import pygame

from database.db import Database


class MainMenu:

    def __init__(self, screen):

        self.screen = screen

        self.width = screen.get_width()
        self.height = screen.get_height()

        self.running = True
        self.selected = 0

        self.options = [
            "START GAME",
            "LEADERBOARD",
            "ACHIEVEMENTS",
            "EXIT"
        ]

        # ==============================
        # FONTS
        # ==============================

        self.title_font = pygame.font.SysFont(
            "arial",
            55,
            bold=True
        )

        self.option_font = pygame.font.SysFont(
            "arial",
            30,
            bold=True
        )

        self.text_font = pygame.font.SysFont(
            "arial",
            22
        )

        self.small_font = pygame.font.SysFont(
            "arial",
            18
        )


    # ==========================================
    # MAIN MENU EVENTS
    # ==========================================

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.running = False

                return "EXIT"


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:

                    self.selected -= 1

                    if self.selected < 0:

                        self.selected = (
                            len(self.options) - 1
                        )


                elif event.key == pygame.K_DOWN:

                    self.selected += 1

                    if self.selected >= len(
                        self.options
                    ):

                        self.selected = 0


                elif event.key == pygame.K_RETURN:

                    return self.options[
                        self.selected
                    ]


        return None


    # ==========================================
    # DRAW MAIN MENU
    # ==========================================

    def draw(self):

        self.screen.fill(
            (15, 20, 30)
        )


        # Title
        title = self.title_font.render(
            "SMART SNAKE",
            True,
            (100, 255, 120)
        )

        title_rect = title.get_rect(
            center=(
                self.width // 2,
                80
            )
        )

        self.screen.blit(
            title,
            title_rect
        )


        # Subtitle
        subtitle = self.text_font.render(
            "Play • Compete • Achieve",
            True,
            (180, 180, 190)
        )

        subtitle_rect = subtitle.get_rect(
            center=(
                self.width // 2,
                130
            )
        )

        self.screen.blit(
            subtitle,
            subtitle_rect
        )


        # Menu options
        start_y = 210

        for index, option in enumerate(
            self.options
        ):

            if index == self.selected:

                text = self.option_font.render(
                    "> " + option + " <",
                    True,
                    (255, 215, 0)
                )

            else:

                text = self.option_font.render(
                    option,
                    True,
                    (240, 240, 240)
                )


            rect = text.get_rect(
                center=(
                    self.width // 2,
                    start_y + index * 65
                )
            )

            self.screen.blit(
                text,
                rect
            )


        # Controls
        controls = self.small_font.render(
            "UP / DOWN = Select     ENTER = Open",
            True,
            (150, 150, 160)
        )

        controls_rect = controls.get_rect(
            center=(
                self.width // 2,
                550
            )
        )

        self.screen.blit(
            controls,
            controls_rect
        )


        pygame.display.flip()


    # ==========================================
    # LEADERBOARD SCREEN
    # ==========================================

    def show_leaderboard(self):

        database = Database()

        games = database.get_all_games()

        clock = pygame.time.Clock()

        while True:

            # ------------------------------
            # EVENTS
            # ------------------------------

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    return "EXIT"


                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:

                        return "MENU"


            # ------------------------------
            # BACKGROUND
            # ------------------------------

            self.screen.fill(
                (15, 20, 30)
            )


            # ------------------------------
            # TITLE
            # ------------------------------

            title = self.title_font.render(
                "LEADERBOARD",
                True,
                (255, 215, 0)
            )

            title_rect = title.get_rect(
                center=(
                    self.width // 2,
                    60
                )
            )

            self.screen.blit(
                title,
                title_rect
            )


            # ------------------------------
            # HEADER
            # ------------------------------

            header = self.text_font.render(
                "RANK       PLAYER              SCORE",
                True,
                (100, 255, 120)
            )

            self.screen.blit(
                header,
                (150, 120)
            )


            # ------------------------------
            # DATA
            # ------------------------------

            if not games:

                no_data = self.text_font.render(
                    "No games played yet.",
                    True,
                    (220, 220, 220)
                )

                rect = no_data.get_rect(
                    center=(
                        self.width // 2,
                        250
                    )
                )

                self.screen.blit(
                    no_data,
                    rect
                )


            else:

                # Top 10 scores
                for index, game_data in enumerate(
                    games[:10],
                    start=1
                ):

                    player_name = str(
                        game_data[1]
                    )

                    score = game_data[2]


                    # Medal
                    if index == 1:

                        rank_text = "1"

                        rank_color = (
                            255,
                            215,
                            0
                        )

                    elif index == 2:

                        rank_text = "2"

                        rank_color = (
                            200,
                            200,
                            200
                        )

                    elif index == 3:

                        rank_text = "3"

                        rank_color = (
                            205,
                            127,
                            50
                        )

                    else:

                        rank_text = str(index)

                        rank_color = (
                            230,
                            230,
                            230
                        )


                    rank = self.text_font.render(
                        rank_text,
                        True,
                        rank_color
                    )

                    name = self.text_font.render(
                        player_name,
                        True,
                        (240, 240, 240)
                    )

                    score_text = self.text_font.render(
                        str(score),
                        True,
                        (100, 255, 120)
                    )


                    y = 165 + (
                        index - 1
                    ) * 38


                    self.screen.blit(
                        rank,
                        (170, y)
                    )

                    self.screen.blit(
                        name,
                        (260, y)
                    )

                    self.screen.blit(
                        score_text,
                        (550, y)
                    )


            # ------------------------------
            # BACK
            # ------------------------------

            back = self.small_font.render(
                "Press ESC to return to menu",
                True,
                (160, 160, 170)
            )

            back_rect = back.get_rect(
                center=(
                    self.width // 2,
                    560
                )
            )

            self.screen.blit(
                back,
                back_rect
            )


            pygame.display.flip()

            clock.tick(30)


    # ==========================================
    # ACHIEVEMENTS SCREEN
    # ==========================================

    def show_achievements(
        self,
        player_name
    ):

        database = Database()

        games = database.get_all_games()

        # Player ke games
        player_games = []

        for game in games:

            if game[1] == player_name:

                player_games.append(game)


        # ------------------------------
        # PLAYER STATS
        # ------------------------------

        total_games = len(
            player_games
        )

        best_score = 0

        total_score = 0

        longest_snake = 0


        for game in player_games:

            score = game[2]

            length = game[3]


            if score > best_score:

                best_score = score


            total_score += score


            if length > longest_snake:

                longest_snake = length


        clock = pygame.time.Clock()


        while True:

            # ------------------------------
            # EVENTS
            # ------------------------------

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    return "EXIT"


                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:

                        return "MENU"


            # ------------------------------
            # BACKGROUND
            # ------------------------------

            self.screen.fill(
                (15, 20, 30)
            )


            # ------------------------------
            # TITLE
            # ------------------------------

            title = self.title_font.render(
                "ACHIEVEMENTS",
                True,
                (255, 215, 0)
            )

            title_rect = title.get_rect(
                center=(
                    self.width // 2,
                    55
                )
            )

            self.screen.blit(
                title,
                title_rect
            )


            # Player name
            player_text = self.text_font.render(
                f"Player: {player_name}",
                True,
                (100, 255, 120)
            )

            player_rect = player_text.get_rect(
                center=(
                    self.width // 2,
                    105
                )
            )

            self.screen.blit(
                player_text,
                player_rect
            )


            # ------------------------------
            # ACHIEVEMENTS
            # ------------------------------

            achievements = []


            # First Game
            if total_games >= 1:

                achievements.append(
                    (
                        "FIRST GAME",
                        "You completed your first game!"
                    )
                )


            # Score 50
            if best_score >= 50:

                achievements.append(
                    (
                        "SCORE MASTER",
                        "You reached a score of 50+!"
                    )
                )


            # Score 100
            if best_score >= 100:

                achievements.append(
                    (
                        "SCORE LEGEND",
                        "You reached a score of 100+!"
                    )
                )


            # Snake length
            if longest_snake >= 10:

                achievements.append(
                    (
                        "SNAKE GROWER",
                        "Your snake reached length 10+!"
                    )
                )


            # Games
            if total_games >= 5:

                achievements.append(
                    (
                        "REGULAR PLAYER",
                        "You played 5+ games!"
                    )
                )


            # No achievements
            if not achievements:

                message = self.text_font.render(
                    "No achievements unlocked yet.",
                    True,
                    (220, 220, 220)
                )

                message_rect = message.get_rect(
                    center=(
                        self.width // 2,
                        230
                    )
                )

                self.screen.blit(
                    message,
                    message_rect
                )


            else:

                # Draw achievements
                for index, achievement in enumerate(
                    achievements
                ):

                    title_text = achievement[0]

                    description = achievement[1]


                    y = 160 + (
                        index * 65
                    )


                    # Achievement box
                    box = pygame.Rect(
                        120,
                        y,
                        560,
                        52
                    )

                    pygame.draw.rect(
                        self.screen,
                        (30, 40, 55),
                        box
                    )


                    # Achievement title
                    achievement_title = (
                        self.text_font.render(
                            "★ " + title_text,
                            True,
                            (255, 215, 0)
                        )
                    )

                    self.screen.blit(
                        achievement_title,
                        (140, y + 5)
                    )


                    # Description
                    description_text = (
                        self.small_font.render(
                            description,
                            True,
                            (210, 210, 210)
                        )
                    )

                    self.screen.blit(
                        description_text,
                        (140, y + 30)
                    )


            # ------------------------------
            # PLAYER STATISTICS
            # ------------------------------

            stats_y = 500

            stats = self.small_font.render(
                f"Games: {total_games}   "
                f"Best Score: {best_score}   "
                f"Longest Snake: {longest_snake}",
                True,
                (180, 180, 190)
            )

            stats_rect = stats.get_rect(
                center=(
                    self.width // 2,
                    stats_y
                )
            )

            self.screen.blit(
                stats,
                stats_rect
            )


            # ------------------------------
            # BACK
            # ------------------------------

            back = self.small_font.render(
                "Press ESC to return to menu",
                True,
                (150, 150, 160)
            )

            back_rect = back.get_rect(
                center=(
                    self.width // 2,
                    550
                )
            )

            self.screen.blit(
                back,
                back_rect
            )


            pygame.display.flip()

            clock.tick(30)


    # ==========================================
    # RUN MENU
    # ==========================================

    def run(self):

        clock = pygame.time.Clock()

        while self.running:

            result = self.handle_events()

            if result is not None:

                return result


            self.draw()

            clock.tick(60)


        return "EXIT"