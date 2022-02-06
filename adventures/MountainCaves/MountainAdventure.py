from Battle import *
from adventures.MountainCaves.Enemies import *
from adventures.Adventures import Adventure
from adventures.MountainCaves.Traps import *
from items.Potions import *
import threading
from time import sleep
from threading import Timer
from adventures.Merchant import Merchant


class MountainAdventure:
    def __init__(self, player):
        self.player = player

        map_data = []
        self.adventure = Adventure(self.player, map_data, 0, 0)

        self.traps = [StoneStakes(), BoulderMace(), PillarLaunch()]


    def Mountain_merchant(self):
        print("A merchant sits in a dark cave on the edge of the mountain. You go inside...")
        merchant = Merchant(items_list=[HealthPotion(), ManaPotion()],
                            greeting="This mountain speaks to our souls, showing us what life is about!",
                            sales_pitch="Perhaps these will give you sustenance. What would you like?",
                            goodbye="Farewell, and beware.")
        merchant.greet(self.player)

    def empty(self):
        print(
            "This area is empty. Fred wasn't sure what to put here, but wanted to put something as a proof of concept.")

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

        while len(self.activePlayers) > 0:
            sleep(0.5)

    def player_hit_by_trap(self, player, trap):
        time_out=50
        timer = Timer(time_out, print, ['Times up!!!'])
        jump = input(player.name + "Theres a " + trap.name + ", Type 'jump' to avoid the trap!!!!!!!!!")
        timer.start()
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

    def dragon_fight(self):
        if self.adventure.already_visited() is False:
            print("There is a Mountain Dragon in the camp, Hurry, take that dragon down!")
            time.sleep(2)
            print("")
            if Battle().start(self.player, MountainDragon()):
                print("")
                input(self.player.name, "Woah that dragon was tough! Now that that's over lets take a look around this camp.")
                print("")
                self.adventure.mark_visited()

        else:
            print("The slain Mountain Dragon lies in the middle of the camp.")
            print("The wind blows steadily from the mountains to the East, but there is nothing else here.")

    def golem_fight(self):
        if self.adventure.already_visited() is False:
            print("Have you ever seen a golem? No? There's one right there!")
            time.sleep(2)
            print("")
            if Battle().start(self.player, Golem()):
                print("")
                input(self.player.name, "I mean this is getting ridiculous! A golem? really?")
                print("")
                self.adventure.mark_visited()

        else:
            print("Oh hey look it's that golem again! I really hope it's dead, i mean how do you know? hes all rock!")
            print("I think we got everything, so to be safe, let's just leave!")

    def maliciousMountainLion_fight(self):
        if self.adventure.already_visited() is False:
            print("Is that a mountain lion? I knew i shouldn't have come this way!")
            time.sleep(2)
            print("")
            if Battle().start(self.player, MaliciousMountainLion()):
                print("")
                input(self.player.name, "Ok, could have been worse. I may have rabies but i'll be fine!")
                print("")
                self.adventure.mark_visited()

        else:
            print("Look, it's that mountain lion that bit me! I think we should leave, his friends are probably close!")
            print("This place is clean, let's move fast!")