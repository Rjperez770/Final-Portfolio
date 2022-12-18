#Roberto J. Perez
#12/2/2022
#CSS 225
#Milestone 2
import main_character
import section_3
import church
import mausoleum
def start(player):
    print("The crew went into the Cemetery.")
    input()
    print("Mike: It's so foggy in here, I can barley see")
    input()
    print("Eddie and Sam: Lets stay close...Do you hear that")
    input()
    print("Jeff: Hey guys I found a note")
    input()
    print("All: what does it say?")
    input()
    print("Note:You have been trapped in the cemetery, you will need to find 5 fingers and the gate will reopen,"
          "but watch there's a monster in the mist")
    input()
    print("Mike: Guy the gate is gone and there's some type of barrier what do we do")
    input()
    print("Everybody: Did you guys hear that!")
    input()
    #If/elif statement to add more than just reading on the player and has consequences
    a = input("should we stay close or split? 1.Lets stay close, 2.lets split into pars\n")
    if a == "1":
        print("Everybody: Sounds like a good idea")
    else:
        print("Everybody: Doesn't sound but ok")
        section_3.start(player)
    input()
    print("The note turned into a finger you got 1/5")
    player.inventory = 1
    input()
    print("Mike: Which place should we search next?")
    input()
    #IF/elif statement that takes you to different parts of the cemetery
    sign = input("Sign: 1.right, to the church or 2.left, to the indoor mausoleum\n")
    if sign == "1":
        print("everybody: ok lets go!")
        church.start(player)
    elif sign == "2":
        print("everybody: ok lets go!")
        mausoleum.start(player)
    input()

