#Roberto J. Perez
#12/2/2022
#CSS 225
#Milestone 3
import main_character
import section_2
def start(player):
    print("Jeff: ok guys we will split Eddie and I, and Matt and Sam remember we got to collect 5 fingers")
    input()
    print("Jeff: OMG!! the note turned into a finger so we got 1/5")
    input()
    print("Eddie: lets explore around")
    input()
    print("Jeff: Ok hopefully we can get out of here")
    input()
    print("*screaming from the other side of the cemetery*")
    input()
    print("Eddie: What was that!!")
    input()
    print("Jeff: Let's go check it out, it could be Matt and Sam")
    input()
    print("Eddie: OMG Sam!!! Jeff he's been cut in half. Where's Matt ")
    input()
    print("*growl*")
    input()
    print("Jeff: Eddie run!!")
    input()
    print("Eddie: What the HELL!! IS THAT!!!")
    input()
    print("Jeff: just keep on running")
    input()
    #A running scene where you turn left or right 5 times
    count = 0
    user_jeff = input("Let's turn left now or let's turn right now\n")
    while count < 5:
        count += 1
        print("You went",user_jeff)
        user_jeff = input("Let's turn left now or let's turn right now\n")
        break
    input()
    print("Jeff: I think we escaped from the monster")
    input()
    print("Eddie: Jeff it got me pretty bad *scrached on his stomach* ")
    input()
    print("Jeff: try my best to help you here is mt t-shirt, place it over the wound and press hard")
    input()
    print("Eddie: Thank you Jeff for everything! it's my time to see Sam I'll tell him he was right "
          "should've just watched The Thing. ")
    input()
    print("Eddie has died")
    input()
    print("Jeff: NO WHYYYYYYY!!!")
    input()
    print("*Growl*")
    input()
    print("Jeff: You killed my friends...Whyy!")
    input()
    print("*slash* the monster has killed Jeff")
    input()
    #Losing condition gives option to restart from section 2 or just end the game
    game = input("Game over! Would you like to restart from the last checkpoint? Y/N\n")
    if game == "Y" or game =="Yes":
        section_2.start(player)
    elif game == "N" or game == "No":
        exit()

