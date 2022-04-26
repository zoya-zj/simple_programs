# A simple game were the user guesses a number between 1 and 1000

import random

num = random.randint(1, 1000)
guess = 0

while guess != str(num):
    guess = input("Guess a number between 1 and 1000: ")
    try:
        if(int(guess) < num):
            print("Higher")
        elif(int(guess) > num):
            print("Lower")
    except:
        print("That is not a number")

print("Correct the number is ", num)
    