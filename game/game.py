import pygame
import time
import os

from game.snake import Snake
from game.food import Food
from game.obstacle import Obstacle
from game.powerup import PowerUp
from database.db import Database


class Game:

    def __init__(self, player):

        # ==========================================
        # PYGAME
        # ==========================================

        pygame.init()

        # ==========================================
        # PLAYER
        # ==========================================

        self.player = player
        self.player.start_game()

        # ==========================================
        # DATABASE
        # ==========================================

        self.database = Database()

        # ==========================================
        # SCREEN
        # ==========================================

        self.width = 800
        self.height = 600

        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )

        pygame.display.set_caption(
            "SmartSnake"
        )

        # ==========================================
        # CLOCK
        # ==========================================

        self.clock = pygame.time.Clock()

        # ==========================================
        # GAME OBJECTS
        # ==========================================

        self.snake = Snake()
        self.food = Food()

        # ==========================================
        # OBSTACLES
        # ==========================================

        self.obstacles = []

        # ==========================================
        # POWERUP
        # ==========================================

        self.powerup = PowerUp(
            self.width,
            self.height
        )

        self.powerup.active = False

        self.powerup_spawn_time = time.time()
        self.powerup_interval = 10

        # ==========================================
        # POWERUP EFFECTS
        # ==========================================

        self.speed_boost = False
        self.double_score = False
        self.shield_active = False

        self.active_power_name = "NONE"
        self.powerup_end_time = 0

        # ==========================================
        # SCORE
        # ==========================================

        self.score = 0

        # ==========================================
        # GAME STATE
        # ==========================================

        self.running = True
        self.game_over = False
        self.game_saved = False

        # ==========================================
        # SOUND
        # ==========================================

        self.sound_enabled = True
        self.music_enabled = True

        try:
            pygame.mixer.init()
        except pygame.error:
            self.sound_enabled = False
            self.music_enabled = False

        self.food_sound = self.load_sound(
            "sounds/food.wav"
        )

        self.powerup_sound = self.load_sound(
            "sounds/powerup.wav"
        )

        self.gameover_sound = self.load_sound(
            "sounds/gameover.wav"
        )

        self.load_background_music()

        # ==========================================
        # CREATE OBSTACLES
        # ==========================================

        self.create_obstacles()

    # ==================================================
    # LOAD SOUND
    # ==================================================

    def load_sound(self, filename):

        if not self.sound_enabled:
            return None

        if not os.path.exists(filename):

            print(
                f"Sound file not found: {filename}"
            )

            return None

        try:

            return pygame.mixer.Sound(
                filename
            )

        except pygame.error:

            print(
                f"Could not load sound: {filename}"
            )

            return None

    # ==================================================
    # BACKGROUND MUSIC
    # ==================================================

    def load_background_music(self):

        if not self.music_enabled:
            return

        filename = "sounds/background.mp3"

        if not os.path.exists(filename):

            print(
                f"Background music not found: {filename}"
            )

            return

        try:

            pygame.mixer.music.load(
                filename
            )

            pygame.mixer.music.set_volume(
                0.30
            )

            pygame.mixer.music.play(
                -1
            )

        except pygame.error:

            print(
                "Could not load background music."
            )

    # ==================================================
    # STOP MUSIC
    # ==================================================

    def stop_background_music(self):

        try:

            if pygame.mixer.get_init():

                pygame.mixer.music.stop()

        except pygame.error:

            pass

    # ==================================================
    # PLAY SOUND
    # ==================================================

    def play_sound(self, sound):

        if not self.sound_enabled:
            return

        if sound is None:
            return

        try:

            sound.play()

        except pygame.error:

            pass

    # ==================================================
    # CREATE OBSTACLES
    # ==================================================

    def create_obstacles(self):

        self.obstacles = []

        for _ in range(5):

            while True:

                obstacle = Obstacle(
                    self.width,
                    self.height
                )

                position = obstacle.position

                # Snake ke upar nahi
                if position in self.snake.body:
                    continue

                # Food ke upar nahi
                if position == self.food.position:
                    continue

                # Existing obstacle ke upar nahi
                existing_positions = [
                    item.position
                    for item in self.obstacles
                ]

                if position in existing_positions:
                    continue

                break

            self.obstacles.append(
                obstacle
            )

    # ==================================================
    # HANDLE EVENTS
    # ==================================================

    def handle_events(self):

        for event in pygame.event.get():

            # ==========================================
            # WINDOW CLOSE
            # ==========================================

            if event.type == pygame.QUIT:

                self.running = False

                continue

            # ==========================================
            # KEYBOARD
            # ==========================================

            if event.type == pygame.KEYDOWN:

                # ======================================
                # ESC = RETURN TO MAIN MENU
                # ======================================

                if event.key == pygame.K_ESCAPE:

                    self.running = False

                    self.stop_background_music()

                    return

                # ======================================
                # SOUND
                # ======================================

                if event.key == pygame.K_m:

                    self.sound_enabled = (
                        not self.sound_enabled
                    )

                    print(
                        "Sound Effects:",
                        "ON"
                        if self.sound_enabled
                        else "OFF"
                    )

                    if not self.sound_enabled:

                        try:

                            pygame.mixer.stop()

                        except pygame.error:

                            pass

                # ======================================
                # MUSIC
                # ======================================

                elif event.key == pygame.K_n:

                    self.music_enabled = (
                        not self.music_enabled
                    )

                    if self.music_enabled:

                        print(
                            "Background Music: ON"
                        )

                        self.start_background_music()

                    else:

                        print(
                            "Background Music: OFF"
                        )

                        self.stop_background_music()

                # ======================================
                # GAME RUNNING
                # ======================================

                if not self.game_over:

                    if event.key == pygame.K_UP:

                        self.snake.change_direction(
                            "UP"
                        )

                    elif event.key == pygame.K_DOWN:

                        self.snake.change_direction(
                            "DOWN"
                        )

                    elif event.key == pygame.K_LEFT:

                        self.snake.change_direction(
                            "LEFT"
                        )

                    elif event.key == pygame.K_RIGHT:

                        self.snake.change_direction(
                            "RIGHT"
                        )

                # ======================================
                # GAME OVER
                # ======================================

                else:

                    if event.key == pygame.K_r:

                        self.restart()

    # ==================================================
    # START MUSIC
    # ==================================================

    def start_background_music(self):

        if not self.music_enabled:
            return

        try:

            if pygame.mixer.get_init():

                pygame.mixer.music.play(
                    -1
                )

        except pygame.error:

            pass

    # ==================================================
    # CHECK FOOD
    # ==================================================

    def check_food(self):

        snake_head = self.snake.body[0]

        if snake_head == self.food.position:

            self.snake.grow()

            points = self.food.get_points()

            # Double score
            if self.double_score:

                points *= 2

            self.score += points

            self.player.update_score(
                self.score
            )

            self.player.update_length(
                len(self.snake.body)
            )

            self.play_sound(
                self.food_sound
            )

            self.respawn_food()

    # ==================================================
    # RESPAWN FOOD
    # ==================================================

    def respawn_food(self):

        while True:

            new_position = (
                self.food.generate_position()
            )

            # Snake ke andar nahi
            if new_position in self.snake.body:
                continue

            # Obstacles
            obstacle_positions = [
                obstacle.position
                for obstacle in self.obstacles
            ]

            if new_position in obstacle_positions:
                continue

            self.food.position = new_position

            self.food.type = (
                self.food.generate_type()
            )

            break

    # ==================================================
    # POWERUP SPAWN
    # ==================================================

    def update_powerup_spawn(self):

        if self.powerup.active:
            return

        current_time = time.time()

        if (
            current_time
            - self.powerup_spawn_time
            >= self.powerup_interval
        ):

            self.spawn_powerup()

    # ==================================================
    # SPAWN POWERUP
    # ==================================================

    def spawn_powerup(self):

        while True:

            self.powerup.respawn()

            position = self.powerup.position

            if position in self.snake.body:
                continue

            if position == self.food.position:
                continue

            obstacle_positions = [
                obstacle.position
                for obstacle in self.obstacles
            ]

            if position in obstacle_positions:
                continue

            break

        self.powerup_spawn_time = time.time()

    # ==================================================
    # CHECK POWERUP
    # ==================================================

    def check_powerup(self):

        if not self.powerup.active:
            return

        snake_head = self.snake.body[0]

        if snake_head != self.powerup.position:
            return

        power_type = self.powerup.type

        self.powerup.active = False

        self.play_sound(
            self.powerup_sound
        )

        # ==============================================
        # SPEED
        # ==============================================

        if power_type == "SPEED":

            self.speed_boost = True
            self.double_score = False
            self.shield_active = False

            self.active_power_name = "SPEED"

            self.powerup_end_time = (
                time.time() + 8
            )

        # ==============================================
        # DOUBLE SCORE
        # ==============================================

        elif power_type == "DOUBLE":

            self.double_score = True
            self.speed_boost = False
            self.shield_active = False

            self.active_power_name = "DOUBLE"

            self.powerup_end_time = (
                time.time() + 10
            )

        # ==============================================
        # SHIELD
        # ==============================================

        elif power_type == "SHIELD":

            self.shield_active = True
            self.speed_boost = False
            self.double_score = False

            self.active_power_name = "SHIELD"

            self.powerup_end_time = (
                time.time() + 15
            )

    # ==================================================
    # UPDATE POWERUP EFFECT
    # ==================================================

    def update_powerup_effect(self):

        if not (
            self.speed_boost
            or
            self.double_score
            or
            self.shield_active
        ):

            return

        if time.time() >= self.powerup_end_time:

            self.speed_boost = False
            self.double_score = False
            self.shield_active = False

            self.active_power_name = "NONE"

            self.powerup_end_time = 0

    # ==================================================
    # POWERUP TIMER
    # ==================================================

    def get_powerup_time(self):

        if self.powerup_end_time <= 0:

            return 0

        remaining = (
            self.powerup_end_time
            - time.time()
        )

        return max(
            0,
            int(remaining)
        )

    # ==================================================
    # COLLISION
    # ==================================================

    def check_collision(self):

        collision = False

        # ==============================================
        # WALL
        # ==============================================

        if self.snake.check_wall_collision(
            self.width,
            self.height
        ):

            collision = True

        # ==============================================
        # SELF
        # ==============================================

        if self.snake.check_self_collision():

            collision = True

        # ==============================================
        # OBSTACLE
        # ==============================================

        snake_head = self.snake.body[0]

        for obstacle in self.obstacles:

            if snake_head == obstacle.position:

                collision = True

                break

        # ==============================================
        # SHIELD
        # ==============================================

        if collision and self.shield_active:

            self.shield_active = False

            self.active_power_name = "NONE"

            self.powerup_end_time = 0

            self.snake = Snake()

            return

        # ==============================================
        # GAME OVER
        # ==============================================

        if collision:

            self.game_over = True

            self.play_sound(
                self.gameover_sound
            )

        # ==============================================
        # SAVE DATABASE
        # ==============================================

        if (
            self.game_over
            and
            not self.game_saved
        ):

            self.save_game_result()

            self.game_saved = True

    # ==================================================
    # SAVE GAME
    # ==================================================

    def save_game_result(self):

        self.database.save_game(

            player_name=self.player.name,

            score=self.score,

            snake_length=len(
                self.snake.body
            ),

            level=self.get_level(),

            food_type=self.food.type
        )

    # ==================================================
    # SPEED
    # ==================================================

    def get_speed(self):

        if self.score < 50:

            speed = 10

        elif self.score < 100:

            speed = 12

        elif self.score < 200:

            speed = 14

        elif self.score < 300:

            speed = 16

        else:

            speed = 18

        if self.speed_boost:

            speed += 5

        return speed

    # ==================================================
    # LEVEL
    # ==================================================

    def get_level(self):

        if self.score < 50:

            return 1

        elif self.score < 100:

            return 2

        elif self.score < 200:

            return 3

        elif self.score < 300:

            return 4

        return 5

    # ==================================================
    # RESTART
    # ==================================================

    def restart(self):

        self.snake = Snake()

        self.food = Food()

        self.powerup = PowerUp(
            self.width,
            self.height
        )

        self.powerup.active = False

        self.powerup_spawn_time = time.time()

        self.score = 0

        self.game_over = False
        self.game_saved = False

        self.speed_boost = False
        self.double_score = False
        self.shield_active = False

        self.active_power_name = "NONE"
        self.powerup_end_time = 0

        self.player.start_game()

        self.create_obstacles()

    # ==================================================
    # DRAW
    # ==================================================

    def draw(self):

        self.screen.fill(
            (20, 20, 30)
        )

        # ==============================================
        # SNAKE
        # ==============================================

        self.snake.draw(
            self.screen
        )

        # ==============================================
        # FOOD
        # ==============================================

        self.food.draw(
            self.screen
        )

        # ==============================================
        # OBSTACLES
        # ==============================================

        for obstacle in self.obstacles:

            obstacle.draw(
                self.screen
            )

        # ==============================================
        # POWERUP
        # ==============================================

        self.powerup.draw(
            self.screen
        )

        # ==============================================
        # FONTS
        # ==============================================

        font = pygame.font.Font(
            None,
            26
        )

        # ==============================================
        # PLAYER
        # ==============================================

        self.screen.blit(

            font.render(
                f"Player: {self.player.name}",
                True,
                (255, 255, 255)
            ),

            (20, 15)
        )

        # ==============================================
        # SCORE
        # ==============================================

        self.screen.blit(

            font.render(
                f"Score: {self.score}",
                True,
                (255, 255, 255)
            ),

            (20, 45)
        )

        # ==============================================
        # LEVEL
        # ==============================================

        self.screen.blit(

            font.render(
                f"Level: {self.get_level()}",
                True,
                (255, 255, 255)
            ),

            (20, 75)
        )

        # ==============================================
        # SPEED
        # ==============================================

        self.screen.blit(

            font.render(
                f"Speed: {self.get_speed()}",
                True,
                (255, 255, 255)
            ),

            (20, 105)
        )

        # ==============================================
        # LENGTH
        # ==============================================

        self.screen.blit(

            font.render(
                f"Length: {len(self.snake.body)}",
                True,
                (255, 255, 255)
            ),

            (20, 135)
        )

        # ==============================================
        # POWER
        # ==============================================

        self.screen.blit(

            font.render(
                f"Power: {self.active_power_name}",
                True,
                (255, 215, 0)
            ),

            (20, 165)
        )

        # ==============================================
        # POWER TIMER
        # ==============================================

        remaining = self.get_powerup_time()

        if remaining > 0:

            self.screen.blit(

                font.render(
                    f"Power Time: {remaining}s",
                    True,
                    (255, 255, 255)
                ),

                (20, 195)
            )

        # ==============================================
        # CONTROLS
        # ==============================================

        self.screen.blit(

            font.render(
                "ESC = Main Menu",
                True,
                (180, 180, 180)
            ),

            (20, 560)
        )

        # ==============================================
        # GAME OVER SCREEN
        # ==============================================

        if self.game_over:

            big_font = pygame.font.Font(
                None,
                70
            )

            small_font = pygame.font.Font(
                None,
                30
            )

            game_over_text = big_font.render(
                "GAME OVER",
                True,
                (255, 80, 80)
            )

            score_text = small_font.render(
                f"Final Score: {self.score}",
                True,
                (255, 255, 255)
            )

            best_text = small_font.render(
                f"Best Score: {self.player.best_score}",
                True,
                (255, 215, 0)
            )

            restart_text = small_font.render(
                "R = Restart    ESC = Main Menu",
                True,
                (255, 255, 255)
            )

            self.screen.blit(
                game_over_text,
                game_over_text.get_rect(
                    center=(
                        self.width // 2,
                        220
                    )
                )
            )

            self.screen.blit(
                score_text,
                score_text.get_rect(
                    center=(
                        self.width // 2,
                        300
                    )
                )
            )

            self.screen.blit(
                best_text,
                best_text.get_rect(
                    center=(
                        self.width // 2,
                        340
                    )
                )
            )

            self.screen.blit(
                restart_text,
                restart_text.get_rect(
                    center=(
                        self.width // 2,
                        400
                    )
                )
            )

        # ==============================================
        # DISPLAY UPDATE
        # ==============================================

        pygame.display.flip()

    # ==================================================
    # MAIN GAME LOOP
    # ==================================================

    def run(self):

        self.running = True

        while self.running:

            self.handle_events()

            # ESC ke baad loop immediately stop
            if not self.running:
                break

            if not self.game_over:

                self.snake.move()

                self.check_food()

                self.check_powerup()

                self.update_powerup_spawn()

                self.update_powerup_effect()

                self.check_collision()

            self.draw()

            self.clock.tick(
                self.get_speed()
            )

        # ==============================================
        # MUSIC STOP
        # ==============================================

        self.stop_background_music()

        # IMPORTANT:
        # pygame.quit() yahan NAHI hai.
        # Main.py final mein pygame.quit() karega.

        return