# Regular Polygons
# Mr. Scott
# April 27, 2026
# Warm-up for our Turtle Confusion Assignment

# Turtle Boilerplate
import turtle, random

wn = turtle.Screen()
wn.setup(600,400)

philip = turtle.Turtle()

# Main Program
def triangle_simple():
    # using our turtle, draw a reg triangle
    # limitations:
    # - can control specific global turtle
    # - size of the triangle is fixed (100)
    for i in range(3): #i: 0, 1, 2
        philip.fd(100)
        philip.left(120)

def triangle_improved(active_turtle, length):
    # improved version of our triangle function
    # any turtle can draw a reg. triangle
    # side length can vary
    for i in range(3):
        active_turtle.fd(length)
        active_turtle.left(120)

def square(active_turtle, length):
    # use given turtle to draw a square
    for i in range(4):
        active_turtle.fd(length)
        active_turtle.left(90)

def pentagon(active_turtle, length):
    # use given turtle to draw a pentagon
    for i in range(5):
        active_turtle.fd(length)
        active_turtle.left(72)
        
def r_poly(active_turtle,x,y,s):
    # draw regular poly with s sides at x,y
    active_turtle.up() #pick up the pen
    active_turtle.goto(x,y)
    active_turtle.down() #put pen down
    
    for i in range(s):
        active_turtle.fd(250/s)
        active_turtle.left(360/s)

# draw 5, 9, 11, 15, 29 sides shapes on the screen
for sides in [5, 9, 11, 15, 29]:
    x = random.randrange(-300,300)
    y = random.randrange(-200,200)
    r_poly(philip, x,y,sides)

# pentagon(philip, 70)
# square(philip, 70)
# triangle_improved(philip, 70)
# small multi-turtle test
# turtles = []
# for i in range(10): #i: 0, 1, 2, 3, ... , 9
#     turtles.append(turtle.Turtle())
#     turtles[i].left(random.randrange(0,360))
#     triangle_improved(turtles[i], random.randrange(50,200))

#Very End
wn.exitonclick()