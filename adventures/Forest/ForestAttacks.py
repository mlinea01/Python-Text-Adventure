from attacks.AttacksInfo import *
from attacks.StatusEffects import *


class ForestAttacks:
    class StickyWeb(Attack):
        def __init__(self):
            name = "Sticky Web"
            desc = "Shoots sticky web."
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Normal, statusEffects=[Paralyze(
                paralyzeDuration=1, chance=60)], manaCost=0)

    class SweetScent(Attack):
        def __init__(self):
            name = "Sweet Scent"
            desc = "Lures the enemy in."
            super().__init__(name, desc, damage=0, atkType=AttackTypes.Normal, statusEffects=charmed(1, 100), manaCost=0)

    class Devour(Attack):
        def __init__(self):
            name = "Devour"
            desc = "Devours enemy whole!"
            super().__init__(name, desc, damage=7, atkType=AttackTypes.Normal, statusEffects=[], manaCost=0)

        def filter_targets(self, attacker, targets):
            targetIndex = 0
            while targetIndex < len(targets):
                target = targets[targetIndex]
                is_charmed = False
                for status_effect in target.status_effects:
                    if status_effect.name == "charmed":
                        is_charmed = True

                if is_charmed:
                    targets.remove(target)
                else:
                    targetIndex += 1

    class Slap(Attack):
        def __init__(self):
            name = "Slap"
            desc = "A mighty slap!"
            super().__init__(name, desc, damage=3, atkType=AttackTypes.Normal, statusEffects=[], manaCost=0)
