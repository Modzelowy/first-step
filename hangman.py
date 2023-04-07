"""
The hangman game the program chooses a random word from list and prompts the user to guess letters in word.
It keeps track of user's guesses and fills in
the blanks for correctly guessed letters until the user guesses the word or runs out of guesses     
"""
import random


class Game:
    # when we will create an instance we create lifes, counter,
    # then open file read the wordsforhangman we then save in self data and use it to pick a random one in self.line
    def __init__(self):
        self.lifes = 12
        self.counter = 0

        with open("wordsforhangman.txt", "r") as f:
            self.data = f.readlines()

        self.line = random.choice(self.data)

    def game_logic(self):
        # we create blanks based on how many letters is in the word that has been choosen,
        # we print the blanks so the user has a rough idea how many letters to provie
        self.create_blank()
        print(self.blank)
        while (
            self.lifes > 0 and "_" in self.blank
        ):  # game loop if lifes are bigger than 0 and there is still blank to fill
            guess = (
                self.get_user_input()
            )  # we assign guess parameter to get_user_input so that guess is ultimetly a letter user provides
            if guess in self.line:  # we check if the letter is in the word  if it is:
                self.fill_blank(guess)  # we fill a blank
            else:
                self.decrement_life()  # if not we take 1 life of self.lifes
            print(
                self.blank
            )  # still in initial loop at the end of it we want to update the blanks to have already guessed letters
        self.increment_counter()  # this is an increament counter but we dont use it anywhere

    def get_user_input(self):
        message = "provide input"
        user_input = input(message)
        while (
            len(user_input) != 1 or not user_input.isalpha()
        ):  # here we check if user passed a letter and check if it's not capital
            user_input = input(message)

        return user_input

    def fill_blank(self, guess):
        indices = self.get_letter_indices(guess)
        for index in indices:
            self.blank[index] = guess

    def create_blank(self):
        self.blank = list("_" * (len(self.line) - 1))
        return self.blank

    def increment_counter(self):
        self.counter += 1

    def decrement_life(self):
        self.lifes -= 1

    def get_letter_indices(self, guess):
        return [idx for idx, value in enumerate(self.line) if value == guess]


Game().game_logic()
