from Battle import *
from adventures.Ocean.Enemies import *
from adventures.Adventures import Adventure
from adventures.Ocean.Traps import *
from items.Potions import *
import threading
from time import sleep
from adventures.Merchant import Merchant


class OceanAdventure:
    def __init__(self, players):
        self.players = players

        map_data = []
        self.adventure = Adventure(self.players, map_data, 0, 0)

        self.traps = [ElectrifyingNet(), StickySeaweed(), CatastrohpicClam()]

    def get_primary_player(self, players):
        result = 0
        for player in players:
            if player.hp > 0:
                return result
            else:
                result += 1

    def Ocean_merchant(self):
        IO.print_text("A merchant sits on an island in the middle of the sea. You swim over...")
        merchant = Merchant(items_list=[HealthPotion(), ManaPotion()],
                            greeting="Does the ocean call to you like it calls to me?, bless this deep blue ocean!",
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
            IO.print_text(trap.desc, player.player_num)
            player.hit_by(trap)
            time.sleep(2)
            self.adventure.mark_visited()
        else:
            IO.print_text("You avoided the trap! I almost peed my pants!", player.player_num)
        self.adventure.mark_visited()
        self.activePlayers.remove(player)

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