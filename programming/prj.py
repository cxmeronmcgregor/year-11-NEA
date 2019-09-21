### !!!! READ ME !!!! ###
# This is my coursework's source code. It's really badly made, I know. Enjoy!

# Assignment
# Katarina is developing a two-player dice game.The players roll two 6-sided dice each and get points depending on what they roll. There are 5 rounds in a game.
# In each round, each player rolls the two dice.
# The rules are:
# •The points rolled on each player’s dice are added to their score.
# • If the total is an even number, an additional 10 points are added to their score.
# • If the total is an odd number, 5 points are subtracted from their score.
# • If they roll a double, they get to roll one extra die and get the number of points rolled added to their score.
# • The score of a player cannot go below 0 at any point.
# • The person with the highest score at the end of the 5 rounds wins.
# • If both players have the same score at the end of the 5 rounds, they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins).
# Only authorised players are allowed to play the game. Where appropriate, input from the user should be validated. Design, develop, test and evaluate a program that:
# 1. Allows two players to enter their details, which are then authenticated to ensure that they are authorised players.
# 2. Allows each player to roll two 6-sided dice.
# 3. Calculates and outputs the points for each round and each player’s total score.
# 4. Allows the players to play 5 rounds.
# 5. If both players have the same score after 5 rounds, allows each player to roll 1 die each until someone wins.
# 6. Outputs who has won at the end of the 5 rounds.
# 7. Stores the winner’s score, and their name, in an external file.
# 8. Displays the score and player name of the top 5 winning scores from the external file.

import time
import random

print("Welcome to the Dice Game")
time.sleep(1)
print("Developed & Designed: Cameron McGregor")
time.sleep(1)
print("Find the source code: https://github.com/cxomeronmcgregor/year-11-NEA")
print("---------------------------------------------------------------------")
time.sleep(2)
