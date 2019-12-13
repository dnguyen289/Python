# Dana Nguyen June 23 2016

import turtle

w = turtle.Screen()
t = turtle.Turtle()

for side in [20, 40, 50, 70]:
    t.down()
    for i in range(0,4):
        t.fd (side)
        t.lt(90)
    t.up()
    t.fd(side+10)
t.down()
