# Turtle Graphics Basics
# Mr. Scott
# April 24, 2026
# Making visuals with the
# turtle.py library

# you MAY NOT save your file as turtle.py!
# name it anything else!!!

import turtle, random

# TURTLE BOILERPLATE CODE:
window = turtle.Screen() #returns a "screen" obj
window.setup(600, 400) #set window dimensions
window.bgcolor("POWDERBLUE")

my_turtle = turtle.Turtle() #return "turtle" obj
my_turtle.color("tomato")    
my_turtle.pensize(3)
my_turtle.speed(0) #controls animation delay
                    # max speed
turtle.tracer(False) #disables turtle animations
                #so anything to draw all
                #appears at once.

# Main Program Starts:

#Program Three
colors = ["blue", "chartreuse", "tomato", "cadetblue", "seashell", "sandybrown"]

def color_line(steps):
    #create a single line with STEPS little lines
    for i in range(steps):
        col = random.choice(colors)
        my_turtle.color(col)
        my_turtle.fd(5)
        

for i in range(360):
    color_line(40)
    my_turtle.penup()   #.up()
    my_turtle.goto(0,0)
    my_turtle.pendown() #.down()
    my_turtle.left(1)
    if i % 5 == 0: #i==0, 5, 10, 15, 20..
        turtle.update() #updates the screen

#Program Two:
# for i in range(0,300,2):#[0, 2, 4, 6..., 198] 
#     my_turtle.fd(i)
#     my_turtle.rt(90)
    
#Program One:
# my_turtle.forward(150)
# my_turtle.left(60)
# my_turtle.forward(100)


# At the very end...
window.exitonclick()

