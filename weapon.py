class Weapon:
    def __init__(self, name: str, weapon_type: str, damage_die: str, finesse: bool = False):
        assert weapon_type in ["melee", "ranged", "melee_or_ranged"]
        self.name = name
        self.weapon_type = weapon_type
        self.damage_die = damage_die
        self.finesse = finesse