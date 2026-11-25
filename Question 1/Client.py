from Zoos.AbstractZoo import Zoo

class Client:
    def __init__(self) -> None:
        self._availableZoos: list[Zoo] = []
        self._selectedZoo: Zoo | None = None

    @property
    def availableZoos(self) -> list[Zoo]:
        return self._availableZoos

    @property
    def selectedZoo(self) -> Zoo | None:
        return self._selectedZoo

    def addZoo(self, zoo: Zoo) -> None:
        self._availableZoos.append(zoo)
        if self._selectedZoo is None:
            self._selectedZoo = zoo

    def removeZoo(self, zooName: str) -> None:
        for index, zoo in enumerate(self._availableZoos):
            if zoo.name == zooName:
                removed = self._availableZoos.pop(index)
                if self._selectedZoo is removed:
                    self._selectedZoo = self._availableZoos[0] if self._availableZoos else None
                return

    def selectZoo(self, zooName: str) -> Zoo:
        for zoo in self._availableZoos:
            if zoo.name == zooName:
                self._selectedZoo = zoo
                return zoo
        raise ValueError(f"Zoo '{zooName}' not found.")