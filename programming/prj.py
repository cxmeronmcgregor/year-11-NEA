# Setup
import random
import sys
import time

# Code
print("Welcome to the Dice Game")
print("------------------------")

time.sleep(3)

authuscounter = 0
while authuscounter < 3:
    authinputuser=input("Please input your username: ")
    if authinputuser != "DesignatedUser":
        authuscounter = authuscounter + 1
    else:
        authpwcounter = 0
        while authpwcounter < 3:
            authinputpw=input("Please input your password: ")
            if authinputpw != "DesignatedPassword":
                authpwcounter = authpwcounter + 1
            else:
                print(authpwcounter)
else:
    print("You have been locked out after too many attempts.")
