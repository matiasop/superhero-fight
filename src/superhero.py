from ctypes import alignment
from random import randint
from typing import Any


class Superhero:

    def __init__(self, id: int, name: str, powerstats: dict[str, int], alignment: str) -> None:
        self.id: int = id
        self.name: str = name

        self.intelligence: int = powerstats["intelligence"]
        self.strength: int = powerstats["strength"]
        self.speed: int = powerstats["speed"]
        self.durability: int = powerstats["durability"]
        self.power: int = powerstats["power"]
        self.combat: int = powerstats["combat"]
        self.alignment: str = alignment

        self.actual_stamina: int = randint(0, 10)
