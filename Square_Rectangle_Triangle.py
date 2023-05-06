# Draw Square in Turtle – Python
import turtle
t = turtle.Turtle()

side = int(input('Enter the length of the side of the Square: '))

# drawing first side
t.forward(side) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree

# drawing second side
t.forward(side)
t.left(90)

# drawing third side
t.forward(side)
t.left(90)

# drawing fourth side
t.forward(side)
t.left(90)

turtle.done()

# Second approach (Using Loop) for Square
import turtle
t = turtle.Turtle()

s = int(input('Enter the length of the side of the Square: '))

for _ in range(4):
    t.forward(s)
    t.left(90)
turtle.done()

# Drawing Rectangle
import turtle
t = turtle.Turtle()

l = int(input('Enter the length of the side of the Square: '))
w = int(input('Enter the width of the side of the Square: '))

t.forward(l)
t.left(90)

t.forward(w)
t.left(90)

t.forward(l)
t.left(90)

t.forward(w)
t.left(90)

turtle.done()

# Second approach (Using Loop) for Rectangle
import turtle
t = turtle.Turtle()

l = int(input('Enter the length of the side of the Square: '))
w = int(input('Enter the width of the side of the Square: '))

for _ in range(4):
    if _% 2 == 0:
        t.forward(l)
        t.left(90)
    else:
        t.forward(w)
        t.left(90)
turtle.done()

# Drawing Triangle
import turtle
t = turtle.Turtle()

s = int(input('Length of adge is: '))

for _ in range(3):
    t.forward(s)
    t.left(120)
turtle.done()

# Second approach for Triangle
import turtle
 
 
# Screen() method to get screen
wn=turtle.Screen() 
 
# creating tess object
tess=turtle.Turtle() 
 
 
def triangle(x,y):
   
    # it is used to draw out the pen
    tess.penup()
     
    # it is used to move cursor at x
    # and y position
    tess.goto(x,y)
     
    # it is used to draw in the pen
    tess.pendown()
    for i in range(3):
       
          # move cursor 100 unit
        # digit forward
        tess.forward(100)
         
        # turn cursor 120 degree left
        tess.left(120)
         
        # Again,move cursor 100 unit
        # digit forward
        tess.forward(100)
         
# special built in function to send current
# position of cursor to triangle
turtle.onscreenclick(triangle,1)
 
turtle.listen()
 
# hold the screen
turtle.done()

# Drawing Pentagon
import turtle
t = turtle.Turtle()

s = int(input('Length of adge is: '))

for _ in range(5):
    t.forward(s)
    t.left(72)
turtle.done()

# Drawing Hexagon
import turtle
t = turtle.Turtle()

s = int(input('Length of adge is: '))

for _ in range(6):
    t.forward(s)
    t.left(60)
turtle.done()

# Drawing Octagon
import turtle
t = turtle.Turtle()

s = int(input('Length of adge is: '))

for _ in range(8):
    t.forward(s)
    t.left(45)
turtle.done()

'''
Since as of now, you must have learned how to draw various basic geometrical illustrations
like circle, square, rectangle. So, lets implement this knowledge to build something
which you can really use in building games like lets draw a human being 
using the basic knowledge of geometrical knowledge.
Here the code for this implementation:-
'''
import turtle
 
def draw_dream():
    window = turtle.Screen()
    window.bgcolor("white")
    draw_Scarlett()
    window.exitonclick()
 
 
def draw_Scarlett():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    draw_head(brad)
    draw_body(brad)
    draw_arm(brad)
    draw_leg1(brad)
    draw_leg2(brad)
 
 
def draw_head(brad):
    brad.circle(60)
    brad.speed(3)
    brad.right(60)
 
 
def draw_body(brad):
    num = 0
    while num < 3:
        brad.forward(150)
        brad.right(120)
        brad.speed(1)
        num += 1
 
 
def draw_arm(brad):
    brad.forward(60)
    brad.left(60)
    brad.forward(60)
 
    brad.backward(60)
    brad.right(60)
    brad.backward(60)
 
    brad.right(60)
 
    brad.forward(60)
    brad.right(60)
    brad.forward(60)
 
    brad.backward(60)
    brad.left(60)
    brad.forward(90)
 
 
def draw_leg1(brad):
    brad.left(120)
    brad.forward(40)
    brad.right(120)
    brad.forward(120)
    draw_foot1(brad)
 
 
def draw_leg2(brad):
    brad.color("red")
    brad.right(180)
    brad.forward(120)
    brad.right(60)
    brad.forward(70)
    brad.right(60)
    brad.forward(120)
    draw_foot2(brad)
 
 
def draw_foot1(brad):
    brad.color("blue")
    num = 0
    while num < 4:
        brad.forward(20)
        brad.right(90)
        num += 1
 
 
def draw_foot2(brad):
    brad.color("blue")
    num = 0
    while num < 4:
        brad.forward(20)
        brad.left(90)
        num += 1
 
 
draw_dream()


