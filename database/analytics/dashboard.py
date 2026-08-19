import sqlite3
import pygame


class Dashboard:

    def __init__(self, db_name="game_history.db"):

        self.db_name = db_name

        self.width = 800
        self.height = 600

        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )

        pygame.display.set_caption(
            "SmartSnake - Statistics"
        )

        self.clock = pygame.time.Clock()

        self.running = True

    # ==========================================
    # GET STATISTICS
    # ==========================================

    def get_statistics(self):

        connection = sqlite3.connect(
            self.db_name
        )

        cursor = connection.cursor()

        # Total games
        cursor.execute("""
            SELECT COUNT(*)
            FROM game_history
        """)

        total_games = cursor.fetchone()[0]

        # Total players
        cursor.execute("""
            SELECT COUNT(
                DISTINCT player_name
            )
            FROM game_history
        """)

        total_players = cursor.fetchone()[0]

        # Highest score
        cursor.execute("""
            SELECT MAX(score)
            FROM game_history
        """)

        highest_score = cursor.fetchone()[0]

        if highest_score is None:
            highest_score = 0

        # Average score
        cursor.execute("""
            SELECT AVG(score)
            FROM game_history
        """)

        average_score = cursor.fetchone()[0]

        if average_score is None:
            average_score = 0

        # Average snake length
        cursor.execute("""
            SELECT AVG(snake_length)
            FROM game_history
        """)

        average_length = cursor.fetchone()[0]

        if average_length is None:
            average_length = 0

        # Best player
        cursor.execute("""
            SELECT
                player_name,
                MAX(score) AS best_score
            FROM game_history
            GROUP BY player_name
            ORDER BY best_score DESC
            LIMIT 1
        """)

        best_player = cursor.fetchone()

        connection.close()

        if best_player is None:

            best_player_name = "No Player"

            best_player_score = 0

        else:

            best_player_name = best_player[0]

            best_player_score = best_player[1]

        return {

            "total_games": total_games,

            "total_players": total_players,

            "highest_score": highest_score,

            "average_score": average_score,

            "average_length": average_length,

            "best_player": best_player_name,

            "best_player_score": best_player_score

        }

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
    # DRAW DASHBOARD
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

        card_title_font = pygame.font.Font(
            None,
            25
        )

        value_font = pygame.font.Font(
            None,
            35
        )

        small_font = pygame.font.Font(
            None,
            22
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
                55
            )
        )

        self.screen.blit(
            title,
            title_rect
        )

        # ==================================
        # SUBTITLE
        # ==================================

        subtitle = card_title_font.render(
            "GAME STATISTICS",
            True,
            (255, 255, 255)
        )

        subtitle_rect = subtitle.get_rect(
            center=(
                self.width // 2,
                100
            )
        )

        self.screen.blit(
            subtitle,
            subtitle_rect
        )

        # ==================================
        # GET DATA
        # ==================================

        stats = self.get_statistics()

        # ==================================
        # CARD FUNCTION
        # ==================================

        def draw_card(
            x,
            y,
            width,
            height,
            title,
            value
        ):

            pygame.draw.rect(
                self.screen,
                (30, 30, 45),
                (x, y, width, height)
            )

            pygame.draw.rect(
                self.screen,
                (80, 80, 100),
                (x, y, width, height),
                2
            )

            title_surface = (
                card_title_font.render(
                    title,
                    True,
                    (180, 180, 180)
                )
            )

            title_rect = title_surface.get_rect(
                center=(
                    x + width // 2,
                    y + 35
                )
            )

            self.screen.blit(
                title_surface,
                title_rect
            )

            value_surface = (
                value_font.render(
                    str(value),
                    True,
                    (255, 215, 0)
                )
            )

            value_rect = value_surface.get_rect(
                center=(
                    x + width // 2,
                    y + 80
                )
            )

            self.screen.blit(
                value_surface,
                value_rect
            )

        # ==================================
        # ROW 1
        # ==================================

        draw_card(
            80,
            140,
            280,
            120,
            "TOTAL GAMES",
            stats["total_games"]
        )

        draw_card(
            440,
            140,
            280,
            120,
            "TOTAL PLAYERS",
            stats["total_players"]
        )

        # ==================================
        # ROW 2
        # ==================================

        draw_card(
            80,
            285,
            280,
            120,
            "HIGHEST SCORE",
            stats["highest_score"]
        )

        draw_card(
            440,
            285,
            280,
            120,
            "AVERAGE SCORE",
            round(
                stats["average_score"],
                2
            )
        )

        # ==================================
        # ROW 3
        # ==================================

        draw_card(
            80,
            430,
            280,
            80,
            "AVG. SNAKE LENGTH",
            round(
                stats["average_length"],
                2
            )
        )

        draw_card(
            440,
            430,
            280,
            80,
            "BEST PLAYER",
            stats["best_player"]
        )

        # ==================================
        # BEST PLAYER SCORE
        # ==================================

        best_score_text = small_font.render(
            f"Best Player Score: "
            f"{stats['best_player_score']}",
            True,
            (255, 255, 255)
        )

        best_score_rect = (
            best_score_text.get_rect(
                center=(
                    self.width // 2,
                    535
                )
            )
        )

        self.screen.blit(
            best_score_text,
            best_score_rect
        )

        # ==================================
        # FOOTER
        # ==================================

        footer = small_font.render(
            "Press ESC to return",
            True,
            (150, 150, 150)
        )

        footer_rect = footer.get_rect(
            center=(
                self.width // 2,
                575
            )
        )

        self.screen.blit(
            footer,
            footer_rect
        )

        pygame.display.flip()

    # ==========================================
    # RUN
    # ==========================================

    def run(self):

        self.running = True

        while self.running:

            self.handle_events()

            self.draw()

            self.clock.tick(30)