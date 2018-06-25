from attacks.AttacksInfo import *
from attacks.StatusEffects import *


class HuggingCactus(Attack):
    def __init__(self):
        desc = "A cactus wraps it's limbs around you, giving you a very pointy, very tight hug!"
        super().__init__("Hugging, Cactus", desc, damage=5, atkType=AttackTypes.Normal,
                         statusEffects=[Bleed(bleedDuration=1, chance=100)], manaCost=0)

    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_isAlive(targets)


class QuickSand(Attack):
    def __init__(self):
        desc = "A pool of quicksand sucks you under as you struggle to break free"
        super().__init__("Quicksand", desc, damage=5, atkType=AttackTypes.Normal,
                         statusEffects=[Paralyze(paralyzeDuration=1, chance=100)], manaCost=0)

    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_isAlive(targets)


class Mirage(Attack):
    def __init__(self):
        desc = "A mirage appears looking like an amazing pool of clear water, you jump in only to find out its a hole!"
        super().__init__("Mirage", desc, damage=5, atkType=AttackTypes.Normal, statusEffects=[], manaCost=0)

    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_isAlive(targets)
