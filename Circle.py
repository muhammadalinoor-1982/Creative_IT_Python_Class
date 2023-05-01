
# Draw a Circle using turtle programming **********************

#importing turtle module
import turtle

#Initialising the turtle object
t = turtle.Turtle()
radius = 50

#using built-in function to draw a circle
t.circle(radius)

#Finish by turtle.done() command
turtle.done()

# Draw Tangent circles using turtle programming ******
import turtle
t = turtle.Turtle()

r = 10
n = 10

for i in range(1, n + 1, 1):
    t.circle(r * i)

turtle.done()

# Draw spiral circle using turtle programming *********
import turtle
t = turtle.Turtle()
r = 10
for i in range(100):
    t.circle(r + i, 25)
turtle.done()

# Draw Concentric circles using turtle programming
import turtle
t = turtle.Turtle()
r = 10
for i in range(10):
    t.circle(r * i)
    t.up()
    t.sety((r * i)*(-1))
    t.down()
turtle.done()

