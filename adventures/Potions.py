import adventures.ItemsInfo


class HealthPotion(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("Health Potion", healthRestore=10, manaRestore=0, spdIncrease=0, dmgIncrease=0)


class ManaPotion(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("Mana Potion", healthRestore=0, manaRestore=10, spdIncrease=0, dmgIncrease=0)


class SpeedPotion(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("Speed Potion", healthRestore=0, manaRestore=0, spdIncrease=5, dmgIncrease=0)


class DamagePotion(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("Damage Potion", healthRestore=0, manaRestore=0, spdIncrease=0, dmgIncrease=5)
