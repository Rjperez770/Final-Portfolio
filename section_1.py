#Roberto J. Perez
#11/3/2022
#Milestone 2
#CSS 225
#Header comments go here

#import main_character and section_2 here
import main_character
import section_2
#This start function is called by main_game.
#This will control the whole section.
#It'll need the player character as an input in order to interact with them.
def start(player):
    print("Mike: Hey Jeff, are you ready to explore the cemetery")
    input()
    print("Eddie: Yeah are you ready. have you heard the stories that once you enter there's no coming back XD")
    input()
    #IF/elif statement for a 1 pov of Jeff
    choice = input("1.Yeah I'm ready and I heard that's all a myth 2.No I'm not ready have a bad feeling\n")

    if choice == "1":
        print("Mike:Awesome we are almost here boys!")
    elif choice == "2":
        print("Mike:Don't worry about it we will be fine")
    input()
    print("Sam:No it's not a myth 2 summer ago a group of college went and are still missing.")
    input()
    print("Mike and Eddie:Stop trying to scare us it's all just a myth")
    input()
    print("Sam:I swear I'm not lying")
    input()
    print("Jeff:I don't know, I'm just going with what I heared from the media")
    input()
    print("Mike:We are here are y'all ready?")
    input()
    print("Eddie:Of course I've been waiting so long")
    input()
    print("Sam:We should just go back to my place and watch The Thing instead")
    input()
    print("Eddie:That sounds lame this is once in a life time")
    input()
    print("Mike:How about you Jeff. Should we continue or go back home")
    input()
    print("Sam and Eddie: Yeah you're our tie breaker")
    input()
    # IF/elif statement for a 1 pov of Jeff
    a = int(input("1.Let's continue our mama's didn't raise any babies 2.I agree with same like I said I have a really bad feeling\n"))
    if a == "1":
        print("Everbody:Alright let's goooo!")
    elif a == "2":
        print("Mike:Ok let me start the car again and lets go home")
        print("Mike: guys the car won't start")

    #Give the player some options of things to do here.
    #Be sure to put their choice in a variable!
    
    #Then use an if/elif/else statement to do something based on the player's choice.
    
    #One of the options should move the story to the next section with code like this:
    section_2.start(player)
    
    #Add pseudocode here to describe the rest of the functionality of this section of your game.
    #You may also draw and submit flowcharts if you prefer.
