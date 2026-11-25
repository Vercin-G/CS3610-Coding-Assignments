from Animals.IAnimal import IAnimal

class PolarBear(IAnimal):

    species: str = "PolarBear"

    def say(self) -> str:
        return "Grrrr"