from Battle import *
from adventures.Desert.Enemies import *
from adventures.Adventures import *
from adventures.Desert.Traps import *
from items.Potions import *
import threading
from time import sleep
from adventures.Merchant import Merchant


class DesertAdventure:
    def __init__(self, players):
        self.players = players

        map_data = []
        self.adventure = Adventure(self.players, map_data, 0, 0)

        self.traps = [HuggingCactus(), QuickSand(), Mirage()]

    def get_primary_player(self, players):
        result = 0
        for player in players:
            if player.hp > 0:
                return result
            else:
                result += 1

    def Desert_merchant(self):
        print("You see a merchant in the distance)
        merchant = Merchant(items_list=[HealthPotion(), ManaPotion()],
                            greeting="Don't worry, I am as real as the heat covering this desert!",
                            sales_pitch="Perhaps these will give you sustenance. What would you like?",
                            goodbye="Farewell, and beware.")
        merchant.greet(self.players[0])

    def empty(self):
        print(
            "This area is empty. Fred wasn't sure what to put here, but wanted to put something as a proof of concept.")

    def camp(self):
        print("Look! There is a camp up ahead)
        print("")
        time.sleep(1)
        self.item_loot()

    def item_loot(self):
        potions = [HealthPotion, ManaPotion, SpeedPotion, DamagePotion]
        search = random.randint(1, 8)

        if search <= 4 and self.adventure.already_visited() is False:
            print("You found an item!")
            item = potions[search - 1]()
            print("You found a " + item.name)
            self.players[self.get_primary_player(self.players)].items.append(item)
            self.adventure.mark_visited()

        elif self.adventure.already_visited():
            print("The place has been ransacked! Looks like there's nothing left.")
        else:
            print("There are no items here)

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
            print("Theres that trap you got caught in! Let's not do that again!")

        while len(self.activePlayers) > 0:
            sleep(0.5)

    def player_hit_by_trap(self, player, trap):
        jump = IO.get_input(player.player_num, "Theres a " + trap.name + ", Type 'jump' to avoid the trap!!!!!!!!!",
                            time_out=50)
        print(" ")
        if jump != "jump":
            print(trap.desc)
            player.hit_by(trap)
            time.sleep(2)
            self.adventure.mark_visited()
        else:
            print("You avoided the trap! I almost peed my pants!")
        self.adventure.mark_visited()
        self.activePlayers.remove(player)

    def antagonsticArmadillo_fight(self):
        if self.adventure.already_visited() is False:
            print("Is that a huge ball rolling around the desert? OMG IT'S AN ARMADILLO)
            time.sleep(2)
            print("")
            if Battle().start(self.players, AntagonisticArmadillo()):
                print("")
                IO.get_input(self.get_primary_player(self.players), "Wow that armadillo had me rollin! No pun intended!")
                print("")
                self.adventure.mark_visited()

        else:
              print("Oh god we came back to the armadillo! lets run before backup shows up!!!")
              print("If you really think you missed something)

    def chaoticCactus_fight(self):
        if self.adventure.already_visited() is False:
            print("Oh look a cactus)
            time.sleep(2)
            print("")
            if Battle().start(self.players, ChaoticCactus()):
                print("")
                IO.get_input(self.get_primary_player(self.players), "Well we survived but i'm still thirsty!")
                print("")
                self.adventure.mark_visited()

        else:
            print("Well there is that cactus that tried to kill us again!")
            print("I guess we can look around a bit more)

    def tantalizingTremor_fight(self):
        if self.adventure.already_visited() is False:
            print("OMG it's a tremor!!! its tough has teeth)
            time.sleep(2)
            print("")
            if Battle().start(self.players, TantalizingTremor()):
                print("")
                IO.get_input(self.get_primary_player(self.players), "Ok, if we see one of those again I will cry!")
                print("")
                self.adventure.mark_visited()

        else:
            print("It's the tremor again...I'm not scared)
            print("I'm not so sure i want to be here.  Is it on me? i feel like it's on me!")