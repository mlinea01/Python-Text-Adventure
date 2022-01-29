from Battle import *
from adventures.Clouds.Enemies import *
from adventures.Adventures import *
from adventures.Clouds.Traps import *
import threading
from time import sleep
from items.Potions import *
from adventures.Merchant import Merchant

class CloudAdventure:
    def __init__(self, players):
        self.players = players

        map_data = []
        self.adventure = Adventure(self.players, map_data, 0, 0)

        self.traps = [RainbowRope(), LightningDart(), MeteorBucket()]

    def get_primary_player(self, players):
        result = 0
        for player in players:
            if player.hp > 0:
                return result
            else:
                result += 1

    def Cloud_merchant(self):
        print("A merchant hovers in the sky on a nimbus cloud. You hover over...")
        merchant = Merchant(items_list=[HealthPotion(), ManaPotion()],
                            greeting="The sky is a peaceful meadow showing us what heaven will be like",
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
            trap = self.traps[traps-1]
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
        jump = IO.get_input(player.player_num, "Theres a " + trap.name + ", Type 'jump' to avoid the trap!!!!!!!!!", time_out=50)
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

    def unluckyLeprechaun_fight(self):
        if self.adventure.already_visited() is False:
            print("Hey look a leprechaun! You think he'll give us some gold?")
            time.sleep(2)
            print("")
            if Battle().start(self.players, UnluckyLeprechaun()):
                print("")
                IO.get_input(self.get_primary_player(self.players),
                             "Ok, he didn't give us gold!")
                print("")
                self.adventure.mark_visited()

        else:
            print("Oh look it's the leprechaun again!")
            print("I know we didn't find anything before)

    def hideousHippogryph_fight(self):
        if self.adventure.already_visited() is False:
            print("Holy crap what is that? I saw something on the discovery channel about a hippogryph,"
                          " I think that's what that is!!")
            time.sleep(2)
            print("")
            if Battle().start(self.players, HideousHippogryph()):
                print("")
                IO.get_input(self.get_primary_player(self.players), "Ok that was creep! I don't think we're in kansas anymore")
                print("")
                self.adventure.mark_visited()

        else:
            print("Hey look it's that hippogryph)
            print("Well since i'm clearly dreaming)

    def crazyCockatrice_fight(self):
        if self.adventure.already_visited() is False:
            print("Look a Cockatrice! It almost looks like the beast from never ending story)
            time.sleep(2)
            print("")
            if Battle().start(self.players, CrazyCockatrice()):
                print("")
                IO.get_input(self.get_primary_player(self.players), "Welp, it was definitely meaner than the beast from never ending story!")
                print("")
                self.adventure.mark_visited()

        else:
            print("Hey look its the never ending story monster)
            print("I'm pretty sure we cleared this camp out!")