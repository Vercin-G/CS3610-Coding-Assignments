from Animals.IAnimal import IAnimal

class GrizzlyBear(IAnimal):

    species: str = "GrizzlyBear"

    def say(self) -> str:
        return "Roaaarr!"