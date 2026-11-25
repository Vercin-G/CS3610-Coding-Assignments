from Zoos.AbstractZoo import Zoo
from Animals.IAnimal import IAnimal
from Animals.Lion import Lion
from Animals.Elephant import Elephant
from Animals.Penguin import Penguin
from Animals.PolarBear import PolarBear

class TorontoZoo(Zoo):

    def __init__(self, name: str = "Toronto Zoo"):
        super().__init__(name)

    def createAnimals(self) -> list[IAnimal]:
        return [Lion() ,Elephant() , Penguin(), PolarBear()]

    def getItinery(self):
        return "Welcome to " + self.name + "! \n 1. African Savanna \n 2. Tundra Trek"
