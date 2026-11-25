from Animals.IAnimal import IAnimal

class Elephant(IAnimal):

    species: str = "Elephant"

    def say(self) -> str:
        return "Bvaroooomf"