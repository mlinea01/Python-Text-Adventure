import adventures.ItemsInfo
from attacks import StatusEffects

class HealthPotion(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("Health Potion", healthRestore=10, manaRestore=0, spdIncrease=0, dmgIncrease=0)

    def use_item_on(self, character):
        character.hp += 10


class ManaPotion(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("Mana Potion", healthRestore=0, manaRestore=10, spdIncrease=0, dmgIncrease=0)

    def use_item_on(self, character):
        character.mana += 10


class SpeedPotion(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("Speed Potion", healthRestore=0, manaRestore=0, spdIncrease=5, dmgIncrease=0)

    def use_item_on(self, character):
        character.speed += 10


class DamagePotion(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("Damage Potion", healthRestore=0, manaRestore=0, spdIncrease=0, dmgIncrease=5)

    def use_item_on(self, character):
        character.status_effect_add(StatusEffects.DamageBoost(amount=10, duration=3))