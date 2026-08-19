import sqlite3


class Database:

    def __init__(self, db_name="game_history.db"):

        self.db_name = db_name

        self.create_table()


    # =================================
    # DATABASE CONNECTION
    # =================================

    def connect(self):

        return sqlite3.connect(
            self.db_name
        )


    # =================================
    # CREATE TABLE
    # =================================

    def create_table(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS game_history (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                player_name TEXT NOT NULL,

                score INTEGER NOT NULL,

                snake_length INTEGER NOT NULL,

                level INTEGER NOT NULL,

                food_type TEXT,

                game_date TIMESTAMP
                    DEFAULT CURRENT_TIMESTAMP

            )
        """)

        connection.commit()

        connection.close()


    # =================================
    # SAVE GAME
    # =================================

    def save_game(
        self,
        player_name,
        score,
        snake_length,
        level,
        food_type
    ):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO game_history
            (
                player_name,
                score,
                snake_length,
                level,
                food_type
            )

            VALUES (?, ?, ?, ?, ?)
        """, (
            player_name,
            score,
            snake_length,
            level,
            food_type
        ))

        connection.commit()

        connection.close()


    # =================================
    # GET ALL GAMES
    # =================================

    def get_all_games(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                id,
                player_name,
                score,
                snake_length,
                level,
                food_type,
                game_date

            FROM game_history

            ORDER BY score DESC
        """)

        games = cursor.fetchall()

        connection.close()

        return games


    # =================================
    # GET BEST SCORE
    # =================================

    def get_best_score(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT MAX(score)
            FROM game_history
        """)

        result = cursor.fetchone()

        connection.close()

        if result[0] is None:

            return 0

        return result[0]


    # =================================
    # GET TOP PLAYERS
    # =================================

    def get_leaderboard(
        self,
        limit=10
    ):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                player_name,
                MAX(score) AS best_score

            FROM game_history

            GROUP BY player_name

            ORDER BY best_score DESC

            LIMIT ?
        """, (
            limit,
        ))

        leaderboard = cursor.fetchall()

        connection.close()

        return leaderboard


    # =================================
    # GET PLAYER BEST SCORE
    # =================================

    def get_player_best_score(
        self,
        player_name
    ):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT MAX(score)

            FROM game_history

            WHERE player_name = ?
        """, (
            player_name,
        ))

        result = cursor.fetchone()

        connection.close()

        if result[0] is None:

            return 0

        return result[0]