# This module is for status effects usually applied by attacks (i.e. shields, poison, stuns, etc.)


class Shield:
    def __init__(self, shieldAmount):
        self.name = "Shielded"
        self.amount = shieldAmount


class Stun:
    def __init__(self, stunDuration):
        self.name = "Stunned"
        self.duration = stunDuration


class Blind:
    def __init__(self, blindDuration):
        self.name = "Blinded"
        self.duration = blindDuration


class Bleed:
    def __init__(self, bleedDuration):
        self.name = "Bleeding"
        self.duration = bleedDuration


class Paralyze:
    def __init__(self, paralyzeDuration):
        self.name = "Paralyzed"
        self.duration = paralyzeDuration


class Slow:
    def __init__(self, slowDuration):
        self.name = "Slowed"
        self.duration = slowDuration