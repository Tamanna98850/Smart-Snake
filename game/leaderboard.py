import sqlite3
import pygame


class Leaderboard:

    def __init__(self, db_name="game_history.db"):

        self.db_name = db_name

        self.width = 800
        self.height = 600

        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )

        pygame.display.set_caption(
            "SmartSnake - Leaderboard"
        )

        self.clock = pygame.time.Clock()

        self.running = True

    # ==========================================
    # GET LEADERBOARD DATA
    # ==========================================

    def get_leaderboard(self):

        connection = sqlite3.connect(
            self.db_name
        )

        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                player_name,
                MAX(score) AS best_score
            FROM game_history
            GROUP BY player_name
            ORDER BY best_score DESC
            LIMIT 10
        """)

        data = cursor.fetchall()

        connection.close()

        return data

    # ==========================================
    # HANDLE EVENTS
    # ==========================================

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    self.running = False

    # ==========================================
    # DRAW LEADERBOARD
    # ==========================================

    def draw(self):

        self.screen.fill(
            (15, 15, 25)
        )

        # ==================================
        # FONTS
        # ==================================

        title_font = pygame.font.Font(
            None,
            55
        )

        header_font = pygame.font.Font(
            None,
            30
        )

        player_font = pygame.font.Font(
            None,
            28
        )

        small_font = pygame.font.Font(
            None,
            24
        )

        # ==================================
        # TITLE
        # ==================================

        title = title_font.render(
            "SMART SNAKE",
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

        # ==================================
        # SUBTITLE
        # ==================================

        subtitle = header_font.render(
            "LEADERBOARD",
            True,
            (255, 255, 255)
        )

        subtitle_rect = subtitle.get_rect(
            center=(
                self.width // 2,
                110
            )
        )

        self.screen.blit(
            subtitle,
            subtitle_rect
        )

        # ==================================
        # TABLE HEADER
        # ==================================

        rank_header = header_font.render(
            "Rank",
            True,
            (180, 180, 180)
        )

        player_header = header_font.render(
            "Player",
            True,
            (180, 180, 180)
        )

        score_header = header_font.render(
            "Best Score",
            True,
            (180, 180, 180)
        )

        self.screen.blit(
            rank_header,
            (120, 160)
        )

        self.screen.blit(
            player_header,
            (300, 160)
        )

        self.screen.blit(
            score_header,
            (550, 160)
        )

        # ==================================
        # LINE
        # ==================================

        pygame.draw.line(
            self.screen,
            (100, 100, 100),
            (100, 195),
            (700, 195),
            2
        )

        # ==================================
        # GET DATA
        # ==================================

        leaderboard = self.get_leaderboard()

        # ==================================
        # NO DATA
        # ==================================

        if not leaderboard:

            empty_text = player_font.render(
                "No games played yet.",
                True,
                (255, 255, 255)
            )

            empty_rect = empty_text.get_rect(
                center=(
                    self.width // 2,
                    280
                )
            )

            self.screen.blit(
                empty_text,
                empty_rect
            )

        # ==================================
        # DISPLAY DATA
        # ==================================

        else:

            y = 215

            for index, row in enumerate(
                leaderboard
            ):

                player_name = row[0]

                score = row[1]

                rank = index + 1

                # ==================================
                # RANK COLOR
                # ==================================

                if rank == 1:

                    rank_text = "1st"

                    text_color = (
                        255,
                        215,
                        0
                    )

                elif rank == 2:

                    rank_text = "2nd"

                    text_color = (
                        200,
                        200,
                        200
                    )

                elif rank == 3:

                    rank_text = "3rd"

                    text_color = (
                        205,
                        127,
                        50
                    )

                else:

                    rank_text = str(
                        rank
                    )

                    text_color = (
                        255,
                        255,
                        255
                    )

                # ==================================
                # RANK
                # ==================================

                rank_surface = (
                    player_font.render(
                        rank_text,
                        True,
                        text_color
                    )
                )

                self.screen.blit(
                    rank_surface,
                    (125, y)
                )

                # ==================================
                # PLAYER
                # ==================================

                player_surface = (
                    player_font.render(
                        str(player_name),
                        True,
                        text_color
                    )
                )

                self.screen.blit(
                    player_surface,
                    (300, y)
                )

                # ==================================
                # SCORE
                # ==================================

                score_surface = (
                    player_font.render(
                        str(score),
                        True,
                        text_color
                    )
                )

                self.screen.blit(
                    score_surface,
                    (570, y)
                )

                y += 38

        # ==================================
        # FOOTER
        # ==================================

        footer = small_font.render(
            "Press ESC to return",
            True,
            (160, 160, 160)
        )

        footer_rect = footer.get_rect(
            center=(
                self.width // 2,
                550
            )
        )

        self.screen.blit(
            footer,
            footer_rect
        )

        pygame.display.flip()

    # ==========================================
    # RUN LEADERBOARD
    # ==========================================

    def run(self):

        self.running = True

        while self.running:

            self.handle_events()

            self.draw()

            self.clock.tick(30)