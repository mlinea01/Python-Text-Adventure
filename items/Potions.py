from items.ItemsInfo import Items
from attacks.AttacksInfo import *
from attacks import StatusEffects


class HealthPotion(Items):
    def __init__(self):
        item_attack = Attack(atkType=AttackTypes.Normal, damage=None, desc="", manaCost=0, name="Health Potion",
                             statusEffects=StatusEffects.HpBoost(10))
        item_attack.filter_targets = self.filter_targets
        super().__init__("Health Potion", "Restores missing health", item_attack)

    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_allies(attacker, targets)
        TargetFilters.target_filter_isAlive(targets)


class ManaPotion(Items):
    def __init__(self):
        item_attack = Attack(atkType=AttackTypes.Normal, damage=None, desc="", manaCost=0, name="Mana Potion",
                             statusEffects=StatusEffects.manaBoost(10))
        item_attack.filter_targets = self.filter_targets
        super().__init__("Mana Potion", "Replenishes 10 points of mana", item_attack)

    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_allies(attacker, targets)
        TargetFilters.target_filter_isAlive(targets)


class SpeedPotion(Items):
    def __init__(self):
        item_attack = Attack(atkType=AttackTypes.Normal, damage=None, desc="", manaCost=0, name="Speed Potion",
                             statusEffects=StatusEffects.speedBoost(amount=10, duration=3))
        item_attack.filter_targets = self.filter_targets
        super().__init__("Speed Potion", "Increases speed for a short duration", item_attack)

    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_allies(attacker, targets)
        TargetFilters.target_filter_isAlive(targets)



class DamagePotion(Items):
    def __init__(self):
        item_attack = Attack(atkType=AttackTypes.Normal, damage=None, desc="", manaCost=0, name="Damage Potion",
                             statusEffects=StatusEffects.DamageBoost(amount=10, duration=3))
        item_attack.filter_targets = self.filter_targets
        super().__init__("Damage Potion", "Increases damage for a short duration", item_attack)

    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_allies(attacker, targets)
        TargetFilters.target_filter_isAlive(targets)