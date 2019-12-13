# Turtle Graphics/Loops
# Dana Nguyen June 28 2016
# Part 2: Clock

# Objective: Display an ANALOG clock face with hands showing the current time
# Display/print time in digital format and analog

import turtle
import datetime

w = turtle.Screen()
c = turtle.Turtle()
# c = clock face

c.shape('square')

c.lt(90)
for n in range (0,12):
    c.up()
    c.fd(150)
    c.stamp()
    c.rt(180)
    c.fd(150)
    c.lt(150)

minute = datetime.datetime.now().minute
hour = datetime.datetime.now().hour % 12

m_degrees = -6 * minute + 90
h_degrees = -30 * (hour + (minute/60)) + 90

m = turtle.Turtle()
# m = minutes
m.pensize(3)

m.lt(m_degrees)
m.fd(120)


h = turtle.Turtle()
#h = hours
h.pensize(3)

h.lt(h_degrees)
h.fd(100)


print('Hour is', hour)
print('Minute is', minute)
