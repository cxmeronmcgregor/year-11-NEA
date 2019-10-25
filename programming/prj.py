# Setup
import random
import time

# Code
print("Welcome to the Dice Game")
print("------------------------")

time.sleep(3)
#Username and pwd defined in AUTH.md
counter = 5
while True:
    authinputuser=input("Please input your username: ")
    if authinputuser == "":
        print("No input detected.")
    if authinputuser !="DesignatedUser":
        ()
    if authinputuser == "DesignatedUser":
        authinputpw=input("Please input your password: ")
    if authinputpw == "DesignatedPassword":
        break
    else:
        time.sleep(counter)
        counter=counter*10
