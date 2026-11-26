from abc import ABC,abstractmethod
from Products.Customer import Customer

class AppBuilder(ABC):

    @property
    @abstractmethod
    def result(self) -> Customer:
        pass

    @abstractmethod
    def setFirstName(self) -> None: 
        pass

    @abstractmethod
    def setLastName(self) -> None:
        pass

    @abstractmethod
    def setPrimaryEmail(self) -> None:
        pass

    @abstractmethod
    def setPrimaryPhone(self) -> None:
        pass

    #Below are optional items. WebApp wants all, mobile doesnt
    
    def setMiddleName(self) -> None:
        pass

    def setSecondaryEmail(self) -> None:
        pass

    def setSecondaryPhone(self) -> None:
        pass