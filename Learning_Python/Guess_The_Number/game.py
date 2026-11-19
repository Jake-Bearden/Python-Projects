import random
from player import Player


class GuessingGame:

    def __init__(self):
        self.player = Player()
        self.secret_number = 0
        self.attempts = 0
        self.max_attempts = 0
        self.difficulty = ""

    def start(self):
        self.get_player_name()
        self.select_difficulty()
        self.generate_number()
        self.play()
        self.show_results()

    def get_player_name(self):
        # Get player's name
        pass

    def select_difficulty(self):
        # Allow player to select difficulty
        # Easy: 1-50
        # Medium: 1-100
        # Hard: 1-500
        pass

    def generate_number(self):
        # Generate random secret number
        pass

    def play(self):
        # Main guessing loop
        # Get player guesses
        # Check if guess is too high or too low
        # Track attempts
        # End when guessed correctly or attempts run out
        pass

    def check_guess(self, guess):
        # Compare guess against secret number
        pass

    def show_results(self):
        # Display final score and game results
        pass