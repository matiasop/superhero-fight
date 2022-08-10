from functools import reduce
from random import randint
from typing import Any

from superhero import Superhero
from superhero_api_caller import SuperheroAPICaller


class Team:
    def __init__(self) -> None:
        self.team_size: int = 5
        self.team_ids: set[int] = set()
        self.team: list[Superhero] = []
        self.alive_members: list[Superhero] = []
        self.team_alignment: str = None

        self.create_team()
        self.find_team_alignment()
        self.compute_team_real_stats()

    def create_team(self) -> None:
        while len(self.team_ids) < self.team_size:
            MAX_ID: int = 700
            id: int = randint(0, MAX_ID)
            if id in self.team_ids:
                continue

            name = SuperheroAPICaller.get_name(id)
            powerstats = SuperheroAPICaller.get_powerstats(id)
            alignment = SuperheroAPICaller.get_alignment(id)

            if powerstats is None or alignment is None:
                continue

            superhero: Superhero = Superhero(id, name, powerstats, alignment)
            self.team_ids.add(id)
            self.team.append(superhero)
            self.alive_members.append(superhero)

    def find_team_alignment(self) -> None:
        good_counter: int = 0
        for superhero in self.team:
            if superhero.alignment == "good":
                good_counter += 1

        self.team_alignment = "good" if good_counter >= 3 else "bad"

    def compute_team_real_stats(self) -> None:
        for superhero in self.team:
            superhero.compute_all_stats(self.team_alignment)

    def is_someone_alive(self) -> bool:
        superheroes_hp: list[int] = [superhero.hp for superhero in self.team]
        total_hp: int = reduce(lambda a, b: a + b, superheroes_hp)
        return total_hp > 0
