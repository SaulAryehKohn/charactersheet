from typing import Dict
from ability import Ability, Skill

class AbilityBlock:
    
    def __init__(self, stat_dict: Dict[str, int], proficiency_bonus: int):
        # set base values
        self.strength = Ability("strength", stat_dict.get("str", 10))
        self.dexterity = Ability("dexterity", stat_dict.get("dex", 10))
        self.constitution = Ability("constitution", stat_dict.get("con", 10))
        self.intelligence = Ability("intelligence", stat_dict.get("int", 10))
        self.wisdom = Ability("wisdom", stat_dict.get("wis", 10))
        self.charisma = Ability("charisma", stat_dict.get("cha", 10))
        abilities = [self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma]

        # define skill dependencies
        strength_skills = ["athletics",]
        dexterity_skills = ["acrobatics", "sleight_of_hand", "stealth"]
        constitution_skills = []
        intelligence_skills = ["history", "investigation", "nature", "religion"]
        wisdom_skills = ["insight", "medicine", "perception", "survival"]
        charisma_skills = ["deception", "intimidation", "performance", "persuasion"]
        skills = [strength_skills, dexterity_skills, constitution_skills, intelligence_skills, wisdom_skills, charisma_skills]
        
        self.skill_dict = {}
        for (sk_list, ab) in zip([skills, [skills, abilities]]):
            for sk in sk_list:
                self.skill_dict[sk] = Skill(sk, ab)

        self.initiative = self.dexterity.modifier
        self.passive_perception = 10 + self.wisdom.modifier
        self.proficiency_bonus = proficiency_bonus

    def apply_proficiency(self, skill_name):
        self.skill_dict[skill_name].add_proficiency(self.proficiency_bonus)
    

