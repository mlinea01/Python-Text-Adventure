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
        if cls.get_index_string_in_list(input_str, str_list) is not None:
            return True
        else:
            return False

    @classmethod
    def get_index_string_in_list(cls, input_str, str_list):
        str_index = 0
        while str_index < len(str_list):
            s = str_list[str_index]
            if s in input_str:
                return str_index
            str_index += 1
        return None

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
        self.player_attacks = []
        self.build_attacks_list(players)
        self.player_items = []
        self.build_items_list(players)
        self.targets_list = []
        self.build_targets_list(players)
        self.fall = Attack("Bridge Fall", "You slam into the side of the gorge while clinging onto the broken bridge "
                           "as it swings down!", damage=5, atkType=AttackTypes.Normal, manaCost=0,
                           statusEffects=[])
        self.bridge_status = "normal"
        self.move_words_bridge = ["bridge", "across", "forward", "continue", "cross"]
        self.move_words_neutral = ["go", "walk"]
        self.move_words_fast = ["run", "sprint", "jog", "fast", "quick", "quickly", "swiftly", "speed"]
        self.investigate_words = ["investigate", "look", "test", "check", "examine", "touch"]
        self.retreat_words = ["back", "leave", "away", "turn around", "flee", "retreat"]
        self.player_use_attack_words = ["attack", "cast", "spellcast"]
        self.player_use_item_words = ["throw", "toss", "chuck", "item", "potion"]
        self.player_use_attack_or_items_words = ["use"]
        self.attack_words = ["throw", "use", "attack"]
        self.attack_confirm = ["throw", "use", "attack with"]
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
                    sleep(1)
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
            is_moving_neutral = StringUtils.string_contains(input_text, self.move_words_neutral)
            is_moving_fast = StringUtils.string_contains(input_text, self.move_words_fast)
            is_attack_word_used = StringUtils.string_contains(input_text, self.player_use_attack_words)
            is_item_word_used = StringUtils.string_contains(input_text, self.player_use_item_words)
            attack_index = StringUtils.get_index_string_in_list(input_text, self.player_attacks[player.player_num])
            item_index = StringUtils.get_index_string_in_list(input_text, self.player_items[player.player_num])

            if StringUtils.string_contains(input_text, self.retreat_words):
                self.player_go_back.append(player)
                break

            elif is_moving_neutral or is_moving_fast:
                if StringUtils.string_contains(input_text, self.move_words_bridge):
                    self.player_crosses(player, is_moving_fast)
                    break

            elif StringUtils.string_contains(input_text, self.investigate_words):
                IO.print_text("The bridge sways and creaks in the breeze...", player.player_num)

            elif is_attack_word_used:
                if attack_index is None:
                    attack_name = IO.get_input(player.player_num, "Which attack would you like to use?")
                else:
                    attack_name = self.player_attacks[player.player_num][attack_index]

                attack_exists = False
                for attack in self.player_attacks[player.player_num]:
                    if attack.name == attack_name:
                        attack_exists = True
                if attack_exists is False:
                    IO.print_text("You do not know that attack.", player.player_num)
                else:
                    IO.print_text(player.name + " uses " + self.player_attacks[player.player_num][attack_index] + "!")

            elif is_item_word_used:
                if item_index is None:
                    IO.get_input(player.player_num, "Which item would you like to use?")
                    item_name = IO.get_input(player.player_num, "Which item would you like to use?")
                else:
                    item_name = self.player_items[player.player_num][item_index]

                item_exists = False
                for item in self.player_items[player.player_num]:
                    if item.name == item_name:
                        item_exists = True
                if item_exists is False:
                    IO.print_text("", player.player_num)
                    continue
                else:
                    IO.print_text(player.name + " uses " + item_name)

            else:
                IO.print_text("You cannot do that.", player.player_num)

    def player_crosses(self, player, is_moving_fast):
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

        else:

            if is_moving_fast:
                sleep(3)
            else:
                sleep(5)

            if self.bridge_status == "normal":
                self.players_on_bridge.remove(player)
                self.players_across.append(player)
                IO.print_text(player.name + " made it across the bridge!")

    def player_falls(self, player):
        reaction = IO.get_input(player.player_num,
                                "Type 'run back' to get back quick!",
                                time_out=50)
        IO.print_text(" ")
        if reaction != "run back":
            IO.print_text("You start falling! But you grab onto a piece of the bridge as it swings down and you "
                          "hit the side of the gorge!", player.player_num)
            self.players_injured.append(player)
        else:
            IO.print_text(player.name + " made it back safely!")

        self.players_falling.remove(player)

    def build_attacks_list(self, players):
        for player in players:
            atk_list = []
            for atk in player.attacks:
                atk_list.append(atk.name)
            self.player_attacks.append(atk_list)

    def build_items_list(self, players):
        for player in players:
            item_list = []
            for item in player.items:
                item_list.append(item.name)
            self.player_items.append(item_list)

    def build_targets_list(self, players):
        for player in players:
            self.targets_list.append(player.name)
        self.targets_list.append("bridge")