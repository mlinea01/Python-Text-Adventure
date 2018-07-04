import threading
from Multiplayer import IO
from time import sleep
from copy import copy
from attacks.AttacksInfo import Attack
from attacks.AttacksInfo import AttackTypes
import enum


class StringUtils:
    @classmethod
    def string_contains(cls, input_str, str_list):
        for s in str_list:
            if s in input_str:
                return True
        return False


# This class keeps track of attack types - useful for things like determining resistances to certain moves
class BridgeResults(enum.Enum):
    BridgeBroke = enum.auto()
    MadeItAcross = enum.auto()
    RanAway = enum.auto()


class BridgeEvent:

    def __init__(self, players):
        IO.print_text("The party comes upon a clearing in the forest in which you can see a giant gorge extending down "
                      "for miles with a stream running at the bottom. Stretching the length of the gorge is a rope "
                      "bridge that looks like it's been there for ages. Nonetheless, it is the only way across.")
        self.players = players
        self.players_on_bridge = []
        self.players_falling = []
        self.players_injured = []
        self.players_across = []
        self.player_go_back = []
        self.result = ""
        self.fall = Attack("Bridge Fall", "You slam into the side of the gorge while clinging onto the broken bridge "
                           "as it swings down!", damage=5, atkType=AttackTypes.Normal, manaCost=0,
                           statusEffects=[])
        self.bridge_status = "normal"
        self.bridge_words = ["bridge", "across", "forward", "continue"]
        self.move_words_neutral = ["go", "walk"]
        self.move_words_fast = ["run", "sprint", "jog"]
        self.investigate_words = ["investigate", "look", "test", "check", "examine"]
        self.retreat_words = ["back", "leave", "away", "turn around", "flee", "retreat"]
        self.num_players_on_bridge = 0

    def get_event_result(self):
        return self.result

    def start_event(self):
        for player in self.players:
            threading.Thread(target=self.player_action, args=[player]).start()

        while True:
            sleep(0.5)
            if self.bridge_status == "broken" and len(self.players_falling) == 0 and len(self.players_injured) > 0:
                injured_names = ""
                injured_player_index = 0
                while injured_player_index < len(self.players_injured):
                    injured_player = self.players_injured[injured_player_index]
                    injured_names += injured_player.name
                    if injured_player_index < len(self.players_injured)-1:
                        injured_names += " and "
                    injured_player.hit_by(copy(self.fall))
                    injured_player_index += 1
                if len(self.players_injured) > 1:
                    injured_names += " climb"
                else:
                    injured_names += " climbs"
                IO.print_text(injured_names + " back up after clinging on to part of the bridge as it swung down "
                                              "hard into the side of the gorge, with some bruises to show for it.")
                self.result = BridgeResults.BridgeBroke
                return self

            elif len(self.players_across) == len(self.players):
                sleep(0.5)
                IO.print_text("Everyone has made it across safely! Now you may continue onwards...")
                self.result = BridgeResults.MadeItAcross
                sleep(1)
                return self

            elif len(self.player_go_back) > 0:
                IO.print_text(self.player_go_back[0].name + " looks very flustered and just runs away!")
                if len(self.players) > 1:
                    IO.print_text("Everyone else quickly runs after them.")
                if self.bridge_status == "normal":
                   self.result = BridgeResults.RanAway
                else:
                    self.result = BridgeResults.BridgeBroke
                sleep(1)
                return self

    def player_action(self, player):
        while True:
            input_text = IO.get_input(player.player_num, "What would you like to do? ")
            moving_neutral = StringUtils.string_contains(input_text, self.move_words_neutral)
            moving_fast = StringUtils.string_contains(input_text, self.move_words_fast)

            if StringUtils.string_contains(input_text, self.retreat_words):
                self.player_go_back.append(player)
                break

            elif moving_neutral or moving_fast:
                # moving across bridge
                if StringUtils.string_contains(input_text, self.bridge_words):
                    self.players_on_bridge.append(player)
                    IO.print_text(player.name + " steps onto the bridge and begins moving across...")
                    if len(self.players_on_bridge) >= 2:
                        self.bridge_status = "broken"
                        sleep(0.5)
                        IO.print_text("The bridge ropes snap! The bridge begins to fall into the gorge below!")
                        self.players_falling = copy(self.players_on_bridge)
                        for player_falling in self.players_falling:
                            threading.Thread(target=self.player_falls, args=[player_falling]).start()
                        self.players_on_bridge = []
                        break

                    else:

                        if moving_fast:
                            sleep(2)
                        else:
                            sleep(4)

                        if self.bridge_status == "normal":
                            self.players_on_bridge.remove(player)
                            self.players_across.append(player)
                            IO.print_text(player.name + " made it across the bridge!")

                        break

            elif StringUtils.string_contains(input_text, self.investigate_words):
                IO.print_text("The bridge sways and creaks in the breeze...", player.player_num)

            else:
                IO.print_text("You cannot do that.", player.player_num)

    def player_falls(self, player):
        reaction = IO.get_input(player.player_num,
                                "Type 'run back' to get back quick!",
                                time_out=50)
        IO.print_text(" ")
        if reaction != "run back":
            IO.print_text("You start falling! But you grab onto a piece of the bridge as it swings down and you "
                          "hit the side of the gorge!")
            self.players_injured.append(player)
        else:
            IO.print_text(player.name + " made it back safely!")

        self.players_falling.remove(player)