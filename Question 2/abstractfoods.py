from abc import ABC, abstractmethod


class iProduct(ABC):

    @abstractmethod
    def get_Price(): int

    @abstractmethod
    def get_Description(): str

class Pizza(iProduct):

    __price = 0
    __calories = 0
    __descr = ""
    __size = "Small"

    def get_Price(self) -> int:
        return self.__price

    def get_Description(self) -> str:
        return self.__descr

class Burger(iProduct):

    __price = 0
    __calories = 0
    __descr = ""

    def get_Price(self) -> int:
        return self.__price

    def get_Description(self) -> str:
        return self.__descr
