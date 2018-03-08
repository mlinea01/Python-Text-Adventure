import csv
from Multiplayer import IO
from functools import partial


class Adventure:
    def __init__(self):
        self.adventure_data = [["a1", None, "a3"],
                               ["b1", None, "b3"],
                               ["c1", "c2", "c3", "c4"]]

        self.player_x = 0
        self.player_y = 0

        while True:
            IO.print_text(" ")
            self.print(self.player_x, self.player_y)
            IO.print_text("Choose direction to go in: ", 0)
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

            direction = int(IO.get_input(0, "Your choice: ", partial(IO.check_num_in_range, minimum=1,
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
            if x < 0 or x >= len(self.adventure_data[y]):
                return False
            if y < 0 or y >= len(self.adventure_data):
                return False
            if self.adventure_data[y][x] is None:
                return False

            return True

        except IndexError:
            return False

    def print(self, x, y):
        IO.print_text(self.adventure_data[y][x])
