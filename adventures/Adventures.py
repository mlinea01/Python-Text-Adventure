import csv
from Multiplayer import IO
from functools import partial
from Battle import Battle
from characters.Enemies import *
import time


class Adventure:
    def __init__(self, players):
        self.players = players
        self.adventure_data = [[self.normal_room,     None,   self.normal_room],
                               [self.normal_room,     None,   self.normal_room],
                               [self.enemy_room ,  self.trap, self.normal_room , self.dead_end]]

        self.player_x = 0
        self.player_y = 0

        while True:
            IO.print_text(" ")
            self.run_room(self.player_x, self.player_y)
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

    def normal_room(self):
        IO.print_text("This is just a normal room.")

    def dead_end(self):
        IO.print_text("This is a dead end...")

    def trap(self):
        IO.print_text("Careful, there is  trap in this room!")

    def enemy_room(self):
        IO.print_text("Enemy attacking!")
        time.sleep(2)
        Battle(self.players, TerrifyingTurantula())

    def run_room(self, x, y):
        self.adventure_data[y][x]()
