# Setup
import random
import time
import sys

# Code
print("Welcome to the Dice Game")
print("------------------------")

time.sleep(3)
while True:
    authinputuser=input("Please input your username: ")

    if authinputuser == "DesignatedUser":
        authinputpw=input("Please input your password: ")
    elif authinputuser != "DesignatedUser":
        print("Incorrect password. System restarting...")
        sys.exit()
    if authinputpw == "DesignatedPassword":
        break

print("Dice Game Starting...")

time.sleep(1)

def dice_roll(): #Make a new subroutine, 'Dice Roll'
    input("PLAYER 1 | Please enter to roll the dice") #Enter to continue
    time.sleep(1) #Sleep for 1 second [pause]

    diceus1 = random.randint(1,6) #Creates new variable & assigns random number from 1-6
    dice2 = random.randint(1,6)
    total = dice1+dice2 #Creates new varaible, total, adds dice1 and dice2

    print ("") #Formatting
    print ("Your Dices") #Prints title
    print ("----------") #Formatting
    time.sleep(1) #Sleep for 1 second [pause]

    print ("Dice 1:",dice1)
    print ("Dice 2:",dice2)
