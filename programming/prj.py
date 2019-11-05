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
