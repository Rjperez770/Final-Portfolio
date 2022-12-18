#Roberto J. Perez
#12/6/2022
#CSS 225
#Final project
import Ending
def start(player):
    print("The crew made it to the mausoleum ")
    input()
    print("Eddie: Let's get these fingers so we can leave this place")
    input()
    print("Matt: Let's explore and try to find them")
    input()
    print("Sam: I'm going to check downstairs and hopefully find something")
    input()
    print("Everybody: ok")
    input()
    print("Matt: look at this poster has a unique look and was made in 1928")
    input()
    print("Sam: Guys I found a vault and we need a code. Lets check it out")
    input()
    print("The went to the basement to unlock the vault")
    input()
    enter = int(input("Enter the 4 digit code to unlock the vault\n"))
    #Loop to enter a code and unlock the safe wont open until the exact code has been entered
    code = 1928
    while enter:
        if enter == 1928:
            print("The vault has been unlocked")
            print("Good Job!!")
            break
        while enter!= 1928:
            print("try again")
            enter = int(input("Enter the 4 digit code to unlock the vault\n"))
    print("Everybody: Good job you found 2 finger!!")
    player.inventory = 2
    input()
    print("Jeff: Lets go back to the gate where we started")
    input()
    Ending.start(player)

