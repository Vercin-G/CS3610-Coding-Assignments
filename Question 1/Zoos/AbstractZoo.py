from abc import ABC, abstractmethod
from Animals.IAnimal import IAnimal

class Zoo(ABC):

    def __init__(self, name:str):
        self.name: str = name
        self.animals: list[IAnimal] = self.createAnimals()

    @abstractmethod
    def createAnimals(self) -> list[IAnimal]:
        pass

    #though the assignment states this is not an abstract, it is far more logical to make it so.
    @abstractmethod
    def getItinery(self) -> str:
        pass

    def showAnimals (self) -> None:
        string = "Animals: "
        for animal in self.animals:
            string = string + animal.species + " "
        print(string)


