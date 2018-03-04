import adventures.ItemsInfo
from attacks import StatusEffects
from characters.CharacterRace import *

class HealthPotion(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("Health Potion", "Restores missing health")

    def use_item_on(self, character):
        character.hp += 10

        if character.hp > character.maxHp:
            character.hp = character.maxHp


class ManaPotion(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("Mana Potion", "Replenishes 10 points of mana")

    def use_item_on(self, character):
        character.mana += 10

        if character.mana > character.maxMana:
            character.mana = character.maxMana



class SpeedPotion(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("Speed Potion", "Increases speed for a short duration")

    def use_item_on(self, character):
        character.speed += 10


class DamagePotion(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("Damage Potion", "Increases damage for a short duration")

    def use_item_on(self, character):
        character.status_effect_add(StatusEffects.DamageBoost(amount=10, duration=3))