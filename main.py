# Author: Chris K.
import random


n = int(input("How many dice would you like to roll? "))  # number of die to roll
s = int(input("How many sides should the die have? "))  # number of sides on each die
if s <= 0:
    print("Sorry, that die doesn't exist! Please input a positive whole number.")
elif n <= 0:
    print("Sorry, i cant roll that many dice! Please input a positive whole number.")

for i in range(n):
    print(f"You rolled a {random.randint(1, s)}!")



