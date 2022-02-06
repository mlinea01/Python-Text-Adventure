from Battle import *
from adventures.Clouds.Enemies import *
from adventures.Adventures import *
from adventures.Clouds.Traps import *
import threading
from items.Potions import *
from adventures.Merchant import Merchant
from threading import Timer

class CloudAdventure:
    def __init__(self, player):
        self.player = player

        map_data = []
        self.adventure = Adventure(self.player, map_data, 0, 0)

        self.traps = [RainbowRope(), LightningDart(), MeteorBucket()]

    def Cloud_merchant(self):
        print("A merchant hovers in the sky on a nimbus cloud. You hover over...")
        merchant = Merchant(items_list=[HealthPotion(), ManaPotion()],
                            greeting="The sky is a peaceful meadow showing us what heaven will be like",
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


    def player_hit_by_trap(self, player, trap):
        time_out=50
        timer = Timer(time_out, print, ['Times up!!!'])
        jump = input("Theres a " + trap.name + ", Type 'jump' to avoid the trap!!!!!!!!!", time_out=50)
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

    def unluckyLeprechaun_fight(self):
        if self.adventure.already_visited() is False:
            print("Hey look a leprechaun! You think he'll give us some gold?")
            time.sleep(2)
            print("")
            if Battle().start(self.player, UnluckyLeprechaun()):
                print("")
                input(self.player, "Ok, he didn't give us gold!")
                print("")
                self.adventure.mark_visited()

        else:
            print("Oh look it's the leprechaun again!")
            print("I know we didn't find anything before, but there may be gold here")

    def hideousHippogryph_fight(self):
        if self.adventure.already_visited() is False:
            print("Holy crap what is that? I saw something on the discovery channel about a hippogryph,"
                          " I think that's what that is!!")
            time.sleep(2)
            print("")
            if Battle().start(self.player, HideousHippogryph()):
                print("")
                input(self.player, "Ok that was creep! I don't think we're in kansas anymore")
                print("")
                self.adventure.mark_visited()

        else:
            print("Hey look it's that hippogryph, i guess i still didn't wake up from this dream!")
            print("Well since i'm clearly dreaming, lets look for a million dollars")

    def crazyCockatrice_fight(self):
        if self.adventure.already_visited() is False:
            print("Look a Cockatrice! It almost looks like the beast from never ending story, but not!")
            time.sleep(2)
            print("")
            if Battle().start(self.player, CrazyCockatrice()):
                print("")
                input(self.player, "Welp, it was definitely meaner than the beast from never ending story!")
                print("")
                self.adventure.mark_visited()

        else:
            print("Hey look its the never ending story monster, the umm...Cockatrice!")
            print("I'm pretty sure we cleared this camp out!")