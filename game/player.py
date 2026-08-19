class Player:

    def __init__(self, name):

        self.name = name

        self.games_played = 0

        self.best_score = 0

        self.best_length = 0

        self.current_score = 0

        self.current_length = 3

    def start_game(self):

        self.games_played += 1

        self.current_score = 0

        self.current_length = 3

    def update_score(self, score):

        self.current_score = score

        if score > self.best_score:

            self.best_score = score

    def update_length(self, length):

        self.current_length = length

        if length > self.best_length:

            self.best_length = length

    def get_statistics(self):

        return {
            "name": self.name,
            "games_played": self.games_played,
            "best_score": self.best_score,
            "best_length": self.best_length
        }