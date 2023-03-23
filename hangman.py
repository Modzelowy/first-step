import random


"""
The hangman game the program chooses a random word from list and prompts the user to guess letters in word.
It keeps track of user's guesses and fills in
the blanks for correctly guessed letters until the user guesses the word or runs out of guesses    
    
    
"""


class Game:
    def __init__(self):
        with open("wordsforhangman.txt", "r") as f:
            self.data = f.readlines()
            self.line = random.choice(self.data)
            self.number_of_lifes = 12
            self.counter = 0

    def game_logic(self):
        self.create_blank()
        print(f"{self.blanks}")
        while self.number_of_lifes > 0 and "_" in self.blanks:
            guess = self.user_input()
            if guess in self.line:
                self.fill_blank(guess)
            else:
                self.life_decrement()
            print(f"{self.blanks}")
        self.guess_counter()

    def user_input(self):
        self.inputek = input("provide a letter: ")
        return self.inputek

    def fill_blank(self, guess):
        indices = self.looking_for_index(guess)
        for index in indices:
            self.blanks[index] = guess

    def create_blank(self):
        blank = "_"
        number_of_blanks = len(self.line)
        self.blanks = list((number_of_blanks - 1) * blank)
        return self.blanks

    def guess_counter(self):
        self.counter += 1

    def life_decrement(self):
        self.number_of_lifes -= 1

    def looking_for_index(self, guess):
        index_list = [idx for idx, value in enumerate(self.line) if value == guess]
        return index_list


game = Game()
game.game_logic()
