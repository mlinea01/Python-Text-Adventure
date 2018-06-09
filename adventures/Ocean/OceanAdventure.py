from Battle import *
from adventures.Ocean.Enemies import *
from adventures.Adventures import Adventure


class OceanAdventure:
    def __init__(self, players):
        self.players = players

        map_data = []
        self.adventure = Adventure(self.players, map_data, 0, 0)

    def get_primary_player(self, players):
        result = 0
        for player in players:
            if player.hp > 0:
                return result
            else:
                result += 1

    def giantSquid_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("What is that coming out of the water? NO! its a giant squid!!!")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, GiantSquid()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players), "That squid almost had us! And you wanted to take a boat!")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("Whats that smell? Smells like rotten fish! oh its that squid!")
            IO.print_text("If you want to look around go for it, ")