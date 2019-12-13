# Turtle Graphics/Loops
# Dana Nguyen June 27 2016
# Part 1: Spiral

# Objective: Create varies of spirals in Python Turtle
# Ask for a number of "sides"
# Ask for how many times to for turtle to move
# Ask for what is the percent increase for each arm

side = int(input("Enter the number of sides: "))
spir = int(input("Enter the number of times to spiral: "))
#spir = spiral (Because spiral is taken by the file name)
pct = float(input("Enter the percantage increase(Example: 12 for 12%): "))
#pct = percent for abb.

import turtle
w = turtle.Screen()
t = turtle.Turtle()
t.pensize(2)

length = 10

for i in range(0 , spir):
    t.fd(length)
    t.rt(360/side)
    length =(length * (1 + (pct / 100)))
