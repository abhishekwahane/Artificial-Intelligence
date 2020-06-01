# PB1 ABHISHEK WAHANE
# Tic-Tac-Toe using Minimax Algorithm

import time

class Game:

    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

        self.player_turn = 'X'

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

# Check for game end
def is_end(self):
    # Vertical win
    for i in range(0, 3):
        if (self.current_state[0][i] != '.' and
            self.current_state[0][i] == self.current_state[1][i] and
            self.current_state[1][i] == self.current_state[2][i]):
            return self.current_state[0][i]

    # Horizontal win
    for i in range(0, 3):
        if (self.current_state[i] == ['X', 'X', 'X']):
            return 'X'
        elif (self.current_state[i] == ['O', 'O', 'O']):
            return 'O'

    # First diagonal win
    if (self.current_state[0][0] != '.' and
        self.current_state[0][0] == self.current_state[1][1] and
        self.current_state[0][0] == self.current_state[2][2]):
        return self.current_state[0][0]

    # Second diagonal win
    if (self.current_state[0][2] != '.' and
        self.current_state[0][2] == self.current_state[1][1] and
        self.current_state[0][2] == self.current_state[2][0]):
        return self.current_state[0][2]

    # Check board full
    for i in range(0, 3):
        for j in range(0, 3):
            if (self.current_state[i][j] == '.'):
                return None

    # Tie Game
    return '.'

def max(self):

    # -1 - loss
    # 0  - a tie
    # 1  - win

    # Initially set to -2 as worst case
    maxv = -2

    px = None
    py = None

    result = self.is_end()

    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)

    for i in range(0, 3):
        for j in range(0, 3):
            if self.current_state[i][j] == '.':
                self.current_state[i][j] = 'O'
                (m, min_i, min_j) = self.min()

                if m > maxv:
                    maxv = m
                    px = i
                    py = j

                self.current_state[i][j] = '.'
    return (maxv, px, py)

def min(self):

    # -1 - win
    # 0  - a tie
    # 1  - loss

    # Initially set to -2 as worst case
    minv = 2

    qx = None
    qy = None

    result = self.is_end()

    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)

    for i in range(0, 3):
        for j in range(0, 3):
            if self.current_state[i][j] == '.':
                self.current_state[i][j] = 'X'
                (m, max_i, max_j) = self.max()
                if m < minv:
                    minv = m
                    qx = i
                    qy = j
                self.current_state[i][j] = '.'

    return (minv, qx, qy)

def play(self):

    while True:
        self.draw_board()
        self.result = self.is_end()

        if self.result != None:
            if self.result == 'X':
                print('Winner: X')
            elif self.result == 'O':
                print('Winner: O')
            elif self.result == '.':
                print("Tie Game")

            self.initialize_game()
            return

        if self.player_turn == 'X':

            while True:

                start = time.time()
                (m, qx, qy) = self.min()
                end = time.time()
                print('Time: {}s'.format(round(end - start, 7)))
                print('Recommended move: X = {}, Y = {}'.format(qx, qy))

                px = int(input('Insert X: '))
                py = int(input('Insert Y: '))

                (qx, qy) = (px, py)

                if self.is_valid(px, py):
                    self.current_state[px][py] = 'X'
                    self.player_turn = 'O'
                    break
                else:
                    print('Invalid Move')

        else:
            (m, px, py) = self.max()
            self.current_state[px][py] = 'O'
            self.player_turn = 'X'

# Execution
def main():
        print("\nTic-Tac-Toe Game\n")
        Game.play()

if __name__ == "__main__":
    main()

"""

Tic-Tac-Toe Game

.| .| .|
.| .| .|
.| .| .|

Time: 5.0726919s
Recommended move: X = 0, Y = 0
Insert X coordinate: 0
Insert Y coordinate: 0
X| .| .|
.| .| .|
.| .| .|

X| .| .|
.| O| .|
.| .| .|

Time: 0.06496s
Recommended move: X = 0, Y = 1
Insert X coordinate: 0
Insert Y coordinate: 1
X| X| .|
.| O| .|
.| .| .|

X| X| O|
.| O| .|
.| .| .|

Time: 0.0020001s
Recommended move: X = 2, Y = 0
Insert X coordinate: 2
Insert Y coordinate: 0
X| X| O|
.| O| .|
X| .| .|

X| X| O|
O| O| .|
X| .| .|

Time: 0.0s
Recommended move: X = 1, Y = 2
Insert X coordinate: 1
Insert Y coordinate: 2
X| X| O|
O| O| X|
X| .| .|

X| X| O|
O| O| X|
X| O| .|

Time: 0.0s
Recommended move: X = 2, Y = 2
Insert X coordinate: 2
Insert Y coordinate: 2
X| X| O|
O| O| X|
X| O| X|

Tie Game

"""
