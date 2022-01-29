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
        IO.print_text("You see a merchant in the distance, is that a mirage?. You approach with caution...")
        merchant = Merchant(items_list=[HealthPotion(), ManaPotion()],
                            greeting="Don't worry, I am as real as the heat covering this desert!",
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