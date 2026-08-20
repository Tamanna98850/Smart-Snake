import pygame

from database.auth import Auth


class AuthScreen:

    def __init__(self, screen):

        self.screen = screen

        self.width = screen.get_width()
        self.height = screen.get_height()

        self.auth = Auth()

        self.title_font = pygame.font.Font(None, 60)
        self.font = pygame.font.Font(None, 32)
        self.small_font = pygame.font.Font(None, 24)

        self.username = ""
        self.password = ""

        self.active_field = "username"

        self.mode = "LOGIN"

        self.message = ""

        self.running = True

    # ==========================================
    # DRAW TEXT
    # ==========================================

    def draw_text(self, text, font, color, x, y):

        surface = font.render(
            text,
            True,
            color
        )

        rect = surface.get_rect(
            center=(x, y)
        )

        self.screen.blit(
            surface,
            rect
        )

    # ==========================================
    # DRAW
    # ==========================================

    def draw(self):

        self.screen.fill(
            (15, 15, 25)
        )

        # TITLE

        self.draw_text(
            "SMART SNAKE",
            self.title_font,
            (255, 215, 0),
            self.width // 2,
            70
        )

        # MODE

        self.draw_text(
            self.mode,
            self.font,
            (255, 255, 255),
            self.width // 2,
            135
        )

        # ======================================
        # USERNAME LABEL
        # ======================================

        self.draw_text(
            "Username",
            self.small_font,
            (180, 180, 180),
            self.width // 2,
            190
        )

        # USERNAME BOX

        username_border = (
            (255, 215, 0)
            if self.active_field == "username"
            else (100, 100, 100)
        )

        pygame.draw.rect(
            self.screen,
            username_border,
            (
                self.width // 2 - 170,
                205,
                340,
                50
            ),
            2
        )

        username_surface = self.font.render(
            self.username,
            True,
            (255, 255, 255)
        )

        self.screen.blit(
            username_surface,
            (
                self.width // 2 - 155,
                215
            )
        )

        # ======================================
        # PASSWORD LABEL
        # ======================================

        self.draw_text(
            "Password",
            self.small_font,
            (180, 180, 180),
            self.width // 2,
            290
        )

        # PASSWORD BOX

        password_border = (
            (255, 215, 0)
            if self.active_field == "password"
            else (100, 100, 100)
        )

        pygame.draw.rect(
            self.screen,
            password_border,
            (
                self.width // 2 - 170,
                305,
                340,
                50
            ),
            2
        )

        # Hide password

        hidden_password = "*" * len(
            self.password
        )

        password_surface = self.font.render(
            hidden_password,
            True,
            (255, 255, 255)
        )

        self.screen.blit(
            password_surface,
            (
                self.width // 2 - 155,
                315
            )
        )

        # ======================================
        # LOGIN / REGISTER BUTTON
        # ======================================

        pygame.draw.rect(
            self.screen,
            (40, 40, 55),
            (
                self.width // 2 - 120,
                390,
                240,
                50
            )
        )

        self.draw_text(
            self.mode,
            self.font,
            (255, 215, 0),
            self.width // 2,
            415
        )

        # ======================================
        # MODE SWITCH
        # ======================================

        self.draw_text(
            "TAB = Login / Register",
            self.small_font,
            (150, 150, 150),
            self.width // 2,
            470
        )

        # ======================================
        # MESSAGE
        # ======================================

        if self.message:

            self.draw_text(
                self.message,
                self.small_font,
                (255, 120, 120),
                self.width // 2,
                510
            )

        # ======================================
        # HELP
        # ======================================

        self.draw_text(
            "Click field • ENTER = Submit • ESC = Back",
            self.small_font,
            (120, 120, 120),
            self.width // 2,
            560
        )

    # ==========================================
    # SUBMIT
    # ==========================================

    def submit(self):

        username = self.username.strip()

        password = self.password

        # Empty username

        if username == "":

            self.message = "Please enter username."

            return None

        # Empty password

        if password == "":

            self.message = "Please enter password."

            return None

        # ======================================
        # REGISTER
        # ======================================

        if self.mode == "REGISTER":

            success, message = self.auth.register(
                username,
                password
            )

            self.message = message

            if success:

                self.mode = "LOGIN"

                self.password = ""

            return None

        # ======================================
        # LOGIN
        # ======================================

        success, user = self.auth.login(
            username,
            password
        )

        if success:

            print(
                "Login successful:",
                user
            )

            return user

        self.message = (
            "Invalid username or password."
        )

        return None

    # ==========================================
    # RUN
    # ==========================================

    def run(self):

        self.running = True

        while self.running:

            for event in pygame.event.get():

                # ==================================
                # CLOSE
                # ==================================

                if event.type == pygame.QUIT:

                    return None

                # ==================================
                # KEYBOARD
                # ==================================

                if event.type == pygame.KEYDOWN:

                    # ESC

                    if event.key == pygame.K_ESCAPE:

                        return None

                    # ENTER

                    elif event.key == pygame.K_RETURN:

                        result = self.submit()

                        if result:

                            return result

                    # TAB

                    elif event.key == pygame.K_TAB:

                        if self.mode == "LOGIN":

                            self.mode = "REGISTER"

                        else:

                            self.mode = "LOGIN"

                        self.message = ""

                    # BACKSPACE

                    elif event.key == pygame.K_BACKSPACE:

                        if self.active_field == "username":

                            self.username = (
                                self.username[:-1]
                            )

                        else:

                            self.password = (
                                self.password[:-1]
                            )

                    # ==================================
                    # SWITCH FIELD
                    # ==================================

                    elif event.key == pygame.K_UP:

                        self.active_field = "username"

                    elif event.key == pygame.K_DOWN:

                        self.active_field = "password"

                    # ==================================
                    # TYPE TEXT
                    # ==================================

                    else:

                        if event.unicode:

                            if self.active_field == "username":

                                if len(self.username) < 20:

                                    self.username += (
                                        event.unicode
                                    )

                            elif self.active_field == "password":

                                if len(self.password) < 30:

                                    self.password += (
                                        event.unicode
                                    )

                # ==================================
                # MOUSE CLICK
                # ==================================

                if event.type == pygame.MOUSEBUTTONDOWN:

                    mouse_x, mouse_y = event.pos

                    # Username box

                    username_box = pygame.Rect(
                        self.width // 2 - 170,
                        205,
                        340,
                        50
                    )

                    # Password box

                    password_box = pygame.Rect(
                        self.width // 2 - 170,
                        305,
                        340,
                        50
                    )

                    if username_box.collidepoint(
                        mouse_x,
                        mouse_y
                    ):

                        self.active_field = "username"

                    elif password_box.collidepoint(
                        mouse_x,
                        mouse_y
                    ):

                        self.active_field = "password"

            self.draw()

            pygame.display.flip()

        return None