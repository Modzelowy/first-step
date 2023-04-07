"""
Zaimplementuj poniższe klasy i metody oraz przedstaw ich działanie wywołując funkcjonalności w mainie.

napisz klasę Rectangle z artybutami a, b
napisz metodę perimiter obliczającą obwód
napisz metodę area obliczającą powierzchnie
napisz metodę display, która wyświetli długość, szerokość, pole, obwód
czym jest metoda _repr_? zaimplementuj ją i zmodyfikuj metodę display tak, żeby wykorzystywała reprezentację tekstową

napisz klasę dziedziczącą Square, która przyjmie do konstruktora
tylko a i wywoła konstruktor klasy bazowej

napisz klasę Cuboid dziedziczącą po Rectangle, która
dodatkowo będzie posiadała atrybut h (wysokość)
napisz metodę volume, która obliczy objętość
zmodyfikuj kod tak, żeby display dodatkowo wyświetlał informację o volume

napisz klasę Cube dziedziczącą po Cuboid
"""


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.perimeter()
        self.area()

    def perimeter(self):
        self.circumference = 2 * (self.a + self.b)
        return self.circumference

    def area(self):
        self.area_rec = self.a * self.b
        return self.area_rec

    def display(self):
        messages = [
            f"a length = {self.a} ",
            f"b width = {self.b}",
            f"circumference = {self.circumference}",
            f"area = {self.area_rec}",
        ]
        for message in messages:
            print(message)


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)
        self.display()


class Cuboid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h
        self.volume()

    def volume(self):
        self.volume_of_cuboid = self.a * self.b * self.h
        return self.volume_of_cuboid

    def display(self):
        messages = [
            f"a length = {self.a} ",
            f"b width = {self.b}",
            f"h height = {self.h}",
            f"volume = {self.volume_of_cuboid}",
        ]
        for message in messages:
            print(message)


class Cube(Cuboid):
    def __init__(self, a):
        super().__init__(a, a, a)

    def perimeter(self):
        self.circumference = 12 * self.a
        return self.circumference

    def area(self):
        self.area_sqr = self.a**2
        return self.area_sqr

    def volume(self):
        self.volume_of_cuboid = self.a**3
        return self.volume_of_cuboid

    def display(self):
        messages = [
            f"a length = {self.a} ",
            f"b width = {self.a}",
            f"h height = {self.a}",
            f"volume = {self.volume_of_cuboid}",
            f"area  = {self.area_sqr}",
            f"perimeter = {self.circumference}",
        ]
        for message in messages:
            print(message)


if __name__ == "__main__":
    Rectangle(1, 1).display()
    Square(1).display()
    Cuboid(1, 1, 1).display()
    Cube(
        1,
    ).display()
