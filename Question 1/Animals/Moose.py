from Animals.IAnimal import IAnimal

class Moose(IAnimal):

    species: str = "Moose"

    def say(self) -> str:
        return "Moo!"