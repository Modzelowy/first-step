"""klasę ekspresu dom
 Kawy z funkcją robienia kawy, statusem ilości wody u kawy i sposobem na uzupełnianie ich
Feton
Rafał Łazicki
Zrobienie kawy ma kosztować 20 jednostek wody i 30 kawy
"""


class Cupboard:
    COFFE_STOCK = 1000
    WATER_STOCK = 1000

    def __init__(self, water_stock=WATER_STOCK, coffe_stock=COFFE_STOCK):
        self.water_stock = water_stock
        self.coffe_stock = coffe_stock


class CoffeeExpress:
    COFFE_MAX = 100
    WATER_MAX = 150
    MC_COFFEE = 30
    MC_WATER = 20

    def __init__(self):
        self.coffe_max = self.COFFE_MAX
        self.water_max = self.WATER_MAX
        self.coffee = 0
        self.water = 0

    def make_coffe(self):
        if self.coffee >= self.MC_COFFEE and self.water >= self.MC_WATER:
            self.coffee -= self.MC_COFFEE
            self.water -= self.MC_WATER
            print(
                "You've just made ur self a beautifull cup of coffe carefull it's hot"
            )
        else:
            self.warning()

    def status(self):
        messages = [
            f"current value of water = {self.coffee}",
            f"Current value of coffe = {self.water}",
        ]
        for message in messages:
            print(message)

    def load(self, cupboard: Cupboard):
        water_load = self.WATER_MAX - self.water
        if water_load > cupboard.water_stock:
            water_load = cupboard.water_stock

        coffee_load = self.COFFE_MAX - self.coffee
        if coffee_load > cupboard.coffe_stock:
            coffee_load = cupboard.coffe_stock

        cupboard.coffe_stock -= coffee_load
        cupboard.water_stock -= water_load
        self.coffee += coffee_load
        self.water += water_load

    def warning(self):
        print(
            "Warning current values of units water/coffe is  too low in coffe machine \n "
            + "please check status and  load  machine "
        )


if __name__ == "__main__":
    cupboard = Cupboard()
    coffee_express = CoffeeExpress()
    coffee_express.load(cupboard=cupboard)

    for _ in range(10):
        coffee_express.make_coffe()
        coffee_express.status()
