import adventures.TrapsInfo


class Hole(adventures.TrapsInfo.Traps):
    def __init__(self):
        desc = "You fell into a huge hole! It may be tough to get out. "
        super().__init__("Hole", desc, damage=1, duration=1)


class Net(adventures.TrapsInfo.Traps):
    def __init__(self):
        desc = "A net fell from above you and trapped you underneath!"
        super().__init__("Net", desc, damage=0, duration=1)


class BarbedWire(adventures.TrapsInfo.Traps):
    def __init__(self):
        desc = "You just ran into Barbed wire and cut yourself! We need to find another way around."
        super().__init__("Barbed Wire", desc, damage=2, duration=1)


class BearTrap(adventures.TrapsInfo.Traps):
    def __init__(self):
        desc = "Your leg is caught in a bear trap! Get out quick before you bleed to death!"
        super().__init__("Bear Trap", desc, damage=2, duration=1)