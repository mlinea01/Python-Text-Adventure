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