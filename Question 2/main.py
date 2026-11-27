from factories import *
from abstractfoods import *

class FoodApp:
    def __init__(self):
        self._AvailableFood: dict[str, ProductFactory] = {
            "NonVeg": NonVegProductFactory(),
            "Veg": VegProductFactory()
        }

    def makeOrder(self, prodNames: list[str]) -> list[iProduct]:

        order = []

        for name in prodNames:

            dietFamily, foodType = name.split("_")
            factory = self._AvailableFood[dietFamily]

            if foodType == "Burger":
                item = factory.createBurger(5, 800, "Burger")

            if foodType == "Pizza":
                item = factory.createPizza(5, 450, "Pizza")

            else:
                raise ValueError("Unknown Product")

            order.append(item)

        return order

    def getOrderDescription(self, order: list[iProduct]) -> str:

        result = ""

        for product in order:
            result += (
                f"{product.get_Description()}: "
                f"${product.get_Price()}\n"
            )

        return result