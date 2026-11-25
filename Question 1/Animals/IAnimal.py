from abc import ABC, abstractmethod

class IAnimal(ABC):

    @property
    @abstractmethod
    def species(self) -> str:
        pass

    @abstractmethod
    def say(self) -> str:
        pass