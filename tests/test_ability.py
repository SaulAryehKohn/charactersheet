from ability import Stat, Ability, Skill
from pytest import mark

mark.parametrize("input,expected", [(6, -2), (7, -2), (8, -1), (9, -1), (10, 0), (11, 0), (12, 1), (13, 1), (14, 2)])
def test_stat_modifier(input, expected):
    stat = Stat("a", input)
    assert stat.modifier == expected
