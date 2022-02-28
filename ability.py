import math

class Stat:
    def __init__(self, name, value):
        self.name = name
        self.value = int(value)
    
    def modifier(self, value):
        return math.floor((value - 10)/2)

class Ability(Stat):
    def __init__(self, name, value):
        super().__init__(name, value)
    
class Skill:
    def __init__(self, name, parent_ability):
        self.name = name
        self.parent_ability = parent_ability
    
    @property
    def value(self):
        return self.parent_ability

    @value.setter
    def add_proficiency(self, proficiency_bonus):
        self.parent_ability += proficiency_bonus
    
