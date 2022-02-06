from attacks.AttacksInfo import *
from attacks.StatusEffects import *

class StoneStakes(Attack):
    def __init__(self):
        desc = "You fall into a hole with stakes carved from stone at the bottom, trapping and impaling you"
        super().__init__("Stone Stakes", desc, damage=5, atkType=AttackTypes.Normal,
                         statusEffects=[Bleed(bleedDuration=1, chance=100)], manaCost=0)

    def filter_targets(self, targets):
        TargetFilters.target_filter_isAlive(targets)

class BoulderMace(Attack):
    def __init__(self):
        desc = "A boulder carved into a mace swings from the cave wall smashing you in the face!"
        super().__init__("Boulder Mace", desc, damage=5, atkType=AttackTypes.Normal,
                         statusEffects=[Bleed(bleedDuration=1, chance=100)], manaCost=0)

    def filter_targets(self, targets):
        TargetFilters.target_filter_isAlive(targets)

class PillarLaunch(Attack):
    def __init__(self):
        desc = "A stone pillar springs up from the ground launching you 200 feet into the air!"
        super().__init__("Pillar Launch", desc, damage=5, atkType=AttackTypes.Normal,
                         statusEffects=[Stun(stunDuration=1, chance=100)], manaCost=0)