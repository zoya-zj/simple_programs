# Simple game of Rock Paper Scissors.
# Where 1 represents Rock, 2 represents paper, and 3 represents scissors.

import random

stop = False
while not stop:
    ans = input("Rock (1), Paper (2), Scissors (3):")
    comp_ans = random.randint(1,3)
    if ans == str(comp_ans):
        print("Its a tie!")
    elif ans == '1' and comp_ans == 2:
        print("Player: Rock \nComputer: Paper \nComputer Wins!!")
    elif ans == '1' and comp_ans == 3:
        print("Player: Rock \nComputer: Scissors \nPlayer Wins!!")
    elif ans == '2' and comp_ans == 1:
        print("Player 1: Paper \nComputer: Rock \nPlayer Wins!!")
    elif ans == '2' and comp_ans == 3:
        print("Player 1: Paper \nComputer: Scissors \nComputer Wins!!")
    elif ans == '3' and comp_ans == 1:
        print("Player 1: Scissors \nComputer: Rock \nComputer Wins!!")
    elif ans == '3' and comp_ans == 2:
        print("Player 1: Scissors \nComputer: Paper \nPlayer Wins!!")
    else:
        print("INVALID")
        
    
    play = input("Stop playing? Y/N?:")
    while play != 'Y' and play != 'N':
        print("Invalid Answer")
        play = input("Stop playing? Y/N?:")
    if play == 'Y':
        stop = True
        print("Exiting game...")
    
    