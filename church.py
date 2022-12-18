#Roberto J. Perez
#12/6/2022
#CSS 225
#Final project
import random as rand
import Ending
def start(player):
    print("*growl*")
    input()
    print("Everybody: Run towards the church")
    input()
    print("Matt: Keep going guys we are almost there!")
    input()
    print("The crew made it to the church with no harm done")
    input()
    print("Matt: Wow is huge in here!")
    input()
    print("Sam: and beautiful")
    input()
    print("Jeff: Look guys there's 2 fingers on the alter")
    input()
    print("You now have 3/5 fingers keep it up")
    player.inventory = 2
    input()
    print("Jeff: Let's go guys 3/5 almost there")
    input()
    print("Eddie: Guys there's a chest with some weapons")
    input()
    #Give Jeff the main charater a random weapon from the chest
    list1 = ["sword", "axe", "mace", "bow"]
    list2 = ["Jeff"]
    choice1 = rand.choice(list1)
    choice2 = rand.choice(list2)
    print(choice2, "and your weapon is a", choice1)
    input()
    print("Sam: Guys the monster is back")
    input()
    print("Matt: Look guys he's a bit slower can it be that we got 3/5 fingers??")
    input()
    print("Jeff: That makes sense. Let's make it back to the gate")
    input()
    print("everybody: Let's go!")
    input()
    Ending.start(player)





