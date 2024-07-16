import time
import os
import random
from itertools import product


class Games:
    def __init__(self):
        self.x_player = 0
        self.y_player = 0
        self.walk_player_move = True

        self.gold = [
            [0, 7], [4, 6], [8, 1], [11, 9]
        ]
        self.thorn = [
            [2, 1], [4, 4], [13, 3], [6, 7]
        ]
        self.wall = [
            [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [0, 8], [1, 8], [2, 8], [3, 0], [3, 1], [3, 2], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [4, 5], [5, 5],
            [6, 5], [7, 5], [8, 5], [9, 5], [12, 5], [13, 5], [8, 6], [8, 7], [6, 0], [6, 1], [6, 2], [7, 2], [8, 2], [9, 2], [12, 2], [13, 2]
        ]
        self.trail = []

    def get_map(self):
        map_list = [
            ['⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫'],
            ['⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫'],
            ['⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫'],
            ['⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫'],
            ['⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫'],
            ['⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫'],
            ['⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫'],
            ['⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫'],
            ['⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫'],
            ['⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫', '⚫'],
        ]  # ⚪⚫🔴🟡🟤 - карта

        for i_player in range(len(map_list)):
            for j_player in range(len(map_list[i_player])):
                is_gold = False
                is_thorn = False
                is_wall = False
                if i_player == self.y_player and j_player == self.x_player:
                    print('⚪', end='')
                else:
                    for i_gold in self.gold:
                        if i_gold[0] == j_player and i_gold[1] == i_player:
                            print('💰', end='')
                            is_gold = True
                            break
                    for i_thorn in self.thorn:
                        if i_thorn[0] == j_player and i_thorn[1] == i_player:
                            print('❌', end='')
                            is_thorn = True
                            break
                    for i_wall in self.wall:
                        if i_wall[0] == j_player and i_wall[1] == i_player:
                            print('🟫', end='')
                            is_wall = True
                            break

                    if not is_gold and not is_thorn and not is_wall:
                        print('⚫', end='')
            print()

        for i_thorn in self.thorn:
            if i_thorn[0] == self.x_player and i_thorn[1] == self.y_player:
                self.thorn.remove([i_thorn[0], i_thorn[1]])
                return 2
        for i_gold in self.gold:
            if i_gold[0] == self.x_player and i_gold[1] == self.y_player:
                self.gold.remove([i_gold[0], i_gold[1]])
                return 1
        return 0

    def walk_player(self):
        self.walk_player_move = True
        x = self.x_player
        y = self.y_player
        player = random.randint(1, 4)
        player_walk_rnd = random.randint(1, 1000) / 10
        if player == 0:
            self.walk_player_move = False
        elif (player == 1) and (x - 1 != -1) and ([x - 1, y] not in self.wall):  # влево
            if ([x - 1, y] in self.trail) and (player_walk_rnd <= 98):
                return
            self.x_player -= 1
            self.walk_player_move = False
        elif (player == 2) and (x + 1 != 14) and ([x + 1, y] not in self.wall):  # вправо
            if ([x + 1, y] in self.trail) and (player_walk_rnd <= 98):
                return
            self.x_player += 1
            self.walk_player_move = False
        elif (player == 3) and (y - 1 != -1) and ([x, y - 1] not in self.wall):  # вверх
            if ([x, y - 1] in self.trail) and (player_walk_rnd <= 98):
                return
            self.y_player -= 1
            self.walk_player_move = False
        elif (player == 4) and (y + 1 != 10) and ([x, y + 1] not in self.wall):  # вниз
            if ([x, y + 1] in self.trail) and (player_walk_rnd <= 98):
                return
            self.y_player += 1
            self.walk_player_move = False

        if [x, y] not in self.trail:
            self.trail.append([x, y])

    def main(self):
        gold = 0
        hp = 3
        self.get_map()
        print(f'\nPLAYER: {self.x_player, self.y_player}\nGOLD: {'💰' * gold}\nHP: {'❤' * hp}')
        while True:
            time.sleep(0.2)
            os.system("CLS")
            while self.walk_player_move:
                self.walk_player()
            result = self.get_map()
            if result == 0:
                pass
            elif result == 1:
                gold += 1
            elif result == 2:
                hp -= 1
            print(f'\nPLAYER: {self.x_player, self.y_player}\nGOLD: {'💰' * gold}\nHP: {'❤' * hp}')
            self.walk_player_move = True

            if hp == 0:
                os.system("CLS")
                print("FAIL")
                break
            if gold == 3:
                os.system("CLS")
                print("WIN")
                break


if __name__ == '__main__':
    a = Games()
    a.main()
