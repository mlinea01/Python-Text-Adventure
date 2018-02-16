# Base class for traps that may appear throughout the adventure.
class Traps:

    def __init__(self, name, desc, damage, duration):
        self.name = name
        self.desc = desc
        self.damage = damage
        self.duration = duration
