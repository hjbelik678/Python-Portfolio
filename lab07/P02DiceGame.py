"""For this project your will be extending either P04Craps from Lab06 or P03EvenOrOdd from Lab04.
Your program should now start by asking the user for their name. If the user is baned then your program should print a
message to that effect and exit. If the user is not banned then your program should play the game as normal. A user is
 baned if their total number of losses is greater than 3 and the number of losses is greater than 2 times the number of
 wins. Your program should store the total number of wins and losses in a file named dice_game.txt in the same directory
  as your program. """
# add file to this project
from ReferenceCraps import craps_main
# global
# banned = open("banned_names", "r")
import sys


def main():
    name = input("What is your name? ")
    # check if name is banned
    if name == name:
        print("You are banned")
        sys.exit
    win , lose = craps_main()
    print(win , lose)
    file2write = open("dice_game.txt", 'w')
    file2write.write(name)
    file2write.writelines(win)
    file2write.writelines(lose)
    file2write.close()
    #store wins and losses
    #then at the end update


    #if lose > 3 and lose > 2 * win:




if __name__ == "__main__":
    main()
