from decouple import config
from random import choice
from typing import List

from team import Team
from superhero import Superhero
from mailer import Mailer


class Simulation:
    def __init__(self) -> None:
        self.teams: List[Team] = []
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

        print(self.summary(html=False))

        Mailer.send_summary(self.summary(html=True))
        print(f"Mail sent to {config('RECEIVER_MAIL_ADDRESS')}")

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
        ATTACK_OPTIONS: List[str] = ["mental", "strong", "fast"]
        attack_type = choice(ATTACK_OPTIONS)
        damage: float = attacker.compute_damage(attack_type)
        defender.get_damaged(damage)

        print(f"{attacker} va a inflingir {round(damage, 0)} de daño a {defender} usando ataque tipo {attack_type}")

        if defender.hp == 0:
            self.teams[self.other_team()].remove_member(defender)
            print(f"{defender} ha muerto")

    def add_html_tag(self, text: str, html: bool, tag: str, new_line: bool = True) -> str:
        result: str = ""
        if html:
            result += f"<{tag}>{text}</{tag}>"
        else:
            result += text
        if new_line:
            result += "\n"
        return result

    def summary(self, html: bool) -> str:
        message: str = self.add_html_tag("Resumen", html, "h1")
        for team_id in range(2):
            message += self.add_html_tag(
                f"Estado final del equipo {team_id}:", html,  "h2")
            for superhero in self.teams[team_id].team:
                if superhero.hp == 0:
                    message += self.add_html_tag(
                        f"id: {superhero.id}, name: {superhero.name}, Dead", html, "p", new_line=not html)
                else:
                    message += self.add_html_tag(
                        f"id: {superhero.id}, name: {superhero.name}, hp: {round(superhero.hp, 0)}", html, "p", new_line=not html)

        message += "\n"
        message += self.add_html_tag(
            f"Equipo Vencedor: {self.winner_team}", html, "b")

        return message
