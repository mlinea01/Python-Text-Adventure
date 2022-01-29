from Battle import *
from adventures.MountainCaves.Enemies import *
from adventures.Adventures import Adventure
from adventures.MountainCaves.Traps import *
from items.Potions import *
import threading
from time import sleep
from adventures.Merchant import Merchant


class MountainAdventure:
    def __init__(self, players):
        self.players = players

        map_data = []
        self.adventure = Adventure(self.players, map_data, 0, 0)

        self.traps = [StoneStakes(), BoulderMace(), PillarLaunch()]

    def get_primary_player(self, players):
        result = 0
        for player in players:
            if player.hp > 0:
                return result
            else:
                result += 1

    def Mountain_merchant(self):
        IO.print_text("A merchant sits in a dark cave on the edge of the mountain. You go inside...")
        merchant = Merchant(items_list=[HealthPotion(), ManaPotion()],
                            greeting="This mountain speaks to our souls, showing us what life is about!",
                            sales_pitch="Perhaps these will give you sustenance. What would you like?",
                            goodbye="Farewell, and beware.")
        merchant.greet(self.players[0])

    def empty(self):
        IO.print_text(
            "This area is empty. Fred wasn't sure what to put here, but wanted to put something as a proof of concept.")

    def camp(self):
        IO.print_text("Look! There is a camp up ahead, Let's check it out and see if we can find any clues!")
        IO.print_text("")
        time.sleep(1)
        self.item_loot()

    def item_loot(self):
        potions = [HealthPotion, ManaPotion, SpeedPotion, DamagePotion]
        search = random.randint(1, 8)

        if search <= 4 and self.adventure.already_visited() is False:
            IO.print_text("You found an item!")
            item = potions[search - 1]()
            IO.print_text("You found a " + item.name)
            self.players[self.get_primary_player(self.players)].items.append(item)
            self.adventure.mark_visited()

        elif self.adventure.already_visited():
            IO.print_text("The place has been ransacked! Looks like there's nothing left.")
        else:
            IO.print_text("There are no items here, Let's see if we can find any clues.")

    def hit_trap(self):
        if self.adventure.already_visited() is False:
            traps = random.randint(1, 4)
            trap = self.traps[traps - 1]
            self.activePlayers = copy(self.players)
            TargetFilters.target_filter_isAlive(self.activePlayers)

            for player in self.players:
                intro_thread = threading.Thread(target=self.player_hit_by_trap, args=[player, trap])
                intro_thread.start()
        else:
            IO.print_text("Theres that trap you got caught in! Let's not do that again!")

        while len(self.activePlayers) > 0:
            sleep(0.5)

    def player_hit_by_trap(self, player, trap):
        jump = IO.get_input(player.player_num, "Theres a " + trap.name + ", Type 'jump' to avoid the trap!!!!!!!!!",
                            time_out=50)
        IO.print_text(" ")
        if jump != "jump":
            print(trap.desc)
            player.hit_by(trap)
            time.sleep(2)
            self.adventure.mark_visited()
        else:
            print("You avoided the trap! I almost peed my pants!")
        self.adventure.mark_visited()
        self.activePlayers.remove(player)

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