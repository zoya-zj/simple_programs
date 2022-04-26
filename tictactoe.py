# A simple program that allows you to play tictactoe with another player or the computer.
# The computer uses a simple algorithm to determine placement of its symbol.
# It prioritizes blocking the player.

import random

class Board:
    # A class to represent the tictactoe board.

    def __init__(self):
        # the board is initialized like
        # 0 | 1 | 2
        # 3 | 4 | 5
        # 6 | 7 | 8
        self.board = ["-", "-", "-",
                    "-", "-", "-",
                    "-", "-", "-"]
    
    def add_X(self, pos):
        # Adds X at pos

        self.board[pos] = "X"
    
    def add_O(self, pos):
        # Adds O at pos

        self.board[pos] = "O"
    
    def check_tictactoe(self):
        # Checking to see if a tictactoe is gotten.
        # Return[0] is True if a tictactoe is found, Return[1] is the symbol that won.

        # Top row
        if self.board[0] == self.board[1] and self.board[1] == self.board[2] and self.board[0] != "-":
            return [True, self.board[0]]
        # Middle Row
        if self.board[3] == self.board[4] and self.board[4] == self.board[5] and self.board[3] != "-":
            return [True, self.board[3]]

        # Bottom Row
        if self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[6] != "-":
            return [True, self.board[6]]

        # Left Column
        if self.board[0] == self.board[3] and self.board[3] == self.board[6] and self.board[0] != "-":
            return [True, self.board[0]]

        # Middle Column
        if self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[1] != "-":
            return [True, self.board[1]]

        # Right Column
        if self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[2] != "-":
            return [True, self.board[2]]

        # Diagonal Left-Right
        if self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[0] != "-":
            return [True, self.board[0]]

        # Diagonal Right-Left
        if self.board[2] == self.board[4] and self.board[4] == self.board[6] and self.board[2] != "-":
            return [True, self.board[2]]
        
        return [False, None]
    
    def sq_is_empty(self, pos):
        # Checking to see if square is empty.

        try:
            pos = int(pos)
        except:
            return False

        if pos > 8:
            return False

        if self.board[pos] == "-":
            return True

        return False

    def is_full(self):
        # Checking for a tie.

        for i in self.board:
            if i == '-':
                return False
        return True

    def clear_board(self):
        # Resets the board.

        self.board = ["-", "-", "-",
                    "-", "-", "-",
                    "-", "-", "-"]
        return "Cleared"
    
    def tictactoe_posssible(self):
        # For the computer to see if it can get a tictactoe or block the player.

        # Top row
        if self.board[0] == self.board[1] and self.board[2] == "-" and self.board[0] != "-":
            return 2

        if self.board[0] == self.board[2] and self.board[1] == "-" and self.board[0] != "-":
            return 1

        if self.board[2] == self.board[1] and self.board[0] == "-" and self.board[2] != "-":
            return 0

        # Middle Row
        if self.board[3] == self.board[4] and self.board[5] == "-" and self.board[3] != "-":
            return 5
        if self.board[5] == self.board[4] and self.board[3] == "-" and self.board[5] != "-":
            return 3
        if self.board[3] == self.board[5] and self.board[4] == "-" and self.board[5] != "-":
            return 4

        # Bottom Row
        if self.board[6] == self.board[7] and self.board[8] == "-" and self.board[6] != "-":
            return 8

        if self.board[6] == self.board[8] and self.board[7] == "-" and self.board[6] != "-":
            return 7

        if self.board[8] == self.board[7] and self.board[6] == "-" and self.board[7] != "-":
            return 6

        # Left Column
        if self.board[0] == self.board[3] and self.board[6] == "-" and self.board[0] != "-":
            return 6

        if self.board[0] == self.board[6] and self.board[3] == "-" and self.board[0] != "-":
            return 3

        if self.board[3] == self.board[6] and self.board[0] == "-" and self.board[3] != "-":
            return 0

        # Middle Column
        if self.board[1] == self.board[4] and self.board[7] == "-" and self.board[1] != '-':
            return 7

        if self.board[1] == self.board[7] and self.board[4] == "-" and self.board[1] != '-':
            return 4

        if self.board[7] == self.board[4] and self.board[1] == "-" and self.board[7] != '-':
            return 1

        # Right Column
        if self.board[2] == self.board[5] and self.board[8] == "-" and self.board[2] != '-':
            return 8

        if self.board[2] == self.board[8] and self.board[5] == "-" and self.board[2] != '-':
            return 5

        if self.board[8] == self.board[5] and self.board[8] == "-" and self.board[8] != '-':
            return 2

        # Diagonal Left-Right
        if self.board[0] == self.board[4] and self.board[8] == "-" and self.board[0] != '-':
            return 8
        
        if self.board[0] == self.board[8] and self.board[4] == "-" and self.board[0] != '-':
            return 4
        
        if self.board[8] == self.board[4] and self.board[0] == "-" and self.board[8] != '-':
            return 0

        # Diagonal Right-Left
        if self.board[2] == self.board[4] and self.board[6] == "-" and self.board[2] != '-':
            return 6

        if self.board[2] == self.board[6] and self.board[4] == "-" and self.board[2] != '-':
            return 4

        if self.board[6] == self.board[4] and self.board[2] == "-" and self.board[6] != '-':
            return 2
        
        return 9
    
    def __str__(self):
        # Prints the board.

        s = str(self.board[0]) + " | " + str(self.board[1]) +  " | " + str(self.board[2]) + "\n"
        s += str(self.board[3]) +  " | " + str(self.board[4]) +  " | " + str(self.board[5]) + "\n"
        s += str(self.board[6]) +  " | " + str(self.board[7]) +  " | " + str(self.board[8]) + "\n"
        return s
        
    
