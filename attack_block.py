from typing import Dict
from weapon import Weapon
from ability_block import AbilityBlock

class AttackBlock:
    def __init__(self, weapons_dict: Dict, ability_block: AbilityBlock):
        self.ability_block = ability_block
        self.weapon_block = {w: {} for w in weapons_dict}
        for w,w_data in weapons_dict.items():
            self.weapon_block[w] = Weapon(w, w_data["weapon_type"], w_data["damage_die"])
        self.attack_dict = {w.name: 
            {
                "type": w.weapon_type,
                "to_hit": self.to_hit_value(w),
                "upon_hit": self.damage_code(w)
            }
        }

    def to_hit_value(self, weapon: Weapon):
        melee_bonus = self.ability_block.strength + self.ability_block.proficiency_bonus
        ranged_bonus = self.ability_block.dexterity + self.ability_block.proficiency_bonus
        best_of_two = max(melee_bonus, ranged_bonus)
        if weapon.finesse or weapon.weapon_type == "melee_or_ranged":
            return best_of_two
        if weapon.weapon_type == "melee":
            return melee_bonus
        return ranged_bonus

    def damage_code(self, weapon: Weapon):
        melee_bonus = self.ability_block.strength
        ranged_bonus = self.ability_block.dexterity
        best_of_two = max(melee_bonus, ranged_bonus)
        if weapon.finesse or weapon.weapon_type == "melee_or_ranged":
            modifier =  best_of_two
        if weapon.weapon_type == "melee":
            modifier = melee_bonus
        modifier = ranged_bonus
        if modifier >= 0:
            concat = "+"
        else:
            concat = ""
        return weapon.damage_die + concat + str(modifier)