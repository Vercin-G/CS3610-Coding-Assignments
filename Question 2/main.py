from abc import ABC, abstractmethod

print("Hello There\n")
print("General Kenobi")

#ProductFactory is an aggregation of FoodApp

#VegProductFactory is a Realization/Implementation of ProductFactory
#NonVegProductFactory is a Realization/Implementation of ProductFactory

#VegPizza is associated with VegProductFactory
#NonVegPizza is associated with NonVegProductFactory

#VegPizza is an Implementation of Pizza
#NonVegPizza is an Implementation of Pizza

#VegBurger is an implementation of Burger
#NonVegBurger is an implementation of Burger

#Pizza and Burger inherit from IProduct

#Let's start with our Abstract Products

class iProduct(ABC):

    @abstractmethod
    def get_Price(): int

    @abstractmethod
    def get_Description(): str

class Pizza(iProduct):

    __price = 0
    __calories = 0
    __descr = ""
    __size = "Small"

    def get_Price(self) -> int:
        return self.__price

    def get_Description(self) -> str:
        return self.__descr

class Burger(iProduct):

    __price = 0
    __calories = 0
    __descr = ""

    def get_Price(self) -> int:
        return self.__price

    def get_Description(self) -> str:
        return self.__descr

#And now our concrete variants

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

#Factories !!!

class ProductFactory(ABC):

    @abstractmethod
    def createBurger(self, p, c, d) -> Burger:
        pass

    @abstractmethod
    def createPizza(self, p, c, s, d) -> Pizza:
        pass

class NonVegProductFactory(ProductFactory):
    def createBurger(self, p, c, d) -> NonVegBurger:
        return NonVegBurger(self, p, c, d)

    def createPizza(self, p, c, s, d) -> NonVegPizza:
        return NonVegPizza(self, p, c, s, d)

class VegProductFactory(ProductFactory):
    def createBurger(self, p, c, d) -> VegBurger:
        return VegBurger(self, p, c, d)

    def createPizza(self, p, c, s, d) -> VegPizza:
        return VegPizza(self, p, c, s, d)


