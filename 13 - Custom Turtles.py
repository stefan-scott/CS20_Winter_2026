# Custom Turtle Shapes
# Mr. Scott
# April 30, 2026
# Checking out register shape...

# Turtle Boilerplate
import turtle

wn = turtle.Screen()
wn.setup(700,700)

t = turtle.Turtle()

# Main Code Here
# 'arrow', 'classic', 'circle', 'square', 'turtle'

# Custom Shapes must be registered...
# coordinate must be stored in a tuple
new_shape = ((-30,0),(0,-30),(30,0),(0,30))
turtle.register_shape("diamond", new_shape)

t.shape("diamond")
t.speed(0)
t.color("beige")
# Using Loops, Create an Argyle Pattern
t.up()
x_start = -280
y_start = 280
t.goto(x_start,y_start)

for i in range(10):
    for j in range(10):
        t.stamp()
        t.fd(60)
    # move turtle back to start_x and decrease y
    y_start -= 60
    t.goto(x_start, y_start)

# REGISTER A GIF for turtle shape
# a few things:
# .gif only, not animated gifs
# not all gifs have transparent backgrounds
#     may need a tool to do this...
#
# image rotation is fixed; doesn't visually
# reflect the turtle's heading.
turtle.register_shape("turtle_image.gif")
t.shape("turtle_image.gif")
t.goto(0,0)

# ON-YOUR-OWN CHALLENGE
custom = turtle.Turtle()
custom.up()
custom.goto(100,0)



wn.exitonclick()