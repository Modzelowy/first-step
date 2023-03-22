import curses
import time
import random

FPS = 10
HEAD = "Ó"
BODY = "0"
FOOD = "X"
WALL = "#"
EMPTY = " "
WIDTH, HEIGHT = 20, 20


DIRECTIONS = {
    curses.KEY_UP: (0, -1),
    curses.KEY_DOWN: (0, 1),
    curses.KEY_LEFT: (-1, 0),
    curses.KEY_RIGHT: (1, 0),
}


class Snake:
    def __init__(self, x_start, y_start):
        self.body = [(x_start, y_start)]
        self.direction = DIRECTIONS[curses.KEY_RIGHT]
        self.prev_direction = self.direction
        self.dead = False
        self.food = (
            self.generate_food()
        )  # we create food before the game starts and every time the snake eats food

    def get_head_position(self):
        return self.body[0]

    def set_direction(self, key):
        """
        We need to set the direction of the snake, because we can't just change it in the update method.
        If we would, the snake would change direction only if we are pressing a key during the update.
        """
        if key not in {
            curses.KEY_UP,
            curses.KEY_DOWN,
            curses.KEY_LEFT,
            curses.KEY_RIGHT,
        }:
            return  # we make sure that the key is one of the arrow keys

        dx, dy = DIRECTIONS[key]
        if (-dx, -dy) == self.prev_direction:
            return  # we make sure that the snake can't move in the opposite direction

        self.direction = dx, dy

    def generate_food(self) -> tuple[int, int]:
        """generate food coordinates using random.randint"""
        return random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2)

    def eat_food(self):
        """
        enlarge the snake's body and generate new food coordinates.
        To enlarge the snake's body, we can duplicate the last element of the body.
        we need to overwrite the food attribute with the new coordinates.
        """
        self.body.append(self.body[-1])
        self.food = self.generate_food()

    def draw(self, stdscr):
        """
        we should:
        - draw the snake's body
        - draw the snake's head
        - draw the food
        - draw the screen borders
        """
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) == self.food:
                    stdscr.addstr(y, x, FOOD)
                elif (x, y) in self.body:
                    stdscr.addstr(y, x, BODY)
                elif x == 0 or y == 0 or x == WIDTH - 1 or y == HEIGHT - 1:
                    stdscr.addstr(y, x, WALL)
                else:
                    stdscr.addstr(y, x, EMPTY)

    def update(self):
        """
        we should:
        - update the snake's body - we can prepend the new head to the body and pop the last element
        - the snake should be moving in the direction we set in the set_direction method
        - check if the snake is eating food - if yes, call the eat_food method
        - check if the snake is dead (if it's outside the screen or if it's eating itself)
        """
        head_x, head_y = self.get_head_position()

        # we need to save the previous direction so we know which direction the snake is moving in
        self.prev_direction = self.direction
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)

        self.body.insert(0, new_head)
        self.body.pop()

        if new_head in self.body[1:]:
            self.dead = True
        elif 0 in new_head or new_head[0] == WIDTH - 1 or new_head[1] == HEIGHT - 1:
            self.dead = True
        elif new_head == self.food:
            self.eat_food()


def game_loop(stdscr):
    snake = Snake(5, 5)
    time_prev = time.time()
    curses.halfdelay(1)

    while not snake.dead:
        key = stdscr.getch()
        snake.set_direction(key)

        if time.time() - time_prev > 1 / FPS:
            stdscr.clear()

            snake.update()
            snake.draw(stdscr)

            stdscr.refresh()
            time_prev = time.time()

    print("\nGame over!")
    while True:
        key = stdscr.getch()
        if key == ord("q"):
            break


if __name__ == "__main__":
    curses.wrapper(game_loop)
