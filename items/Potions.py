from attacks.StatusEffects import HpIncrease
from items.ItemsInfo import Items
from attacks import StatusEffects
from attacks.AttacksInfo import *


class HealthPotion(Items):
    def __init__(self):
        item_attack = Attack(atkType=AttackTypes.Normal, damage=None, desc="", manaCost=0, name="Health Potion",
                             statusEffects=HpIncrease(10))
        super().__init__("Health Potion", "Restores missing health", item_attack)

    def use_item_on(self, character):
        character.hp += 10

        if character.hp > character.maxHp:
            character.hp = character.maxHp


class ManaPotion(Items):
    def __init__(self):
        item_attack = Attack(atkType=AttackTypes.Normal, damage=None, desc="", manaCost=0, name="Mana Potion",
                             statusEffects=[])
        super().__init__("Mana Potion", "Replenishes 10 points of mana", item_attack)

    def use_item_on(self, character):
        character.mana += 10

        if character.mana > character.maxMana:
            character.mana = character.maxMana

class SpeedPotion(Items):
    def __init__(self):
        item_attack = Attack(atkType=AttackTypes.Normal, damage=None, desc="", manaCost=0, name="Speed Potion",
                             statusEffects=[])
        super().__init__("Speed Potion", "Increases speed for a short duration", item_attack)

    def use_item_on(self, character):
        character.speed += 10


class DamagePotion(Items):
    def __init__(self):
        item_attack = Attack(atkType=AttackTypes.Normal, damage=None, desc="", manaCost=0, name="Damage Potion",
                             statusEffects=[])
        super().__init__("Damage Potion", "Increases damage for a short duration", item_attack)

    def use_item_on(self, character):
        character.status_effect_add(StatusEffects.DamageBoost(amount=10, duration=3))