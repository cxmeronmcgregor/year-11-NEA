# Setup
import random
import time
import sys

# Code
print("Welcome to the Dice Game")
print("------------------------")

time.sleep(3)
counter = 5
while True:
    authinputuser=input("Please input your username: ")
    if authinputuser == "DesignatedUser":
        authinputpw=input("Please input your password: ")
    if authinputpw == "DesignatedPassword":
        break
    else:
        time.sleep(counter)
        counter=counter*10

print("Dice Game Starting...")

time.sleep(1)
