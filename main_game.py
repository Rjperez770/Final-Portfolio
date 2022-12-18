#Roberto J. Perez
#11/3/2022
#Milestone 2
#CSS 225
#Header comments go here


#Remember to put all your files into the same folder on your computer!
#Otherwise, these import statements won't be able to find them properly

#Import the main character and section files here
import section_1
import main_character
import section_2
import section_3
import church
import mausoleum
import Ending
#Intro text to the user
#The empty input functions are only here so the player has to type something to move on
player = main_character.main_character()
player.name = "Jeff"
#(like pressing a button in a video game to move the dialogue along)
print("Hello there!")
print("Welcome to my game, Escape")
print("Ready! Lets Go!")
input()

#And do/say anything else to get your game started

#Then call your first section.
section_1.start(player)
