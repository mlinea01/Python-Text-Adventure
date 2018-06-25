from attacks.AttacksInfo import *
from attacks.StatusEffects import *

class RainbowRope(Attack):
    def __init__(self):
        desc = "A rainbow has wrapped itself around you, making it hard to move!"
        super().__init__("Rainbow Rope", desc, damage=5, atkType=AttackTypes.Normal, statusEffects=[], manaCost=0)

    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_isAlive(targets)

class LightningDart(Attack):
    def __init__(self):
        desc = "A bolt of lightning in the shape of a dart strikes, leaving you paralyzed!"
        super().__init__("Lightning Dart", desc, damage=5, atkType=AttackTypes.Normal,
                         statusEffects=[Paralyze(paralyzeDuration=1, chance=60)], manaCost=0)

    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_isAlive(targets)

class MeteorBucket(Attack):
    def __init__(self):
        desc = "A meteor in the shape of a bucket slams on top of you, trapping you underneath!"
        super().__init__("Meteor Bucket", desc, damage=5, atkType=AttackTypes.Normal, statusEffects=[], manaCost=0)

    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_isAlive(targets)