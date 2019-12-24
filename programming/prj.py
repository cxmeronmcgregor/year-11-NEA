# Setup
import random
import time
import sys

## TASK 1

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

## TASK 2, 3 & 4

def dice_rollp1(): #Make a new subroutine, 'Dice Roll'
    input("PLAYER 1 | Please enter to roll the dice") #Enter to continue
    time.sleep(1) #Sleep for 1 second [pause]

    dice1 = random.randint(1,6) #Creates new variable & assigns random number from 1-6
    dice2 = random.randint(1,6)
    total = dice1+dice2 #Creates new varaible, total, adds dice1 and dice2

    print ("") #Formatting
    print ("P1 Dices") #Prints title
    print ("----------") #Formatting
    time.sleep(1) #Sleep for 1 second [pause]

    print ("Dice 1:",dice1)
    print ("Dice 2:",dice2)
    print("Your total is",total)

dice_rollp1()

def dice_rollp2(): #Make a new subroutine, 'Dice Roll'
    input("PLAYER 2 | Please enter to roll the dice") #Enter to continue
    time.sleep(1) #Sleep for 1 second [pause]

    dice3 = random.randint(1,6) #Creates new variable & assigns random number from 1-6
    dice4 = random.randint(1,6)
    total2 = dice3+dice4 #Creates new varaible, total, adds dice1 and dice2

    print ("") #Formatting
    print ("P2 Dices") #Prints title
    print ("----------") #Formatting
    time.sleep(1) #Sleep for 1 second [pause]

    print ("Dice 3:",dice3)
    print ("Dice 4:",dice4)
    print("Your total is",total2)

dice_rollp2()

def dice_rollp1(): #Make a new subroutine, 'Dice Roll'
    input("PLAYER 1 | Please enter to roll the dice") #Enter to continue
    time.sleep(1) #Sleep for 1 second [pause]

    dice1 = random.randint(1,6) #Creates new variable & assigns random number from 1-6
    dice2 = random.randint(1,6)
    total = dice1+dice2 #Creates new varaible, total, adds dice1 and dice2

    print ("") #Formatting
    print ("P1 Dices") #Prints title
    print ("----------") #Formatting
    time.sleep(1) #Sleep for 1 second [pause]

    print ("Dice 1:",dice1)
    print ("Dice 2:",dice2)
    print("Your total is",total)

dice_rollp1()

def dice_rollp2(): #Make a new subroutine, 'Dice Roll'
    input("PLAYER 2 | Please enter to roll the dice") #Enter to continue
    time.sleep(1) #Sleep for 1 second [pause]
    dice3 = random.randint(1,6) #Creates new variable & assigns random number from 1-6
    dice4 = random.randint(1,6)
    total2 = dice3+dice4 #Creates new varaible, total, adds dice1 and dice2

    print ("") #Formatting
    print ("P2 Dices") #Prints title
    print ("----------") #Formatting
    time.sleep(1) #Sleep for 1 second [pause]

    print ("Dice 3:",dice3)
    print ("Dice 4:",dice4)
    print("Your total is",total2)

dice_rollp2()

def dice_rollp1(): #Make a new subroutine, 'Dice Roll'
    input("PLAYER 1 | Please enter to roll the dice") #Enter to continue
    time.sleep(1) #Sleep for 1 second [pause]

    dice1 = random.randint(1,6) #Creates new variable & assigns random number from 1-6
    dice2 = random.randint(1,6)
    total = dice1+dice2 #Creates new varaible, total, adds dice1 and dice2

    print ("") #Formatting
    print ("P1 Dices") #Prints title
    print ("----------") #Formatting
    time.sleep(1) #Sleep for 1 second [pause]

    print ("Dice 1:",dice1)
    print ("Dice 2:",dice2)
    print("Your total is",total)

dice_rollp1()

def dice_rollp2(): #Make a new subroutine, 'Dice Roll'
    input("PLAYER 2 | Please enter to roll the dice") #Enter to continue
    time.sleep(1) #Sleep for 1 second [pause]
    dice3 = random.randint(1,6) #Creates new variable & assigns random number from 1-6
    dice4 = random.randint(1,6)
    total2 = dice3+dice4 #Creates new varaible, total, adds dice1 and dice2

    print ("") #Formatting
    print ("P2 Dices") #Prints title
    print ("----------") #Formatting
    time.sleep(1) #Sleep for 1 second [pause]

    print ("Dice 3:",dice3)
    print ("Dice 4:",dice4)
    print("Your total is",total2)

dice_rollp2()

## TASK 5 & 7

if total > total2:
    print("Dice Winner: PLAYER 1")
    dicewinner = "Player 1"

    f = open ("winner.txt", "w")
    f = open ("winner.txt", "a")

    f.write(dicewinner)
    f.close()

if total2 < total:
    print("Dice Winner: PLAYER 2")
    dicewinner = "Player 2"

    f = open ("winner.txt", "w")
    f = open ("winner.txt", "a")

    f.write(dicewinner)
    f.close()

if total == total2:
    print("Redraw...")

    time.sleep(2)

    dice_rollp1()
    dice_rollp2()
