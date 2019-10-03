# Setup
import random
import sys
import time
import mysql.connector

#MySQL Database Setup (for login auth)
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="loginauthdb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE loginauthdb")

# Code
print("Welcome to the Dice Game")
print("------------------------")

time.sleep(3)
