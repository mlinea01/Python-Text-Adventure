from Multiplayer import IO
from functools import partial


class Adventure:
    def __init__(self, players, map_data, start_x=0, start_y=0):
        self.players = players
        self.map_data = map_data

        self.player_x = start_x
        self.player_y = start_y
        self.visited = set()

    def get_primary_player(self, players):
        result = 0
        for player in players:
            if player.hp > 0:
                return result
            else:
                result += 1

    def start(self):
        while True:
            IO.print_text(" ")
            self.run_room(self.player_x, self.player_y)
            sumHp = 0
            for player in self.players:
                sumHp += player.hp
            if sumHp == 0:
                return
            IO.print_text("Choose direction to go in: ", self.get_primary_player(self.players))
            directions = []
            dir_num = 1
            if self.can_move_to(self.player_x, self.player_y-1):
                directions.append("North")
            if self.can_move_to(self.player_x, self.player_y+1):
                directions.append("South")
            if self.can_move_to(self.player_x+1, self.player_y):
                directions.append("East")
            if self.can_move_to(self.player_x-1, self.player_y):
                directions.append("West")

            for direction in directions:
                IO.print_text(str(dir_num) + ". " + direction)
                dir_num += 1

            direction = int(IO.get_input(self.get_primary_player(self.players), "Your choice: ", partial(IO.check_num_in_range, minimum=1,
                                                                     maximum=len(directions))))-1

            if directions[direction] == "North":
                self.player_y -= 1
            elif directions[direction] == "South":
                self.player_y += 1
            elif directions[direction] == "East":
                self.player_x += 1
            else:
                self.player_x -= 1

    def can_move_to(self, x, y):
        try:
            if x < 0 or x >= len(self.map_data[y]):
                return False
            if y < 0 or y >= len(self.map_data):
                return False
            if self.map_data[y][x] is None:
                return False

            return True

        except IndexError:
            return False

    def run_room(self, x, y):
        self.map_data[y][x]()

    def already_visited(self):
        try:
            if (self.player_x, self.player_y) in self.visited:
                return True
            else:
                return False
        except IndexError:
            return False

    def mark_visited(self):
        self.visited.add((self.player_x, self.player_y))
