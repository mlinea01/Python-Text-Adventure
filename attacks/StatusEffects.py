# This module is for status effects usually applied by attacks (i.e. shields, poison, stuns, etc.)


class Shield:
    def __init__(self, shieldAmount, chance=100):
        self.name = "Shielded"
        self.amount = shieldAmount
        self.chance = chance


class Stun:
    def __init__(self, stunDuration, chance=100):
        self.name = "Stunned"
        self.duration = stunDuration
        self.chance = chance


class Blind:
    def __init__(self, blindDuration, chance=100):
        self.name = "Blinded"
        self.duration = blindDuration
        self.chance = chance


class Bleed:
    def __init__(self, bleedDuration, chance=100):
        self.name = "Bleeding"
        self.duration = bleedDuration
        self.chance = chance


class Paralyze:
    def __init__(self, paralyzeDuration, chance=100):
        self.name = "Paralyzed"
        self.duration = paralyzeDuration
        self.chance = chance


class Slow:
    def __init__(self, slowDuration, chance=100):
        self.name = "Slowed"
        self.duration = slowDuration
        self.chance = chance
