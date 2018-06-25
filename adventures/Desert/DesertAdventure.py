from Battle import *
from adventures.Desert.Enemies import *
from adventures.Adventures import *


class DesertAdventure:
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

    def antagonsticArmadillo_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("Is that a huge ball rolling around the desert? OMG IT'S AN ARMADILLO, RUN!!!")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, AntagonisticArmadillo()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players), "Wow that armadillo had me rollin! No pun intended!")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
              IO.print_text("Oh god we came back to the armadillo! lets run before backup shows up!!!")
              IO.print_text("If you really think you missed something, keep looking but i'm scared!")

    def chaoticCactus_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("Oh look a cactus, maybe we can get some juice i'm thirsty! OH CRAP IT'S MOVING!")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, ChaoticCactus()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players), "Well we survived but i'm still thirsty!")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("Well there is that cactus that tried to kill us again!")
            IO.print_text("I guess we can look around a bit more, maybe we'll find some juice!")

    def tantalizingTremor_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("OMG it's a tremor!!! its tough has teeth, THIS IS MY NIGHTMORE!!!")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, TantalizingTremor()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players), "Ok, if we see one of those again I will cry!")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("It's the tremor again...I'm not scared, you're scared!...Shut up!")
            IO.print_text("I'm not so sure i want to be here.  Is it on me? i feel like it's on me!")