from Battle import *
from adventures.Ocean.Enemies import *
from adventures.Adventures import Adventure
from adventures.Ocean.Traps import *
from items.Potions import *
from adventures.Merchant import Merchant
from threading import Timer


class OceanAdventure:
    def __init__(self, player):
        self.player = player

        map_data = []
        self.adventure = Adventure(self.players, map_data, 0, 0)

        self.traps = [ElectrifyingNet(), StickySeaweed(), CatastrohpicClam()]

    def Ocean_merchant(self):
        print("A merchant sits on an island in the middle of the sea. You swim over...")
        merchant = Merchant(items_list=[HealthPotion(), ManaPotion()],
                            greeting="Does the ocean call to you like it calls to me?, bless this deep blue ocean!",
                            sales_pitch="Perhaps these will give you sustenance. What would you like?",
                            goodbye="Farewell, and beware.")
        merchant.greet(self.player)

    def empty(self):
        print("This area is empty. Fred wasn't sure what to put here, but wanted to put something as a proof of concept.")

    def camp(self):
        print("Look! There is a camp up ahead, Let's check it out and see if we can find any clues!")
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
            self.player.items.append(item)
            self.adventure.mark_visited()

        elif self.adventure.already_visited():
            print("The place has been ransacked! Looks like there's nothing left.")
        else:
            print("There are no items here, Let's see if we can find any clues.")

    def hit_trap(self):
        if self.adventure.already_visited() is False:
            trap = self.traps[random.randint(0, 3)]
            self.player_hit_by_trap(self.player, trap).start()
        else:
            print("Theres that trap you got caught in! Let's not do that again!")

    def player_hit_by_trap(self, player, trap):
        time_out=50
        timer = Timer(time_out, print, ['Times up!!!'])
        jump = input("Theres a " + trap.name + ", Type 'jump' to avoid the trap!!!!!!!!!")
        timer.start();
        print(" ")
        if jump != "jump":
            print(trap.desc)
            player.hit_by(trap)
            time.sleep(2)
            self.adventure.mark_visited()
        else:
            print("You avoided the trap! I almost peed my pants!")
            timer.cancel()
        self.adventure.mark_visited()

    def giantSquid_fight(self):
        if self.adventure.already_visited() is False:
            print("What is that coming out of the water? NO! its a giant squid!!!")
            time.sleep(2)
            print("")
            if Battle().start(self.player, GiantSquid()):
                print("")
                input(self.player, "That squid almost had us! And you wanted to take a boat!")
                print("")
                self.adventure.mark_visited()

        else:
            print("Whats that smell? Smells like rotten fish! oh its that squid!")
            print("If you want to look around go for it, ")

    def megalodonShark_fight(self):
        if self.adventure.already_visited() is False:
            print("Ok I know it's supposed to be a myth but i think that's a megalodon!")
            time.sleep(2)
            print("")
            if Battle().start(self.player, MegalodonShark()):
                print("")
                input(self.player,"Ok that was scary, I'm not crying it's from the ocean!")
                print("")
                self.adventure.mark_visited()

        else:
            print("Oh my jesus its the shark! The waters just warm here, don't look at me!")
            print("maybe we should just go!")

    def petrifyingPiranha_fight(self):
        if self.adventure.already_visited() is False:
            print("Ok its a huge piranha, I'm not saying we're screwed, but we're screwed!")
            time.sleep(2)
            print("")
            if Battle().start(self.player, PetrifyingPiranha()):
                print("")
                input(self.player, "I LIVED! YES!! i may or may not have lost a finger!")
                print("")
                self.adventure.mark_visited()

        else:
            print("Ok i think that's the piranha again! oh hey look it's a rainbow, lets go this way!")
            print("There's nothing here, I looked!")