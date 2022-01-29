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
        IO.print_text("A merchant hovers in the sky on a nimbus cloud. You hover over...")
        merchant = Merchant(items_list=[HealthPotion(), ManaPotion()],
                            greeting="The sky is a peaceful meadow showing us what heaven will be like",
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
            trap = self.traps[traps-1]
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
        jump = IO.get_input(player.player_num, "Theres a " + trap.name + ", Type 'jump' to avoid the trap!!!!!!!!!", time_out=50)
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

    def unluckyLeprechaun_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("Hey look a leprechaun! You think he'll give us some gold?")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, UnluckyLeprechaun()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players),
                             "Ok, he didn't give us gold!")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("Oh look it's the leprechaun again!")
            IO.print_text("I know we didn't find anything before, but there may be gold here")

    def hideousHippogryph_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("Holy crap what is that? I saw something on the discovery channel about a hippogryph,"
                          " I think that's what that is!!")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, HideousHippogryph()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players), "Ok that was creep! I don't think we're in kansas anymore")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("Hey look it's that hippogryph, i guess i still didn't wake up from this dream!")
            IO.print_text("Well since i'm clearly dreaming, lets look for a million dollars")

    def crazyCockatrice_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("Look a Cockatrice! It almost looks like the beast from never ending story, but not!")
            time.sleep(2)
            IO.print_text("")
            if Battle().start(self.players, CrazyCockatrice()):
                IO.print_text("")
                IO.get_input(self.get_primary_player(self.players), "Welp, it was definitely meaner than the beast from never ending story!")
                IO.print_text("")
                self.adventure.mark_visited()

        else:
            IO.print_text("Hey look its the never ending story monster, the umm...Cockatrice!")
            IO.print_text("I'm pretty sure we cleared this camp out!")