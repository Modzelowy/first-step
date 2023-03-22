"""
Number guessing game: The program generates random number between a specified range and prompts the user to guess the number.
It keeps track of guessed attemps and tells user if number is too hight or too low 
"""
# first we have to import the random standard library in order to generate the semi-random number
import random

# first we define a class Game in which we will put all of the game logic
class Game:
    def __init__(self):
        self.guessed_attempts = 0
        self.the_secret_number = random.randint(1, 50)

    def guessing_game(self, number: int) -> str:

        if number == self.the_secret_number:
            return (
                f"Congratulations u guessed right after {self.counter_of_times_run()}"
            )

        if number < self.the_secret_number:
            return f"that is too low \n attempt number {self.counter_of_times_run()}"
        if number > self.the_secret_number:
            return f"too hight bruther \n attempt number {self.counter_of_times_run()}"

    def counter_of_times_run(self):
        self.guessed_attempts += 1
        return self.guessed_attempts

    def restart(self):
        self.guessed_attempts = 0
        self.the_secret_number = random.randint(1, 50)

    def game_loop(self):
        while True:
            guess = int(input("Guess the number between 1 and 50: "))
            result = self.guessing_game(guess)
            print(result)
            if "Congratulations" in result:
                play_again = input("Do you want to play again? (yes/no): ")
                if play_again == "yes":
                    self.restart()
                else:
                    break


game = Game()
game.game_loop()
