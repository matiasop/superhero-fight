from random import randint, choice


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
        self.filiation_coefficient: float = None
        self.hp: int = None

        self.mental_attack: float = None
        self.strong_attack: float = None
        self.fast_attack: float = None

    def compute_filiation_coefficient(self, team_alignment: str) -> float:
        random_number: int = 1 + randint(0, 9)
        filiation_coefficient = random_number if self.alignment == team_alignment else 1/random_number
        return filiation_coefficient

    def compute_hp(self) -> int:
        stats_average: float = 0.8*self.strength + 0.7*self.durability + self.power
        hp: int = 100 + int(0.5*stats_average*(1 + 0.1*self.actual_stamina))
        return hp

    def compute_real_stat(self, base: int) -> int:
        return int(((2*base + self.actual_stamina)/1.1)*self.filiation_coefficient)

    def compute_mental(self) -> float:
        return self.filiation_coefficient*(0.7*self.intelligence + 0.2*self.speed + 0.1*self.combat)

    def compute_strong(self) -> float:
        return self.filiation_coefficient*(0.6*self.strength + 0.2*self.power + 0.2*self.combat)

    def compute_fast(self) -> float:
        return self.filiation_coefficient*(0.55*self.speed + 0.25*self.durability + 0.2*self.strength)

    def compute_all_stats(self, team_alignment: str) -> None:
        self.filiation_coefficient = self.compute_filiation_coefficient(
            team_alignment)
        self.hp = self.compute_hp()

        self.intelligence = self.compute_real_stat(self.intelligence)
        self.strength = self.compute_real_stat(self.strength)
        self.speed = self.compute_real_stat(self.speed)
        self.durability = self.compute_real_stat(self.durability)
        self.power = self.compute_real_stat(self.power)
        self.combat = self.compute_real_stat(self.combat)

        self.mental_attack = self.compute_mental()
        self.strong_attack = self.compute_strong()
        self.fast_attack = self.compute_fast()

    def compute_damage(self, attack_option) -> float:
        damage: float
        if attack_option == "mental":
            damage = self.mental_attack
        elif attack_option == "strong":
            damage = self.strong_attack
        elif attack_option == "fast":
            damage = self.fast_attack
        return damage

    def get_damaged(self, damage: float) -> None:
        if damage >= self.hp:
            self.hp = 0
        else:
            self.hp -= damage

    def __repr__(self) -> str:
        return f"{self.name} (hp: {round(self.hp, 0)})"
