from Client import Client
from Zoos.TorontoZoo import TorontoZoo
from Zoos.CalgaryZoo import CalgaryZoo

toronto = TorontoZoo()
calgary = CalgaryZoo()

client = Client()

client.addZoo(toronto)
client.addZoo(calgary)

activeZoo = client.selectZoo(toronto.name)
print(activeZoo.getItinery())
activeZoo.showAnimals()

activeZoo = client.selectZoo(calgary.name)
print(activeZoo.getItinery())
activeZoo.showAnimals()