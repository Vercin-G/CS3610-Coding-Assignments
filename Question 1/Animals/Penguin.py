from Animals.IAnimal import IAnimal

class Penguin(IAnimal):

    species: str = "Penguin"

    def say(self) -> str:
        return "NOOT! NOOT!"