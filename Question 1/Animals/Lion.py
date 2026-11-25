from Animals.IAnimal import IAnimal

class Lion(IAnimal):

    species: str = "Lion"

    def say(self) -> str:
        return "Roaaar!"