import random


class Game:
    dictionary_of_choices = {1: "scissors", 2: "paper", 3: "rock"}
    a_random_number = random.randint(1, 3)
    random_choice = dictionary_of_choices[a_random_number]

    def user_input(self):
        user_choice = input("choose between: rock paper and scissors:  ")
        match user_choice:
            case "scissors":
                if self.random_choice == "scissors":
                    print("Its a draw")
                elif self.random_choice == "rock":
                    print("you lost")
                elif self.random_choice == "paper":
                    print("you win congrats")

            case "rock":
                if self.random_choice == "rock":
                    print("its a draw")
                elif self.random_choice == "paper":
                    print("you lost")
                elif self.random_choice == "scissors":
                    print("you win congrats")

            case "paper":
                if self.random_choice == "paper":
                    print("its a draw")
                elif self.random_choice == "scissors":
                    print("you lost")
                elif self.random_choice == "rock":
                    print("you win congrats")

            case _:
                print("your doing something wrong m8")


game = Game()
game.user_input()
