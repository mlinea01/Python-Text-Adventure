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
                IO.get_input(self.get_primary_player(self.players),
                             "That squid almost had us! And you wanted to take a boat!")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("Whats that smell? Smells like rotten fish! oh its that squid!")
            IO.print_text("If you want to look around go for it, ")

    def megalodonShark_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("Ok I know it's supposed to be a myth but i think that's a megalodon!")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, MegalodonShark()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players),
                             "Ok that was scary, I'm not crying it's from the ocean!")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("Oh my jesus its the shark! The waters just warm here, don't look at me!")
            IO.print_text("maybe we should just go!")

    def petrifyingPiranha_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("Ok its a huge piranha, I'm not saying we're screwed, but we're screwed!")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, PetrifyingPiranha()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players),
                             "I LIVED! YES!! i may or may not have lost a finger!")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("Ok i think that's the piranha again! oh hey look it's a rainbow, lets go this way!")
            IO.print_text("There's nothing here, I looked!")