"""
Simple game of tick tack toe
#     """
import re


class Game:
    WIDTH = 3
    HEIGHT = 3

    def __init__(self):
        self.board_matrix = [
            [" " for x in range(self.WIDTH)] for x in range(self.HEIGHT)
        ]

    def play(self):
        self.draw()
        for round in range(self.WIDTH * self.HEIGHT):
            x, y = self.get_user_input()
            player = "X" if round % 2 else "O"
            self.board_matrix[x][y] = player
            self.draw()
            if self.check_win(player):
                print(f"Player {player} wins!")
                return
        print("It's a tie!")

    def draw(self):
        for row in self.board_matrix:
            print(row)

    def get_user_input(self):
        while True:
            user_input = input("Enter x,y value (e.g. '1,2'): ")
            match = re.match(r"^\s*(\d+)\s*,\s*(\d+)\s*$", user_input)
            if match:
                x = int(match.group(1))
                y = int(match.group(2))
                if (
                    0 <= x < self.WIDTH
                    and 0 <= y < self.HEIGHT
                    and self.board_matrix[x][y] == " "
                ):
                    return x, y
            print(
                "Invalid input. Please enter x,y value in the format 'x,y' (e.g. '1,2') and choose an empty spot on the board."
            )

    def check_win(self, player):
        # Check rows
        for row in self.board_matrix:
            if row.count(player) == self.WIDTH:
                return True

        # Check columns
        for col in range(self.WIDTH):
            if all(self.board_matrix[row][col] == player for row in range(self.HEIGHT)):
                return True

        # Check diagonals
        if all(self.board_matrix[i][i] == player for i in range(self.WIDTH)):
            return True

        if all(
            self.board_matrix[i][self.WIDTH - 1 - i] == player
            for i in range(self.WIDTH)
        ):
            return True

        return False


if __name__ == "__main__":
    game = Game()
    game.play()


# to do
# user nie moze wstawiac w to samo miejsce
# Win condition
