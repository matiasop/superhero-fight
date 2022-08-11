from random import choice

from team import Team
from superhero import Superhero


class Simulation:
    def __init__(self) -> None:
        self.teams: list[Team] = []
        self.current_team: int = 0
        self.winner_team: int = None

        self.create_teams()

    def create_teams(self) -> None:
        for team_id in range(2):
            print(f"Reclutando los miembros del equipo {team_id}")
            self.teams.append(Team())
            print(f"Los miembros del equipo {team_id} son:")
            for superhero in self.teams[team_id].team:
                print(superhero)
            print()

    def start(self) -> None:
        print("La batalla ha comenzado")

        while self.fight_continues():
            print(f"Es turno del equipo {self.current_team}")

            attacker: Superhero = self.choose_alive_member(self.current_team)
            defender: Superhero = self.choose_alive_member(self.other_team())

            self.attack(attacker, defender)

            self.current_team = self.other_team()

        self.winner_team = self.other_team()
        print("\n", "La pelea ha terminado")

        self.summary()

    def fight_continues(self) -> bool:
        for team in self.teams:
            if not team.is_someone_alive():
                return False
        return True

    def other_team(self) -> int:
        return (self.current_team + 1) % 2

    def choose_alive_member(self, team_index: int) -> Superhero:
        return choice(self.teams[team_index].alive_members)

    def attack(self, attacker: Superhero, defender: Superhero) -> None:
        ATTACK_OPTIONS: list[str] = ["mental", "strong", "fast"]
        attack_type = choice(ATTACK_OPTIONS)
        damage: float = attacker.compute_damage(attack_type)
        defender.get_damaged(damage)

        print(f"{attacker} va a inflingir {round(damage, 0)} de daño a {defender} usando ataque tipo {attack_type}")

        if defender.hp == 0:
            self.teams[self.other_team()].remove_member(defender)
            print(f"{defender} ha muerto")

    def summary(self) -> str:
        message: str = "Resumen\n"
        for team_id in range(2):
            message += f"Estado final del equipo {team_id}:\n"
            for superhero in self.teams[team_id].team:
                if superhero.hp == 0:
                    message += f"id: {superhero.id}, name: {superhero.name}, Dead\n"
                else:
                    message += f"id: {superhero.id}, name: {superhero.name}, hp: {round(superhero.hp, 0)}\n"
            message += "\n"

        message += "Equipo Vencedor: "
        message += f"{self.winner_team}"

        print(message)
