import random


NUM_SIDES = 6

def roll_dice():
    dice1 = random.randint(1 ,NUM_SIDES)
    dice2 = random.randint(1, NUM_SIDES)
    total = dice1 + dice2
    print("Total of 2 dice:", total)

def main ():
    dice1 = 10
    print("dice in main start as:", dice1)
    roll_dice()
    roll_dice()
    roll_dice()

    print("die1 in main() is:", dice1)

if __name__ == '__main__':
    main()
