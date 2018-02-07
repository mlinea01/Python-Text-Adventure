# This module is for status effects usually applied by attacks (i.e. shields, poison, stuns, etc.)


class Shield:
    def __init__(self, shieldAmount):
        self.amount = shieldAmount


class Stun:
    def __init__(self, stunDuration):
        self.duration = stunDuration


class Blind:
    def __init__(self, blindDuration):
        self.duration = blindDuration
