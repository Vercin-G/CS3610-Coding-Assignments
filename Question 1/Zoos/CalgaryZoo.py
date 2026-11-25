from Zoos.AbstractZoo import Zoo
from Animals.IAnimal import IAnimal
from Animals.Moose import Moose
from Animals.GrizzlyBear import GrizzlyBear
from Animals.Penguin import Penguin
from Animals.PolarBear import PolarBear

class CalgaryZoo(Zoo):

    def __init__(self, name: str = "Calgary Zoo"):
        super().__init__(name)

    def createAnimals(self) -> list[IAnimal]:
        return [Penguin(), PolarBear(), GrizzlyBear(), Moose()]

    def getItinery(self):
        return "Welcome to " + self.name + "! \n 1. Penguin Plunge \n 2. Wild Canada"
