import sqlite3
import hashlib


class Auth:

    def __init__(self, db_name="game_history.db"):
        self.db_name = db_name
        self.create_users_table()

    # ==========================================
    # DATABASE CONNECTION
    # ==========================================

    def connect(self):
        return sqlite3.connect(self.db_name)

    # ==========================================
    # CREATE USERS TABLE
    # ==========================================

    def create_users_table(self):

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                username TEXT UNIQUE NOT NULL,

                password TEXT NOT NULL,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()
        conn.close()

    # ==========================================
    # PASSWORD HASH
    # ==========================================

    def hash_password(self, password):

        return hashlib.sha256(
            password.encode()
        ).hexdigest()

    # ==========================================
    # REGISTER
    # ==========================================

    def register(self, username, password):

        username = username.strip()

        if username == "" or password == "":
            return False, "Username and password required."

        password_hash = self.hash_password(password)

        conn = self.connect()
        cursor = conn.cursor()

        try:

            cursor.execute("""
                INSERT INTO users
                (username, password)
                VALUES (?, ?)
            """, (
                username,
                password_hash
            ))

            conn.commit()

            return True, "Registration successful."

        except sqlite3.IntegrityError:

            return False, "Username already exists."

        finally:

            conn.close()

    # ==========================================
    # LOGIN
    # ==========================================

    def login(self, username, password):

        password_hash = self.hash_password(password)

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, username
            FROM users
            WHERE username = ?
            AND password = ?
        """, (
            username,
            password_hash
        ))

        user = cursor.fetchone()

        conn.close()

        if user:

            return True, user

        return False, None
    