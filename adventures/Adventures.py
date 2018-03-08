import csv
from Multiplayer import IO
from functools import partial


class Adventure:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.adventure_data = []
        file_data = csv.reader(open("adventure_data/adventure1.csv", "rt", encoding='utf-8-sig'))
        for row in file_data:
            for item in row:
                self.adventure_data.append(item)
                self.x += 1
            if self.width == 0:
                self.width = self.x
            self.x = 0
            self.y += 1

        self.player_x = 1
        self.player_y = 1

        while True:
            self.print(self.player_x, self.player_y)
            directions = []
            dir_num = 1
            if self.player_y > 1:
                directions.append("North")
            if self.player_y < 3:
                directions.append("South")
            if self.player_x < 3:
                directions.append("East")
            if self.player_x > 1:
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


    def print(self, x, y):
        x -= 1
        y -= 1
        print(self.adventure_data[x + y*self.width])
