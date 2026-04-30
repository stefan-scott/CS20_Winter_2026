# Turtle Confusion
# Mr. Scott
# April 29, 2026
# Drawing shapes / patterns with Turtle

# Boilerplate Code
import turtle

wn = turtle.Screen()
wn.setup(1000,700)

jem = turtle.Turtle()

# Function Definitions
def plus_sign(x,y,size):
    # draw plus sign at (x,y)
    # size → INT (side length)
    jem.up()
    jem.goto(x,y)
    jem.down()
    
    for i in range(4):
        jem.fd(size)
        jem.left(90)
        jem.fd(size)
        jem.right(90)
        jem.fd(size)
        jem.left(90)

# Main Code Here

jem.speed(0)
for i in range(20,111):
    plus_sign(-400,100,i)
    jem.left(4)
wn.exitonclick()

