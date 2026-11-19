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
<<<<<<< HEAD
        self.player.name = input("Enter your name: ")
=======
        # Get player's name
        pass
>>>>>>> ab3cf02d52c536c8cf7f785b58ad29688501b30b

    def select_difficulty(self):
        # Allow player to select difficulty
        # Easy: 1-50
        # Medium: 1-100
        # Hard: 1-500
<<<<<<< HEAD
        self.difficulty = input("Select difficulty (easy/medium/hard): ").lower()
        if self.difficulty == "easy":
            self.max_attempts = 10
            self.secret_number = random.randint(1, 50)
        elif self.difficulty == "medium":
            self.max_attempts = 15
            self.secret_number = random.randint(1, 100)
        elif self.difficulty == "hard":
            self.max_attempts = 20
            self.secret_number = random.randint(1, 500)
        else:
            print("Invalid difficulty. Setting to medium.")
            self.max_attempts = 15
            self.secret_number = random.randint(1, 100)

    def generate_number(self):
        # Generate random secret number
        self.secret_numver = random.randint(1,100)
=======
        pass

    def generate_number(self):
        # Generate random secret number
        pass
>>>>>>> ab3cf02d52c536c8cf7f785b58ad29688501b30b

    def play(self):
        # Main guessing loop
        # Get player guesses
        # Check if guess is too high or too low
        # Track attempts
        # End when guessed correctly or attempts run out
<<<<<<< HEAD
        while self.attempts < self.max_attempts:
            guess = int(input(f"Attempt {self.attempts + 1}/{self.max_attempts}: Enter your guess: "))
            self.attempts += 1
            if self.check_guess(guess):
                print("Congratulations! You've guessed the number!")
                self.player.update_stats(won=True, score=self.max_attempts - self.attempts)
                return
            else:
                print("Incorrect guess. Try again.\n")
        print(f"Game over! The number was {self.secret_number}.")
        self.player.update_stats(won=False, score=0)

    def check_guess(self, guess):
        # Compare guess against secret number
        if guess == self.secret_number:
            return True
        elif guess < self.secret_number:
            print("Too low!")
        else:
            print("Too high!")
        return False

    def show_results(self):
        # Display final score and game results
        print(f"Game Over! Your score: {self.max_attempts - self.attempts}")
=======
        pass

    def check_guess(self, guess):
        # Compare guess against secret number
        pass

    def show_results(self):
        # Display final score and game results
        pass
>>>>>>> ab3cf02d52c536c8cf7f785b58ad29688501b30b
