## Import
import time
import sys
#Username and pwd defined in AUTH.md
authuscounter = 0
while authuscounter < 3:
    authinputuser=input("Please input your username: ")
    if authinputuser == "":
        print("No input detected.")
    if authinputuser != "DesignatedUser":
        authuscounter = authuscounter + 1
    else:
        authpwcounter = 0
        while authpwcounter < 3:
            authinputpw=input("Please input your password: ")
            if authinputpw == "":
                print("No input detected.")
            if authinputpw != "DesignatedPassword":
                authpwcounter = authpwcounter + 1
            if authinputpw == "DesignatedPassword":
                print()
else:
    print("You have been locked out after too many username attempts.")
authpwcounter = 0
while authpwcounter < 3:
    authinputpw=input("Please input your password: ")
    if authinputpw == "":
        print("No input detected.")
    elif authinputpw != "DesignatedPassword":
        authpwcounter = authpwcounter + 1
    elif authinputpw == "DesignatedPassword":
        print("Success! Logging in...")
else:
    print("You have been locked out after too many password attempts.")
