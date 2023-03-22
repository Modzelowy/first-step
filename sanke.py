class Game:
    score = 0
    while score < 999:
        True


class Field:
    TILE = "#"

    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

    def grid_draw(self):
        for x in range(self.size_x):
            for y in range(self.size_y):
                if x == 0 or x == self.size_x - 1 or y == 0 or y == self.size_y - 1:
                    print("X", end="")
                else:
                    print("#", end="")
            print()


field = Field(25, 25)
field.grid_draw()


class Snake:
    moves = ["up", "down", "left", "right"]
    size = 1
    position = []
    snake_head = "Ó"
    snake_body = "0"

    def snake_move(self, move):
        for move in self.moves:
            if move == "up":
                print("gowno")

    # def snake_eat_func():
    #     size += 1


class Point:
    point = "Z"
    score = 0

    def spawn():
        pass


# Utwórz klasę Snake, która będzie reprezentować węża. Klasa ta powinna mieć atrybuty takie jak size, snake_head oraz snake_body.
# Metoda snake_move powinna określać ruch węża w określonym kierunku, natomiast metoda snake_eat_func powinna obsługiwać,
# zjedzenie jedzenia przez węża.

# Utwórz klasę Point, która reprezentuje jedzenie. Klasa ta powinna mieć atrybuty takie jak point oraz score.
# Metoda spawn powinna losowo umieszczać jedzenie na planszy.

# Utwórz klasę Game, która będzie kontrolować logikę gry.
# Ta klasa powinna mieć atrybuty takie jak plansza (pole klasy Field),
# wąż (pole klasy Snake) i punkty (pole klasy Point).
# Metoda play powinna obsługiwać pętlę gry, w której wąż przemieszcza się po planszy,
# a punkty pojawiają się i znikają.

# Utwórz funkcję draw, która będzie rysować planszę gry oraz pozycje węża i jedzenia.

# W metodzie play klasy Game, zaimplementuj pętlę gry, która będzie działać tak długo,
# jak wąż będzie się poruszał i nie natrafi na ścianę lub sam siebie.

# Zaimplementuj sterowanie wężem za pomocą klawiatury.

# Zaimplementuj logikę jedzenia przez węża i zwiększanie wyniku.
# Zdefiniuj klasę Snake, która będzie przechowywać informacje na temat pozycji węża na planszy oraz jego długości i wyglądu. Będziesz potrzebować co najmniej atrybutów position, length, head, body.
# Napisz metodę move(), która będzie przemieszczać węża na planszy zgodnie z podanym wektorem kierunku (np. w górę, w dół, w lewo, w prawo). Pamiętaj, że wąż składa się z głowy i ciała, które poruszają się w inny sposób.
# Napisz metodę eat(), która będzie odpowiadać za zwiększanie długości węża i dodawanie punktów do wyniku po zjedzeniu jedzenia.
# Zdefiniuj klasę Point, która będzie przechowywać informacje na temat pozycji punktu na planszy oraz jego wyglądu.
# Napisz metodę generate_point(), która będzie losowo generować pozycję punktu na planszy.
# Napisz metodę draw(), która będzie rysować planszę, węża i punkt na ekranie. Możesz użyć znaków ASCII do rysowania grafiki.
# Napisz metodę game_loop(), która będzie zawierać główną pętlę gry. W każdym cyklu pętli powinny być wywoływane metody draw(), move() i eat().
# Dodaj obsługę kolizji z samym sobą oraz z krawędziami planszy.
# Dodaj obsługę sterowania wężem przez gracza.
# Dodaj obsługę systemu punktacji i wyświetlanie wyniku na ekranie
