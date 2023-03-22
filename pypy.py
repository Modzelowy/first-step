import curses
import time
import random

FPS = 10


class Snake:
    HEAD = "Ó"
    BODY = "0"
    FOOD = "X"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.body = [(x, y)]
        self.direction = curses.KEY_RIGHT

        # we create food before the game starts and every time the snake eats food
        self.food = self.gerate_food()

    def get_head_position(self):

        return self.body[0]

    def set_direction(self, key):
        """
        We need to set the direction of the snake, because we can't just change it in the update method.
        If we would, the snake would change direction only if we are pressing a key during the update.
        """
        if key == curses.KEY_UP:
            self.direction = curses.KEY_UP
        elif key == curses.KEY_DOWN:
            self.direction = curses.KEY_DOWN
        elif key == curses.KEY_LEFT:
            self.direction = curses.KEY_LEFT
        elif key == curses.KEY_RIGHT:
            self.direction = curses.KEY_RIGHT
        else:
            raise KeyError("to niezła strzałka")

    def gerate_food(self) -> tuple[int, int]:
        """generate food coordinates using random.randint"""
        generate_x_pos = random.randint(1, self.x - 1)
        generate_y_pos = random.randint(1, self.y - 1)
        gen_x_y_tuple = (generate_x_pos, generate_y_pos)
        return gen_x_y_tuple

    def eat_food(self) -> bool:
        """
        enlarge the snake's body and generate new food coordinates.
        To enlarge the snake's body, we can duplicate the last element of the body.
        we need to overwrite the food attribute with the new coordinates.
        """
        if self.body[0] == self.food:
            self.body.insert(0, self.get_head_position())
            self.food = self.gerate_food()
            return True
        else:
            return False

    def update(self):
        """
        we should:
        - update the snake's body - we can prepend the new head to the body and pop the last element
        - the snake should be moving in the direction we set in the set_direction method
        - check if the snake is eating food - if yes, call the eat_food method
        - check if the snake is dead (if it's outside the screen or if it's eating itself)
        """
        head_x, head_y = self.get_head_position()
        if self.direction == curses.KEY_UP:
            new_head = (head_x - 1, head_y)
        elif self.direction == curses.KEY_DOWN:
            new_head = (head_x + 1, head_y)
        elif self.direction == curses.KEY_LEFT:
            new_head = (head_x, head_y - 1)
        elif self.direction == curses.KEY_RIGHT:
            new_head = (head_x, head_y + 1)

        self.body.insert(0, new_head)
        self.body.pop()

        if (
            new_head[0] in [0, self.x]
            or new_head[1] in [0, self.y]
            or new_head in self.body[1:]
        ):

            raise ValueError("Game Over")
        elif self.eat_food():

            self.food = self.generate_food()

    def draw(self):
        SNAKE_WIDTH = 20
        SNAKE_HEIGHT = 20
        FIELDS = [
            (col, row) for row in range(SNAKE_HEIGHT) for col in range(SNAKE_WIDTH)
        ]
        for field in FIELDS:
            if field[0] in (0, SNAKE_WIDTH - 1) or field[1] in (0, SNAKE_HEIGHT - 1):
                print("#", end="")
            elif field == self.food:
                print(self.FOOD)
            elif field in self.body:
                if field == self.get_head_position():
                    print(self.HEAD, end="")
                else:
                    print(self.BODY, end="")
            else:
                print(" ", end="")
            if field[0] == SNAKE_WIDTH - 1:
                print("")


def game_loop(stdscr):
    snake = Snake(5, 5)
    time_prev = time.time()

    while True:
        key = stdscr.getch()
        snake.set_direction(key)

        if time.time() - time_prev > 1 / FPS:
            snake.update()
            time_prev = time.time()


if __name__ == "__main__":
    curses.wrapper(game_loop)
