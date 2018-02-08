from attacks import BasicAttacks
from characters import CharacterInfo


# Player class used to keep track of player stats and actions
class Player(CharacterInfo.Character):
    def __init__(self):
        super().__init__(name="", desc="", hp=10, mana=10, speed=5, attacks=[BasicAttacks.Punch(), BasicAttacks.Block()])
