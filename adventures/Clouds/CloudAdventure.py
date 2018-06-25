from Battle import *
from adventures.Clouds.Enemies import *
from adventures.Adventures import *


class CloudAdventure:
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

    def unluckyLeprechaun_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("Hey look a leprechaun! You think he'll give us some gold?")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, UnluckyLeprechaun()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players),
                             "Ok, he didn't give us gold!")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("Oh look it's the leprechaun again!")
            IO.print_text("I know we didn't find anything before, but there may be gold here")

    def hideousHippogryph_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("Holy crap what is that? I saw something on the discovery channel about a hippogryph,"
                          " I think that's what that is!!")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, HideousHippogryph()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players), "Ok that was creep! I don't think we're in kansas anymore")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("Hey look it's that hippogryph, i guess i still didn't wake up from this dream!")
            IO.print_text("Well since i'm clearly dreaming, lets look for a million dollars")

    def crazyCockatrice_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("Look a Cockatrice! It almost looks like the beast from never ending story, but not!")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, CrazyCockatrice()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players), "Welp, it was definitely meaner than the beast from never ending story!")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("Hey look its the never ending story monster, the umm...Cockatrice!")
            IO.print_text("I'm pretty sure we cleared this camp out!")