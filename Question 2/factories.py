from foods import *
from abc import ABC, abstractmethod

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

    def createNoodles(self, p, c, d) -> NonVegNoodles:
        return NonVegNoodles(self, p, c, d)

    def createCutlet(self, p, c, d) -> NonVegCutlet:
        return NonVegCutlet(self, p, c, d)

class VegProductFactory(ProductFactory):
    def createBurger(self, p, c, d) -> VegBurger:
        return VegBurger(self, p, c, d)

    def createPizza(self, p, c, s, d) -> VegPizza:
        return VegPizza(self, p, c, s, d)

    def createNoodles(self, p, c, d) -> VegNoodles:
        return VegNoodles(self, p, c, d)