if __name__ == "__main__":
    pvp = False
    ans = ''

    while ans != "1" and ans != '2':
        ans = input("PVP (1) or PVC (2): ")
    
    if ans == '1':
        pvp = True
    tictactoe = Board()
    end = "Y"
    # PVP enabled.
    if pvp:
        while end == "Y":
            ans = "10"
            is_empty = False
            end = ""
            check = tictactoe.check_tictactoe()
            full = tictactoe.is_full()
            print(tictactoe)
            while not check[0] and not full:
                # Runs the game.

                # Player 1 Turn
                while not tictactoe.sq_is_empty(ans):
                    # Invalid answer loop.
                    ans = input("Player 1 choose a position (0-8): ")
                tictactoe.add_X(int(ans))
                print(tictactoe)
                check = tictactoe.check_tictactoe()
                full = tictactoe.is_full()
                if full or check[0]:
                    break

                # Player 2 Turn
                tictactoe.add_X(int(ans))
                while not tictactoe.sq_is_empty(ans):
                    # Invalid answer loop.
                    ans = input("Player 2 choose a position (0-8): ")
                tictactoe.add_O(int(ans))

                # Checking for tictactoe.
                check = tictactoe.check_tictactoe()
                full = tictactoe.is_full()
                print(tictactoe)

            if check[0]:
                print(check[1], "'s WINS")
            else:
                print("ITS A TIE!")

            tictactoe.clear_board()

            while end != 'Y' and end != 'N':
                end = input("Continue playing (Y/N): ")
    else:
        # Vs Compyter
        play = ''
        while play != "X" and play != 'O':
            play = input("Do you want you want to play as X or O: ")
        
        # Player is X
        if play == 'X':
            while end == "Y":
                ans = "10"
                is_empty = False
                end = ""
                check = tictactoe.check_tictactoe()
                full = tictactoe.is_full()
                print(tictactoe)
                while not check[0] and not full:
                    # Runs the game.

                    # Player 1 Turn
                    while not tictactoe.sq_is_empty(ans):
                        # Invalid answer loop.
                        ans = input("Player 1 choose a position (0-8): ")
                    tictactoe.add_X(int(ans))
                    print(tictactoe)
                    check = tictactoe.check_tictactoe()
                    full = tictactoe.is_full()
                    if full or check[0]:
                        break

                    # Computer Turn
                    p = tictactoe.tictactoe_posssible()
                    if p <= 8:
                        tictactoe.add_O(p)
                    else:
                        while not tictactoe.sq_is_empty(p):
                            # Invalid answer loop.
                            p = random.randint(0,8)
                        tictactoe.add_O(p)
            
                    # Checking for tictactoe.
                    check = tictactoe.check_tictactoe()
                    print("Computer's Turn:")
                    print(tictactoe)

                if check[0]:
                    print(check[1], "'s WINS")
                else:
                    print("ITS A TIE!")

                tictactoe.clear_board()

                while end != 'Y' and end != 'N':
                    end = input("Continue playing (Y/N): ")
        
        # Player is O
        else:
            while end == "Y":
                ans = "10"
                is_empty = False
                end = ""
                check = tictactoe.check_tictactoe()
                full = tictactoe.is_full()
                print(tictactoe)
                while not check[0] and not full:
                    # Runs the game.

                    # Computer Turn
                    p = tictactoe.tictactoe_posssible()
                    if p <= 8:
                        tictactoe.add_X(p)
                    else:
                        while not tictactoe.sq_is_empty(p):
                            # Invalid answer loop.
                            p = random.randint(0,8)
                        tictactoe.add_X(p)
                    print("Computer's Turn:")
                    print(tictactoe)
                    check = tictactoe.check_tictactoe()
                    full = tictactoe.is_full()
                    if full or check[0]:
                        break

                    # Player 1 Turn
                    while not tictactoe.sq_is_empty(ans):
                        # Invalid answer loop.
                        ans = input("Player 1 choose a position (0-8): ")
                    tictactoe.add_O(int(ans))

                    # Checking for tictactoe.
                    check = tictactoe.check_tictactoe()
                    print(tictactoe)

                if check[0]:
                    print(check[1], "'s WINS")
                else:
                    print("ITS A TIE!")

                tictactoe.clear_board()

                while end != 'Y' and end != 'N':
                    end = input("Continue playing (Y/N): ")