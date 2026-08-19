import pygame
import os
import wave
import math
import struct


class SoundManager:

    def __init__(self):

        # =================================
        # SOUND FOLDER
        # =================================

        self.sound_folder = os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ),
            "sounds"
        )

        os.makedirs(
            self.sound_folder,
            exist_ok=True
        )

        # =================================
        # MIXER
        # =================================

        if not pygame.mixer.get_init():

            pygame.mixer.init()

        # =================================
        # CREATE SOUND FILES
        # =================================

        self.create_sound_files()

        # =================================
        # LOAD SOUNDS
        # =================================

        self.food_sound = pygame.mixer.Sound(
            os.path.join(
                self.sound_folder,
                "food.wav"
            )
        )

        self.game_over_sound = pygame.mixer.Sound(
            os.path.join(
                self.sound_folder,
                "game_over.wav"
            )
        )

        self.pause_sound = pygame.mixer.Sound(
            os.path.join(
                self.sound_folder,
                "pause.wav"
            )
        )

        self.start_sound = pygame.mixer.Sound(
            os.path.join(
                self.sound_folder,
                "start.wav"
            )
        )


    # =================================
    # CREATE TONE
    # =================================

    def create_tone(
        self,
        filename,
        frequency,
        duration
    ):

        filepath = os.path.join(
            self.sound_folder,
            filename
        )

        if os.path.exists(filepath):

            return

        sample_rate = 44100

        samples = int(
            sample_rate * duration
        )

        with wave.open(
            filepath,
            "w"
        ) as sound_file:

            sound_file.setnchannels(1)

            sound_file.setsampwidth(2)

            sound_file.setframerate(
                sample_rate
            )

            for i in range(samples):

                value = int(
                    16000 *
                    math.sin(
                        2 *
                        math.pi *
                        frequency *
                        i /
                        sample_rate
                    )
                )

                data = struct.pack(
                    "<h",
                    value
                )

                sound_file.writeframes(
                    data
                )


    # =================================
    # CREATE ALL SOUNDS
    # =================================

    def create_sound_files(self):

        # Food sound
        self.create_tone(
            "food.wav",
            800,
            0.10
        )

        # Game over sound
        self.create_tone(
            "game_over.wav",
            180,
            0.50
        )

        # Pause sound
        self.create_tone(
            "pause.wav",
            400,
            0.15
        )

        # Start sound
        self.create_tone(
            "start.wav",
            600,
            0.20
        )


    # =================================
    # FOOD
    # =================================

    def play_food(self):

        self.food_sound.play()


    # =================================
    # GAME OVER
    # =================================

    def play_game_over(self):

        self.game_over_sound.play()


    # =================================
    # PAUSE
    # =================================

    def play_pause(self):

        self.pause_sound.play()


    # =================================
    # START
    # =================================

    def play_start(self):

        self.start_sound.play()