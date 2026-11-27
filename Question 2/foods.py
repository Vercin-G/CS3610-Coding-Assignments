from abstractfoods import Burger, Pizza, Noodles, Cutlet


class NonVegPizza(Pizza):
    def __init__(self, price, cals, size, descr):
        self.__price = price
        self.__calories = cals
        self.__size = size
        self.__descr = descr


class VegPizza(Pizza):

    def __init__(self, price, cals, size, descr):
        self.__price = price
        self.__calories = cals
        self.__size = size
        self.__descr = descr

    def showVegPizzaAdver(self):
        return "I am a Vegetarian Pizza"

class NonVegBurger(Burger):
    def __init__(self, price, cals, descr):
        self.__price = price
        self.__calories = cals
        self.__descr = descr

class VegBurger(Burger):
    def __init__(self, price, cals, descr):
        self.__price = price
        self.__calories = cals
        self.__descr = descr

    def showVegBurgerAdver(self):
        return "I am a Vegetarian Burger"

class NonVegNoodles(Noodles):
    def __init__(self, price, cals, descr):
        self.__price = price
        self.__calories = cals
        self.__descr = descr

class VegNoodles(Noodles):
    def __init__(self, price, cals, descr):
        self.__price = price
        self.__calories = cals
        self.__descr = descr

    def showVegNoodlesAdver(self):
        return "I am Vegetarian Noodles"

class NonVegCutlet(Cutlet):
    def __init__(self, price, cals, descr):
        self.__price = price
        self.__calories = cals
        self.__descr = descr
