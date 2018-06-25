from attacks.AttacksInfo import *
from attacks.StatusEffects import *

class ElectrifyingNet(Attack):
    def __init__(self):
        desc = "An invisible electric net traps you in the water pulsing 500 volts through your body!"
        super().__init__("Electrifying Net", desc, damage=5, atkType=AttackTypes.Normal,
                         statusEffects=[Stun(stunDuration=1, chance=100)], manaCost=0)

    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_isAlive(targets)

class StickySeaweed(Attack):
    def __init__(self):
        desc = "You have been trapped in some sticky seaweed, pulling you down into the depths of the ocean!"
        super().__init__("Sticky Seaweed", desc, damage=5, atkType=AttackTypes.Normal,
                         statusEffects=[Stun(stunDuration=1, chance=100)], manaCost=0)

class CatastrohpicClam(Attack):
    def __init__(self):
        desc = "A large clam slams shut, trapping you inside! And there is no pearl in this clam!"
        super().__init__("Catastrophic Clam", desc, damage=5, atkType=AttackTypes.Normal,
                         statusEffects=[Paralyze(paralyzeDuration=1, chance=100)], manaCost=0)