"""Henry B & Fox W"""
import random
import sys


def roll_dice():
    # simulates a pair of dice being rolled
    return random.randint(1, 6) + random.randint(1, 6)


def play_round_one():
    # plays first round of craps
    dice_total = roll_dice()
    if dice_total == 2 or dice_total == 3 or dice_total == 12:
        # if 2, 3, or 12 is rolled, its craps
        print(f"You rolled a {dice_total} ", end="")
        return "craps"
    elif dice_total == 7 or dice_total == 11:
        # if 7 or 11 is rolled, its a natural
        print(f"You rolled a {dice_total} ", end="")
        return "natural"
    else:
        # otherwise it is a value
        point = dice_total
        print(f"The point is set to {point}.")
        return point


def play_craps():
    # plays craps
    played = play_round_one()
    if played == "craps":
        # rolls 2, 3, 12
        return "you lose"
    if played == "natural":
        # rolls 7, 11
        return "you win!"
    else:
        # rolls 4 - 6, 8 - 10
        reroll = roll_dice()
        while played != reroll and reroll != 7:
            # rolls again if you didn't lose (roll a 7) or didn't roll number from first round
            print(f"Your rerolled value = {reroll}! Roll again!")
            reroll = roll_dice()
        if reroll == 7:
            # lose if you roll a 7
            print("You rerolled a 7 ", end="")
            return "you lose"
        if reroll == played:
            # win if you roll round one number
            print(f"You rerolled {played} ", end="")
            return "you win!"


def craps_main():
    play = str(input("Would you like the play craps? ")).lower()
    wins = 0
    lose = 0
    while play == "yes" or "y" == play:
        played = play_craps()
        # determines how many wins and losses
        if played == "you win!":
            print("you win!")
            wins += 1
        if played == "you lose":
            print("you lose!")
            lose += 1

        # displays wins and losses
        print(f"Wins:{wins} Losses:{lose}")

        # does the user want to play again?
        play = str(input("Would you like the play craps? ")).lower()

    # exits program is user is done playing
    if play == "no":
        sys.exit(1)
    return wins, lose


if __name__ == "__craps_main__":
    craps_main()
