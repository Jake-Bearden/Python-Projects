class Player:

    def __init__(self):
        self.name = ""
        self.score = 0
        self.games_played = 0
        self.games_won = 0
        self.best_score = 0

    def update_stats(self, won, score):
        # Update player statistics
        self.games_played += 1
        if won:
            self.games_won += 1
        if score > self.best_score:
            self.best_score = score

    def display_stats(self):
        # Display player statistics
        print(f"Player: {self.name}")
        print(f"Games Played: {self.games_played}")
        print(f"Games Won: {self.games_won}")
        print(f"Best Score: {self.best_score}")