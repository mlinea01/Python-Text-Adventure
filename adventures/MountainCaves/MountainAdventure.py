from Battle import *
from adventures.MountainCaves.Enemies import *
from adventures.Adventures import Adventure


class MountainAdventure:
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

    def dragon_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("There is a Mountain Dragon in the camp, Hurry, take that dragon down!")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, MountainDragon()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players), "Woah that dragon was tough! Now that that's over lets take a look around this camp.")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("The slain Mountain Dragon lies in the middle of the camp.")
            IO.print_text("The wind blows steadily from the mountains to the East, but there is nothing else here.")

    def golem_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("Have you ever seen a golem? No? There's one right there!")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, Golem()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players), "I mean this is getting ridiculous! A golem? really?")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("Oh hey look it's that golem again! I really hope it's dead, i mean how do you know? hes all rock!")
            IO.print_text("I think we got everything, so to be safe, let's just leave!")

    def maliciousMountainLion_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("Is that a mountain lion? I knew i shouldn't have come this way!")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, MaliciousMountainLion()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players), "Ok, could have been worse. I may have rabies but i'll be fine!")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("Look, it's that mountain lion that bit me! I think we should leave, his friends are probably close!")
            IO.print_text("This place is clean, let's move fast!")